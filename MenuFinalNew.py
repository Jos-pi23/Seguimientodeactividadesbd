from sqlalchemy import create_engine, Table, MetaData, select
import pymysql


engine = create_engine(
    'mysql+pymysql://root:password@127.0.0.1:3306/employees')
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
            stmt1 = "select mail from usuario where mail = '" + str(ingreUser) + "'"
            results1 = connection.execute(stmt1).fetchmany(1)
            ingrePass = input("Ingrese su contraseña: ")
            stmt2 = "select password from usuario where password = '" + str(ingrePass) + "'"
            results2 = connection.execute(stmt2).fetchmany(1)
            # codigo del usuario
            stmtuser = "select id_user from Usuario where mail = '" + str(ingreUser) + "'"
            id_user = stmtuser[0]
            if (len(results1) == 1 and len(results2) == 1):
                print("Ingreso completado")
                ingresa = True
        elif ingreOP == "2":
            newNombre = input("Ingrese su nombre: ")
            newMail = input("Ingrese un email: ")
            newPass = input("Ingrese una contraseña: ")
            print("¿Desea ser lider?")
            print("1. True \n2.False")
            op1 = input("Ingrese una opción: ")
            esLider = False
            if (op1 == "1"):
                esLider = True
            print("¿Desea ser colaborador?")
            print("1. True \n2.False")
            op2 = input("Ingrese una opción: ")
            esColaborador = False
            if (op1 == "1"):
                esColaborador = True
            stmt = "insert into Usuario values ('" + newNombre + "', '"+newMail + \
                                                "', '" + newPass + "'," + esLider + ", "+esColaborador+")"
            print("Cuenta registrada")
            print("¿Desea regresar? si/no")
        else:
            print("Opción no válida")
menuPrincipal()
connection.close()

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


def asignarUsuarios(cant):
    listaUsuarios = []
    for i in range(cant):
        usuario = input("Ingrese el correo del usuario: ")
        listaUsuarios.append(usuario)
    return listaUsuarios
def eliminarUsuario(cant):
    print("Usuario eliminado exitosamente")
def crearTareas(cant):
    listaTareas = []
    for i in range(cant):
        nombre = input("Ingrese el nombre de la tarea: ")
        fecha = input("Ingrese fecha de entrega: ")
        descripcion = input("Ingrese la descripción: ")
        tupla = (nombre, fecha, descripcion)
        listaTareas.append(tupla)
    return listaTareas

def asignarTareas(listaUsuarios, listaTareas):
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
            cantiUsuarios = int(
                input("Ingrese la cantidad de colaboradores: "))
            usuariosAsig = asignarUsuarios(cantiUsuarios)
        elif indrePro == "2":
            cantiTareas = int(input("Ingrese la cantidad de tareas: "))
            tareasCreadas = crearTareas(cantiTareas)
            print("Menu de opciones")
            print("1. Asignar tareas a colaboradores: ")
            print("2. Regresar")
            ingrePro2 = input("Ingrese una opción: ")
            if ingrePro2.isdigit():
                if ingrePro2 == "1":
                    asignaciones = asignarTareas(usuariosAsig, tareasCreadas)

        else:
            print("Opción no válida")


def menuProyectoAsignados():
    print("PROYECTOS ASIGNADOS")
    print("Lista de proyectos creados")
    stmt3 = "SELECT p.titulo FROM Registro_inscripcion r join Proyecto p on r.proyecto = p.id_proyecto and r.lider = p.lider where r.colaborador = "+str(id_user)
    resultsPro = connection.execute(stmt3).fetchmany()
    indice = 1
    for e in resultsPro:
        print(indice+". "+e)
        indice += 1
    ingre = int(input("Eija un proyecto: "))
    if ingre <= len(resultsPro):
        proelegido = resultsPro[ingre-1]
        print(proelegido.upper())
        stmtidPro = "SELEC id_proyecto FROM Proyecto where titulo = '" +proelegido+ "'"
        id_pro = stmtidPro[0]
        print("Menú de opciones")
        print("1. Ver participantes")
        print("2. Ver tareas")
        ingre = input("Eija una opción: ")
        if ingre.isdigit():
            if ingre == "1":
                print("PARTICIPANTES")
                stmt4 = "SELECT u.nombre FROM Usuario u join Registro_inscripcion r ON u.id_user = r.colaborador WHERE r.proyecto = "+str(id_pro)
                resultsPart = connection.execute(stmt4).fetchmany()
                indice = 1
                for p in resultsPart:
                    print(indice+". "+p)
                    indice += 1
            elif ingre == "2":
                print("TAREAS")
                stmt5 = "SELECT titulo FROM Tarea WHERE proyecto = "+str(id_pro)+"and colaborador = "+str(id_user)
                resultsTar = connection.execute(stmt5).fetchmany()
                indice = 1
                for t in resultsTar:
                    print(indice+". "+t)
                    indice += 1
                ingre = int(input("Eija una tarea: "))
                if ingre <= len(resultsTar):
                    tarElegida = resultsTar[ingre-1]
                    print(tarElegida.upper())
                    stmtidTar = "SELECT id_tarea FROM Tarea where titulo = '" +tarElegida+ "' and colaborador = "+str(id_user)
                    id_tar = stmtidTar[0]
                    print("Nombre de la tarea: ")
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
                print("Opción no válida")

    else:
        print("Opción no válida")


def menuProyCreados():
    print("PROYECTOS CREADOS")
    print("Lista de proyectos creados")
    stmtPC = "select titulo from Proyecto WHERE lider = " + str(id_user)
    proyectos = connection.execute(stmtPC).fetchmany()
    for i in range(len(resultsPC)):
        print(str(i+1)+". "+resultsPC[i])
    print("0. Regresar")
    ingre1 = input("Elija un proyecto: ")
    if ingre1.isdigit(): #and int(ingre)<len(proyectos):
        while ingre1 != "0":
            tituloProyecto= resultsPC[int(ingre1-1)]
            print(tituloProyecto)
            stmtidPro = "SELEC id_proyecto FROM Proyecto where titulo = '" +tituloProyecto+ "'"
            id_pro = stmtidPro[0]
            #mostrar descripcion
            print("Menú de opciones")
            print("1. Ver participantes")
            print("2. Ver tareas")
            ingre2 = input("Elija una opción: ")
            if ingre2.isdigit():
                if ingre2 == "1":
                    stmt4= "SELECT u.nombre FROM Usuario u join Registro_inscripcion r ON u.id_user = r.colaborador WHERE r.proyecto = "+str(id_pro)
                    participantes = connection.execute(stmt4).fetchmany()
                    print("Participantes: ")
                    for i in range(len(participantes)):
                        print(str(i+1)+". "+participantes[i])
                    print("Menú de opciones")
                    print("1. Agregar participante")
                    print("2. Eliminar participante")
                    print("0. regresar")
                    ingre3 = input("Elija una opcion: ")
                    if ingre3.isdigit():
                        if ingre3 == "1":
                            asignarUsuarios()
                        elif ingre3 == "2":
                            eliminarUsuario()
                elif ingre2 == "2":
                    print("TAREAS")
                    stmttituloTareas = "SELEC titulo FROM Tarea where proyecto = '" +tituloProyecto+"'"
                    tareas = connection.execute(stmttituloTareas).fetchmany()
                    for i in range(len(tareas)):
                        print(str(i+1)+". "+ tareas[i])
                    print("0. regresar al menu principal")
                    ingre4 = input("Elija una tarea: ")
                    while ingre4 !="0":
                        if ingre4.isdigit():
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
            ingre
    else:
        print("Proyecto no existente")
