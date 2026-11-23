import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana Adaptable")

# Hacer que 3 filas y 3 columnas se adapten al estirar/achicar la ventana
for i in range(3):
    ventana.rowconfigure(i, weight=1)
    ventana.columnconfigure(i, weight=1)

# sticky="nsew" estira cada botón hacia Norte, Sur, Este y Oeste (toda su celda)
for f in range(3):
    for c in range(3):
        btn = tk.Button(ventana, text=f"F{f+1}-C{c+1}")
        btn.grid(row=f, column=c, sticky="nsew", padx=5, pady=5)

ventana.mainloop()
