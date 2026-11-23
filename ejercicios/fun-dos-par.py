# 1. DEFINICIÓN DE LA FUNCIÓN (Devuelve 2 valores)
def calcular_potencias(n):
    cuadrado = n * n
    cubo = n * n * n
    otro = n * 10  # <-- Este valor no se utiliza en el programa principal
    return cubo, cuadrado, otro  # <-- Envía ambos valores separados por coma

# 2. PROGRAMA PRINCIPAL
numero = 1
while numero != 0:
    numero = int(input("\nIngrese un número (0 para salir): "))
    
    if numero != 0:
        # Atrapa los dos valores en el mismo orden en que salieron
        res_cuadrado, res_cubo, res_otro = calcular_potencias(numero)
        
        print("El cuadrado es:", res_cuadrado)
        print("El cubo es:", res_cubo)
        print("Otro valor:", res_otro)  # <-- Esto generará un error porque 'otro' no está definido 

print("Programa finalizado.")
