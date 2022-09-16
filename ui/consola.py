def menu():
    seleccion = 0
    print("1. registrar nueva moto:")
    seleccion = int(input("seleccione una opcion"))
    if seleccion == 1:
        registrar()


def registrar():
    placa = str(input("introduzca placa"))
    modelo = str(input("introduzca modelo"))
    marca = str(input("introduzca marca"))
    categoria = int(input("seleccione 1.usado o 2.nuevo"))
    precio_unitario = int(input("introduza el precio de venta de la moto"))
    cantidad = int(input("introduzca la cantidad "))


menu()