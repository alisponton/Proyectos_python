while True:
    try:
        num = float(input("Ingresa el valor (ej. 12.50): "))
        if 0 <= num <= 99.99:
            break  # Sale del ciclo si cumple el rango 99.99
        else:
            print("Error: El número debe estar entre 0.00 y 99.99")
    except ValueError:
        print("Error: Solo se permiten números.")

# Formateo de salida equivalente a PICTURE "99.99"
print(f"Valor guardado: {num:05.2f}")

# Fin del programa, linea anandida en ubuntu vscode
print("Programa terminado.")
# otra linea de prueba *****