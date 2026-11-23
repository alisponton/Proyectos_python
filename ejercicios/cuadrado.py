def calcular_cuadrado(n):
    cuadrado = n * n
    print("El cuadrado de", n, "es:", cuadrado)
    input("Presione Enter para continuar...")  # Pausa hasta presionar Enter


numero=1
while numero != 0:
    numero=int(input("Ingrese un número: "))
    if numero != 0:
        calcular_cuadrado(numero)
        