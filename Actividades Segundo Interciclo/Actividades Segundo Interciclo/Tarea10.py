#2.	Crear una función es_par(numero) que retorne True si el número es par.
numero=int(input("ingrese un numero:"))

def numpar(numero):
    return numero % 2 == 0
print(numpar(numero))