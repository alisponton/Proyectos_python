import os
os.system("clear")
contador = 1
while contador <= 3:
    print(contador)
    contador = contador + 1
    if contador == 2:
        print("Bucle en 2")  # Con sangría = equivalente a EXIT
        print()
print("Bucle terminado")  # Sin sangría = equivalente a ENDDO
os.system("time")