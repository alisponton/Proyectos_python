import os
import tkinter as tk

# 1. Oculta todas las demás aplicaciones abiertas en macOS (Equivalente a Cmd + Option + H)
os.system('''osascript -e 'tell application "System Events" to set visible of every process whose visible is true and name is not "Python" to false' ''')

def accion_nuevo():
    etiqueta.config(text="Elegiste: Nuevo Registro")

def accion_reporte():
    etiqueta.config(text="Elegiste: Ver Reporte")

ventana = tk.Tk()
ventana.title("Ejemplo de Barra de Menú")
ventana.geometry("400x200")

# 2. Crear la barra principal de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo ", menu=menu_archivo)
barra_menu.add_cascade(label="Editar ", menu=tk.Menu(barra_menu, tearoff=0))
barra_menu.add_cascade(label="listados ", menu=tk.Menu(barra_menu, tearoff=0))
barra_menu.add_cascade(label="Ayuda ", menu=tk.Menu(barra_menu, tearoff=0))
#submenu de Archivo
menu_archivo.add_command(label="Nuevo", command=accion_nuevo)
menu_archivo.add_command(label="Reporte", command=accion_reporte)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)
#submenu de Editar
menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Editar 01")
menu_editar.add_command(label="Editar 02")
menu_editar.add_command(label="Editar 03")
#
barra_menu.add_cascade(label="Editar", menu=menu_editar)
etiqueta = tk.Label(ventana, text="Usa el menú superior para elegir una opción", font=("Arial", 12))
etiqueta.pack(expand=True)

# 3. Asegura que tu ventana quede activa y al frente de todo
ventana.lift()
ventana.focus_force()

ventana.mainloop()
