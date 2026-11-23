import tkinter as tk

def accion_nuevo():
    etiqueta.config(text="Elegiste: Nuevo Registro")

def accion_reporte():
    etiqueta.config(text="Elegiste: Ver Reporte")

ventana = tk.Tk()
ventana.title("Ejemplo de Barra de Menú")
ventana.geometry("400x200")

# 1. Crear la barra principal de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)  # Conecta la barra a la ventana

# 2. Crear el menú desplegable "Archivo" (tearoff=0 quita una línea punteada antigua)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# 3. Agregar las opciones dentro de "Archivo"
menu_archivo.add_command(label="Nuevo", command=accion_nuevo)
menu_archivo.add_command(label="Reporte", command=accion_reporte)
menu_archivo.add_separator()  # Dibuja una línea divisoria
menu_archivo.add_command(label="Salir", command=ventana.destroy)

etiqueta = tk.Label(ventana, text="Usa el menú superior para elegir una opción", font=("Arial", 12))
etiqueta.pack(expand=True)

ventana.mainloop()
