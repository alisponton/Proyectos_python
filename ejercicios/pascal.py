def generar_triangulo_pascal(n):
    triangulo = []

    for i in range(n):
        fila = [1] * (i + 1)
        for j in range(1, i):
            fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        triangulo.append(fila)

    return triangulo

def mostrar_triangulo_pascal(triangulo):
    for fila in triangulo:
        print(' '.join(map(str, fila)).center(2 * len(triangulo)))

num_filas = int(input("Introduce el número de filas para el Triángulo de Pascal: "))
triangulo = generar_triangulo_pascal(num_filas)
mostrar_triangulo_pascal(triangulo)
#linea agregada en ubunto despues de descargar
#desde gdrive usando syn_drive.