import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x250")

# Cambia la fuente por defecto para TODOS los botones de esta ventana
ventana.option_add("*Button.Font", "Helvetica 14 bold")

# Ahora ninguno necesita el parámetro font=
tk.Button(ventana, text="Botón 1").pack(pady=10)
tk.Button(ventana, text="Botón 2").pack(pady=10)
tk.Button(ventana, text="Botón 3").pack(pady=10)

ventana.mainloop()
