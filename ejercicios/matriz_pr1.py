import random
import tkinter as tk
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
#voy a rellenar la matriz
m_lista = []
for i in range(filas):
    #m_lista.append(i+1)
    linea=[]
    
    for j in range(columnas):
        
        linea.append(random.randint(1, 99))

    m_lista.append(linea)

#mostrar la matriz
#for i in range(filas):
#    for j in range(columnas):
#        print(f"{m_lista[i][j]:02d}", end=" ")
#    print()

#     
# --- (Debajo de tu código comentado de mostrar la matriz) ---

# PASO 1: Crear la ventana principal en memoria
ventana = tk.Tk()
ventana.title("Mi Matriz de Botones")

# PASO 2: Recorrer tu matriz para fabricar un botón por cada celda
for i in range(filas):
    for j in range(columnas):
        valor = m_lista[i][j]
        
        # Fabricar el botón (aún no aparece en pantalla hasta usar .grid)
        boton = tk.Button(ventana, text=f"{valor:02d}", width=4, height=2)
        
        # Colocarlo en la cuadrícula visual en la fila 'i' y columna 'j'
        boton.grid(row=i, column=j, padx=4, pady=4)

# PASO 3: Encender la ventana y mantenerla abierta en pantalla
ventana.mainloop()
