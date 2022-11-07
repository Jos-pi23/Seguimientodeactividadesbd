print("Menu de opciones")
print("Bienvenid@")
print("1. Ingresar a cuenta")
print("2. Crear cuenta")
ingreOP = int(input("Ingrese una opción: "))
if ingreOP == 1:
    ingreUser = input("Ingrese su email: ")
    ingrePass = input("Ingrese su password: ")
elif ingreOP == 2:
    newNombre = input("Ingrese su nombre: ")
    newNombre = input("Ingrese un email: ")
    newNombre = input("Ingrese una contraseña: ")
    print("Cuenta registrada")
else:
    print("Opción no válida")
