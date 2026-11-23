fila=[]
for i in range(0, 10):
    fila.append(i)
    fila[i]=i+1
    print (fila[i])
print(fila[0:10])
#
print()
filas_col=[]
for i in range(0, 5):
    filas_lin=[]
    for j in range(0, 5):
        filas_lin.append(j+1)
    filas_col.append(filas_lin)
    for j in range(0, 5):
        print (f"{filas_col[i][j]:02d}", end=" ")
    print()
    # Reemplazar el tercer valor de la fila 3 por el número 99
filas_col[2][2] = 99

print("\nMatriz después de cambiar filas_col[2][2]:")
for i in range(0, 5):
    for j in range(0, 5):
        print(f"{filas_col[i][j]:02d}", end=" ")
    print()
# esta linea fue agregada con el editor en github
