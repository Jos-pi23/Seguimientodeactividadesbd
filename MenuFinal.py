from sqlalchemy import create_engine, Table, MetaData,select
import pymysql


engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/employees')
connection = engine.connect()

ingresa = False
while ingresa == False:
    print("Bienvenidos")
    print("Menu de opciones")
    print("1. Ingresar a cuenta")
    print("2. Crear cuenta")
    ingreOP = input("Ingrese una opción: ")
    if ingreOP.isdigit():
        if ingreOP == "1":
            ingreUser = input("Ingrese su email: ")
            stmt1 = "select mail from usuario where mail = '"+ ingreUser + "'"
            results1 = connection.execute(stmt1).fetchmany(1)
            ingrePass = input("Ingrese su contraseña: ")
            stmt2 = "select password from usuario where password = '"+ ingrePass + "'"
            results2 = connection.execute(stmt2).fetchmany(1)
            if (len(results1) == 1 and len(results2) == 1):
                print("Ingreso completado")
                ingresa=True
        elif ingreOP == "2":
            newNombre = input("Ingrese su nombre: ")
            newMail = input("Ingrese un email: ")
            newPass = input("Ingrese una contraseña: ")
            print("¿Desea ser lider?")
            print("1. True \n2.False")
            op1 = input("Ingrese una opción: ")
            esLider = False
            if(op1 == "1"):
                esLider = True
            print("¿Desea ser colaborador?")
            print("1. True \n2.False")
            op2 = input("Ingrese una opción: ")
            esColaborador = False
            if(op1 == "1"):
                esColaborador = True
            stmt = "insert into Usuario values ('"+ newNombre + "', '"+newMail + "', '" + newPass + "'," + esLider + ", "+esColaborador+")"
            print("Cuenta registrada")
            print("¿Desea regresar? si/no")
        else:
            print("Opción no válida")
menuPrincipal()

def menuPrincipal():
    print("VENTANA PRINCIPAL")
    print("1. Crear proyectos")
    print("2. Ver proyectos")
    print("0. Cerrar sesion")
    ingreOP1 = input("Ingrese una opción: ")
    while ingreOP != "0":
        if ingreOP.isdigit():
            if ingreOP == "1":
                CrearProyecto()
            elif ingreOP == "2":
                # llamar a una funcion
                break
            else:
                print("Opción no válida")
    print("Sesion cerrada")

def asignarUsuarios (cant):
    listaUsuarios = []
    for i in range(cant):
        usuario = input("Ingrese el correo del usuario: ")
        listaUsuarios.append(usuario)
    return listaUsuarios

def crearTareas(cant):
    listaTareas = []
    for i in range(cant):
        nombre = input("Ingrese el nombre de la tarea: ")
        fecha = input("Ingrese fecha de entrega: ")
        descripcion = input("Ingrese la descripción: ")
        tupla = (nombre,fecha,descripcion)
        listaTareas.append(tupla)
    return listaTareas

def asignarTareas(listaUsuarios,listaTareas):
    l_usuarioTarea = []
    for usuario in listaUsuarios:
        print(f"Usuario: {usuario}")
        print(listaTareas)
        print("Ingrese la opción que le asigna al usuario")

def CrearProyecto():
    print("Menu de opciones")
    print("1. Asignar usuarios colaboradores")
    print("2. Crear tarea")
    print("3. Asignar tareas a colaboradores")
    print("4. Regresar")
    ingrePro = input("Ingrese una opción: ")
    if ingrePro.isdigit():
        if ingrePro == "1":
            cantiUsuarios = int(input("Ingrese la cantidad de colaboradores: "))
            usuariosAsig = asignarUsuarios(cantiUsuarios)
        elif indrePro== "2":
            cantiTareas = int(input("Ingrese la cantidad de tareas: "))
            tareasCreadas = crearTareas(cantiTareas)
            print("Menu de opciones")
            print("1. Asignar tareas a colaboradores: ")
            print("2. Regresar")
            ingrePro2 = input("Ingrese una opción: ")
            if ingrePro2.isdigit():
                if ingrePro2 == "1":
                    asignaciones = asignarTareas(usuariosAsig,tareasCreadas)

        else:
            print("Opción no válida")


