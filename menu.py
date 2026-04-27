from lista import josephus
def menu():
    while True:
        print("1. ejecutar algoritmo")
        print("2. salir")

        opcion= input("seleccione opcion: ")

        if opcion == "1":
            try:
                n=int(input("Ingrese toatl de datos (n): "))
                k=int(input("Ingrese salt (k): "))

                res = josephus(n, k)
                print("El que queda es:",res)
            except ValueError:
                print("Ingrese otro valor")
        elif opcion == "2":
            break

menu()


    