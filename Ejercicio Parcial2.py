#Estructuras de control y bucles

print("Estructuras de control y bucles")

#Bucle while

a = int(input("Introduce un numero: "))

while a < 0:
    print("El numero introducido es negativo")
    a = int(input("Introduce un numero: "))
else:
    print("El numero introducido es positivo")


A = 0
B = 0

for i in range(0,a):
    A = 1 - 1 / (i+1)
    B += 1 / (i+1)
    while (i+1) == a:
        print("El resultado de la sumatoria es: ", A )
        print(f"\nEl resultado de la multiplicacion es: ", B)
        break



