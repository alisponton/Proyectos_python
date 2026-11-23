import tkinter as tk

ventana = tk.Tk()
ventana.title("Botones Centrados")
ventana.geometry("500x350")

# 1. Botón centrado HORIZONTALMENTE arriba (50% ancho, 60px desde arriba)
btn_arriba = tk.Button(ventana, text="Centrado Arriba", font=("Arial", 14, "bold"))
btn_arriba.place(relx=0.5, y=60, anchor="center")

# 2. Botón centrado en el CENTRO EXACTO de toda la ventana (50% ancho, 50% alto)
btn_centro = tk.Button(ventana, text="Centro Exacto", font=("Arial", 16, "bold"), fg="blue")
btn_centro.place(relx=0.5, rely=0.5, anchor="center")

# 3. Botón centrado HORIZONTALMENTE abajo (50% ancho, 85% alto)
btn_abajo = tk.Button(ventana, text="Cerrar", font=("Arial", 12), fg="red", command=ventana.destroy)
btn_abajo.place(relx=0.5, rely=0.85, anchor="center")

ventana.mainloop()
