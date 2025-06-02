#Crea un mini programa que use al menos 3 funciones. Algunas ideas:
def agregar_contacto(agenda):
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print("Contacto agregado.\n")

def mostrar_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.\n")
    else:
        print("Contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
        print()

def buscar_contacto(agenda):
    nombre = input("Nombre a buscar: ")
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}\n")
    else:
        print("Contacto no encontrado.\n")

def menu():
    agenda = {}
    while True:
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            mostrar_contactos(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            print("Adiós.")
            break
        else:
            print("Opción no válida.\n")

menu()