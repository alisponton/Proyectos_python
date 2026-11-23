# Definición: recibe dos parámetros separados por coma
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total  # Devuelve el resultado al programa principal

# Programa principal
p = float(input("Precio: "))
c = int(input("Cantidad: "))

# Llamada: el valor devuelto por 'return' se guarda en 'resultado'
resultado = calcular_total(p, c)
print("Total a pagar:", resultado)
