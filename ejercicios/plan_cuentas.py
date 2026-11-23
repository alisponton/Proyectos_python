import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# 1. CONEXIÓN Y CREACIÓN DE LA TABLA EN SQLITE
conexion = sqlite3.connect("contabilidad_prueba.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cuentas (
        codigo TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL
    )
""")
conexion.commit()

# 2. FUNCIONES PARA GUARDAR Y MOSTRAR DATOS
def guardar_cuenta():
    cod = entry_codigo.get().strip()
    nom = entry_nombre.get().strip()
    tip = combo_tipo.get()

    if not cod or not nom:
        messagebox.showwarning("Aviso", "Completa el código y el nombre.")
        return

    try:
        cursor.execute("INSERT INTO cuentas VALUES (?, ?, ?)", (cod, nom, tip))
        conexion.commit()
        entry_codigo.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        cargar_tabla()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Ese código de cuenta ya existe.")

def cargar_tabla():
    # Limpia la cuadrícula y vuelve a leer desde SQLite
    for fila in tabla.get_children():
        tabla.delete(fila)
    cursor.execute("SELECT codigo, nombre, tipo FROM cuentas ORDER BY codigo")
    for registro in cursor.fetchall():
        tabla.insert("", tk.END, values=registro)

# 3. INTERFAZ GRÁFICA (FORMULARIO TKINTER)
ventana = tk.Tk()
ventana.title("Catálogo de Cuentas - Prueba")
ventana.geometry("480x350")

# Campos de captura (equivalente a TextBox y ComboBox)
tk.Label(ventana, text="Código:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_codigo = tk.Entry(ventana, width=15)
entry_codigo.grid(row=0, column=1, sticky="w")

tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.grid(row=1, column=1, sticky="w")

tk.Label(ventana, text="Tipo:").grid(row=2, column=0, padx=10, pady=8, sticky="e")
combo_tipo = ttk.Combobox(ventana, values=["Activo", "Pasivo", "Patrimonio", "Ingreso", "Gasto"], state="readonly", width=15)
combo_tipo.current(0)
combo_tipo.grid(row=2, column=1, sticky="w")

btn_guardar = tk.Button(ventana, text="Guardar Cuenta", command=guardar_cuenta)
btn_guardar.grid(row=3, column=1, pady=10, sticky="w")

# Cuadrícula de datos (equivalente al Grid de Visual FoxPro)
tabla = ttk.Treeview(ventana, columns=("codigo", "nombre", "tipo"), show="headings", height=8)
tabla.heading("codigo", text="Código")
tabla.heading("nombre", text="Nombre de la Cuenta")
tabla.heading("tipo", text="Tipo")
tabla.column("codigo", width=80)
tabla.column("nombre", width=240)
tabla.column("tipo", width=110)
tabla.grid(row=4, column=0, columnspan=2, padx=15, pady=10)

cargar_tabla()
ventana.mainloop()
conexion.close()
