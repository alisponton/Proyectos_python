import random  # Librería para generar números aleatorios (como RAND() en FoxPro)

# 1. Pedir dimensiones por teclado
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# 2. Crear y rellenar la matriz
matriz = []  # La matriz nace vacía

for f in range(filas):
    fila_actual = []  # Creamos una fila nueva vacía en cada vuelta
    
    for c in range(columnas):
        numero_aleatorio = random.randint(1, 99)  # Número entero entre 1 y 99
        fila_actual.append(numero_aleatorio)      # Agregamos el número a la fila
        
    matriz.append(fila_actual)  # Agregamos la fila completa a la matriz

# 3. Mostrar la matriz en pantalla en forma de tabla
print("\nMatriz generada:")
for f in range(filas):
    for c in range(columnas):
        # :02d alinea todos los números a 2 dígitos (ej. 05) y end="  " los pone en fila
        print(f"{matriz[f][c]:02d}", end="  ")
    print()  # Salto de línea al terminar cada fila
