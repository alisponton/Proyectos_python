import tkinter as tk

# 1. Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Laboratorio de Botones y Diseño")
ventana.geometry("500x350")  # Tamaño fijo de la ventana: 500 ancho x 350 alto (píxeles)

# 2. Botón 1: Grande, fuente Helvetica negrita, ubicado por coordenadas exactas (x, y)
btn_grande = tk.Button(
    ventana,
    text="Botón Principal (Helvetica 18)",
    font=("Helvetica", 18, "bold"),
    fg="blue",
    width=25,
    height=2
)
btn_grande.place(x=50, y=30)  # A 50px del borde izquierdo y 30px desde arriba

# 3. Botón 2: Fuente tipo máquina de escribir (Courier), más compacto
btn_mediano = tk.Button(
    ventana,
    text="Estilo Courier 14",
    font=("Courier", 14, "italic"),
    fg="darkgreen",
    width=20,
    height=1
)
btn_mediano.place(x=50, y=140)

# 4. Botón 3: Pequeño y deshabilitado (como ENABLED = .F. en FoxPro)
btn_inactivo = tk.Button(
    ventana,
    text="Deshabilitado",
    font=("Arial", 11),
    state="disabled"  # 'normal' lo activa, 'disabled' lo bloquea en gris
)
btn_inactivo.place(x=320, y=140)

# 5. Botón 4: Botón de cierre usando la función interna ventana.destroy
btn_salir = tk.Button(
    ventana,
    text="Cerrar Ventana",
    font=("Arial", 12, "bold"),
    fg="red",
    command=ventana.destroy  # Cierra la ventana limpiamente
)
btn_salir.place(x=180, y=260)

ventana.mainloop()