print("PROYECTOS ASIGNADOS")
print("Lista de proyectos creados")
stmt3 = "select titulo from Proyecto where lider = '"+ ingrePass + "'"
resultsPC = connection.execute(stmt3).fetchmany()
print(resultsPC)
ingre = input("Eija un proyecto: ")
if ingre.isdigit():
    if ingre == "1":
        print("PROYECTO POO")
        print("Menú de opciones")
        print("1. Ver participantes")
        print("2. Ver tareas")
        ingre = input("Eija una opción: ")
        if ingre.isdigit():
            if ingre == "1":
                print("Participantes: Joel, Miguel, Juan")
            elif ingre == "2":
                print("TAREAS")
                print("1. Tarea Array")
                ingre = input("Eija una tarea: ")
                if ingre.isdigit():
                    if ingre == "1":
                        print("Nombre de la tarea: Tarea Array")
                        print("Estado de la tarea: Pendiente")
                        print("Descripción: Crear una lista Arraylist con los nombres de sus familiares")
                        print("Fecha de asignación: 7/10/2022")
                        print("Fecha de entrega: 15/10/2022")
                        print("Menú de opciones")
                        print("1. Pedir ampliación")
                        print("2. Hacer tarea")
                        ingre = input("Eija una tarea: ")
                        if ingre.isdigit():
                            if ingre == "1":
                                amplia = input("Ingrese el motivo de la solicitud de ampliación: ")
                            elif ingre == "2":
                                print("Menú de opciones")
                                print("1. Abrir cuadro de texto")
                                print("2. Subir archivo")
                            else:
                                print("Opción no válida")

                    else:
                        print("Tarea no existente")

            else:
                print("Opción no válida")

    else:
        print("Proyecto no existente")


print("PROYECTOS CREADOS")
print("Lista de proyectos creados")
print("1. Proyecto POO")
ingre = input("Eija un proyecto: ")
if ingre.isdigit():
    if ingre == "1":
        print("PROYECTO POO")
        print("Menú de opciones")
        print("1. Ver participantes")
        print("2. Ver tareas")
        ingre = input("Eija una opción: ")
        if ingre.isdigit():
            if ingre == "1":
                print("Participantes: Joel, Miguel, Juan")
                print("Menú de opciones")
                print("1. Agregar participante")
                print("2. Eliminar participante")
                ingre = input("Elija una opcion: ")
                nombres = ["Joel", "Miguel", "Juan"]
                if ingre.isdigit():
                    if ingre == "1":
                        nombre = input("Ingrese el nombre del nuevo participante: ")
                        nombres.append(nombre)
                        print("Participante agregado con exito")
                    elif ingre == "2":
                        nombre = input("Ingrese el nombre del participante a ser eliminado: ")
                        if nombre in nombres:
                            nombres.remove(nombre)
                            print("Participante eliminado con exito")
                        else:
                            print("El nombre ingresado no esta en la lista de participantes")

            elif ingre == "2":
                print("TAREAS")
                print("1. Tarea Array")
                ingre = input("Eija una tarea: ")
                if ingre.isdigit():
                    if ingre == "1":
                        print("Nombre de la tarea: Tarea Array")
                        print("Estado de la tarea: Pendiente")
                        print("Descripción: Crear una lista Arraylist con los nombres de sus familiares")
                        print("Fecha de asignación: 7/10/2022")
                        print("Fecha de entrega: 15/10/2022")
                        print("Menú de opciones")
                        print("1. Revisar ampliación")
                        print("2. Revisar tarea")
                        ingre = input("Eija una tarea: ")
                        if ingre.isdigit():
                            if ingre == "1":
                                print("Solicitudes de ampliación recibidas")
                                print("1. Solicitud de Joel")
                                ingre = input("Eija una solicitud: ")
                                if ingre.isdigit():
                                    if ingre == "1":
                                        print("Descripción de la solicitud: ...")
                                        print("Menú de opciones")
                                        print("1. Aceptar solicitud")
                                        print("2. Rechazar solicitud")
                                        ingre = input("Eija una solicitud: ")
                                        if ingre.isdigit():
                                            if ingre == "1":
                                                newFecha = input("Ingrese la nueva fecha: ")
                                                print("Solicitud aprobada")
                                            elif ingre == "2":
                                                print("Solicitud rechazada")
                                    else:
                                        print("Solicitud no existente")

                            elif ingre == "2":
                                print("---Visualización de la tarea---")
                                print("Menú de opciones")
                                print("1. Calificar tarea")
                                print("2. Rechazar tarea")
                                ingre = input("Eija una opción: ")
                                if ingre.isdigit():
                                    if ingre == "1":
                                        nota = input("Ingrese la calificación: ")
                                    elif ingre == "2":
                                        print("Tarea rechazada")
                                        obser = input("Ingrese alguna observación: ")
                                    else:
                                        print("Opción no válida")
                            else:
                                print("Opción no válida")

                    else:
                        print("Tarea no existente")

            else:
                print("Opción no válida")

    else:
        print("Proyecto no existente")
