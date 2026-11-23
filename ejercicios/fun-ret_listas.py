# 1. DEFINICIÓN DE LA FUNCIÓN (Devuelve una lista con 3 elementos)
def calcular_potencias(n):
    cuadrado = n * n
    cubo = n * n * n
    otro = n * 10
    return [cuadrado, cubo, otro]  # <-- Los corchetes [] crean la lista

# 2. PROGRAMA PRINCIPAL
numero = 1
while numero != 0:
    numero = int(input("\nIngrese un número (0 para salir): "))
    
    if numero != 0:
        # Una sola variable recibe toda la lista completa
        resultados = calcular_potencias(numero)
        
        # Se accede a cada dato usando su posición entre corchetes (empezando en 0)
        print("Lista completa:", resultados)
        print("El cuadrado es:", resultados[0])
        print("El cubo es:", resultados[1])
        print("Otro valor:", resultados[2])

print("Programa finalizado.")
