k=5
k = int(input("Ingrese un número: "))
for i in range(1, k):
    print(" " * (10 - i), end="")
    for j in range(1, i + 1):
        print(f"{j} ", end="")
    print()
    
   for i in range(1, k):
         print (i)