#Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0
numero = int(input("Ingresa un número (Ingrese el numero 0 para finalizar y obtener su resultado): "))
while numero!= 0:
    suma += numero
    numero = int(input("Ingresa un número (Ingrese el numero 0 para finalizar y obtener su resultado): "))
print("La suma total es:", suma)
#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
numero = 32
intento = int(input("Adivina el número entre 1 y 100: "))

while intento != numero:
    if intento < numero:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")
    intento = int(input("Intenta de nuevo: "))

print("Excelente el numero que has ingresado ha sido el correcto.")

#Validar contraseña (repetir hasta que coincida con una guardada).
contraseña = "rocky"
entrada= input("Ingrese la contraseña:")
while entrada != contraseña:
    print("La contraseña que has ingresado es incorrecta, intentelo de nuevo")
    entrada = input("Ingrese la contraseña:")
    print("La contraseña ingresada ha sido la correcta.")


#Simular un cajero automático (menú: retirar, depositar, salir).
opcion = ""
while opcion != "3":
    print(" Bienvenido ")
    print(" Ingrese 1 para depositar dinero")
    print(" Ingrese 2 para retirar dinero")
    print(" Ingrese 3 para salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("¿Que monto de dinero deseas retirar? "))
        print("Has retirado $",monto )
    elif opcion == "2":
        monto = float(input("¿Cual es el monto a depositar? "))
        print("Se ha depositado $",monto)
    elif opcion == "3":
        print("Gracias, hasta luego.")
    else:
        print("Opción no válida. Intenta de nuevo.")

#Calcular la raíz cuadrada por aproximación (método babilónico).
def raiz_babilonica(n, aproximacion_inicial=1.0, iteraciones=10):
    x = aproximacion_inicial
    for i in range(iteraciones):
        x = (x + n / x) / 2
        print(f"Iteración {i+1}: {x}")
    return x 
n = float(input("Ingrese un número: "))
raiz = raiz_babilonica(n)
print(f"La raíz cuadrada de {n} es aproximadamente {raiz}")

#Contar dígitos de un número entero (ej: 456 → 3).
print("Ingrese un número entero: ")
num = int(input())
cont = 0
while num > 0:
    num = num // 10
    cont += 1
print(f"El número tiene {cont} dígitos")
#Generar la secuencia de Fibonacci hasta un límite.
limite = int(input("Ingrese el límite de la secuencia de Fibonacci: "))
a, b = 0, 1
while a < limite:
    print(a, end=" ")
    a, b = b, a + b
print()
print("Secuencia de Fibonacci hasta el límite:", limite)
#Encontrar números primos en un rango dado.
def nprimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))
print("Números primos en el rango",inicio, "a",fin, ":")
for numero in range(inicio,fin + 1):
    if nprimo(numero):
        print(numero)
print("rango final")

#Simular un temporizador (contar regresivamente desde N).
n=int(input("ingrese el numero de donde empieze le conteo regresivo:"))
while n>=0:
    print(n)
    n=n-1
print("Fin")
#Leer archivos línea por línea hasta fin de archivo.

contador = 0 
while contador<=6:
    print("Numero:", contador)
    contador += 1