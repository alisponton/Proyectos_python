n=int(input("Ingrese un número: "))
for i in range(1, n+1):
    #print(i)
    print(i,"=", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print("Fin del programa")
