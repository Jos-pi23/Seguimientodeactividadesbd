from sqlalchemy import create_engine, Table, MetaData, select
import pymysql
import mysql.connector
import datetime
import subfunciones

cnx = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', port=3306, database='seguimientoactividades')

def menuPrincipal(id_usuario):
    #cnx = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', port=3306, database='seguimientoactividades')
    ingreOP = ""
    while ingreOP != "3":
        print("\n-----------VENTANA PRINCIPAL-----------")
        print("1. Crear proyectos")
        print("2. Ver proyectos")
        print("3. Cerrar sesion")
        ingreOP = input("Ingrese una opción: ")
        if ingreOP.isdigit():
            if ingreOP == "1":
                CrearProyecto(id_usuario)
            elif ingreOP == "2":
                ingreOP1 = ""
                while not (ingreOP1 == "3"):
                    print("\n-----------VER PROYECTOS-----------")
                    print("1. Proyectos creados")
                    print("2. Proyectos asignados")
                    print("3. Retroceder")
                    ingreOP1 = input("Ingrese una opción: ")
                    if ingreOP1.isdigit():
                        if ingreOP1 == "1":
                            menuProyectosCreados(id_usuario)
                        elif ingreOP1 == "2":
                            menuProyectoAsignados(id_usuario)
                        elif ingreOP1 == "3":
                            print("")
                        else:
                            print("Opción no válida")
                
            elif ingreOP == "3":
                print("")
            else:
                print("Opción no válida")
                
    cnx.close()
    print("\n******Sesión cerrada******\n")
    

def CrearProyecto(id_usuario):
    print("\n-----------CREACIÓN DE PROYECTO-----------")
    nomPro = input("Ingrese el título del proyecto: ").capitalize()
    fech_cie = input("Ingrese la fecha de cierre que tendrá el proyecto con el formato (aaaa-mm-dd): ")
    hora_cie = input("Ingrese la hora de cierre que tendrá el proyecto con el formato (hh:mm:ss): ")
    desc_pro = input("Ingrese la descripción del proyecto: ")
    ahora  = datetime.datetime.now()
    fech_crea = ahora.strftime('%Y-%m-%d')
    confirma = input("Desea guardar los datos ingresados? (s/n): ")

    loop1 = True
    while loop1 == True:

        if confirma == "s":
            #actualizar el estado de esLider ya que creo un proyecto
            parametrosUsuario = dict(opcion=0, id_user=0, nombre='', mail='', contrasenia='', esLider='False',
                                     esColaborador='False')
            parametrosUsuario['id_user'] = id_usuario
            parametrosUsuario['opcion']=4 #opcion para actualizar el atributo esLider de la tabal usuario
            parametrosUsuario['esLider']='True'
            cursor = cnx.cursor()

            cursor.callproc('update_usuario', parametrosUsuario)
            cnx.commit()
            cursor.close()

            #crear proyecto

            cursor = cnx.cursor()
            cursor.callproc('CreateProyecto', (nomPro, fech_crea, fech_cie,hora_cie,desc_pro,'pendiente',id_usuario))
            # Confirmar los cambios
            cnx.commit()
            # Cerrar la conexión
            cursor.close()

            print("Proyecto creado exitosamente")

            cursor = cnx.cursor()
            queryID = f'SELECT id_proyecto FROM Proyecto WHERE titulo = "{nomPro}" and lider = "{id_usuario}"'
            cursor.execute(queryID)
            resultsID = cursor.fetchall()
            cursor.close()
            id_Pro = resultsID[0][0]
            avanzar = input("Quiere avanzar a añadir colaboradores y tareas o volver al menu principal ?(s/n): ")

            loop2 = True
            while loop2 == True:
                if avanzar == "s":
                    proyectoCreadoElegido(id_Pro)
                    loop2 = False
                elif avanzar == "n":
                    return
                else:
                    print("opcion no valida responde con 's' si quiere avanzar o 'n' para volver al menu")
            #stmtidPro = "select id_proyecto from Proyecto where titulo = '" +nomPro+ "' and lider = "+str(id_usuario)
            #resPro = connection.execute(stmtidPro).fetchmany(1)
            #id_pro = resPro[0][0]
            return
        elif confirma == "n":
            print("Voliendo al menu... ")
            return
        else:
            print("Opcion no valida")



def proyectoCreadoElegido(id_pro):
    ingrePro = ""
    cursor = cnx.cursor()
    queryTitulo = f'SELECT titulo, lider FROM Proyecto WHERE id_proyecto = "{id_pro}"'
    cursor.execute(queryTitulo)
    resultTitulo = cursor.fetchall()
    cursor.close()
    titulo = resultTitulo[0][0]
    id_lider = resultTitulo[0][1]
    while ingrePro != "3":
        print("\n-----------"+titulo.upper()+"-----------")
        print("Menú de opciones")
        print("1. Asignar usuarios colaboradores")
        print("2. Crear tareas")
        print("3. Regresar")
        ingrePro = input("Ingrese una opción: ")
        if ingrePro.isdigit():
            if ingrePro == "1":
                print("\n-----------ASIGNACIÓN DE USUARIOS-----------")
                cantiUsuarios = int(input("Ingrese el numero de personas que va a añadir: "))
                i =0
                while(i<cantiUsuarios):
                    newNombre = input("Ingrese el nombre del usuario que va a añadir:")
                    newMail = input("Ingrese el correo de la persona que va a añadir: ")

                    cursor = cnx.cursor()
                    queryNombre = f'SELECT id_user, nombre FROM usuario WHERE mail = "{newMail}"'
                    cursor.execute(queryNombre)
                    resultNombre = cursor.fetchall()
                    cursor.close()
                    nombre = resultNombre[0][1]
                    id_colab = resultNombre[0][0]
                    if newNombre == nombre:
                        cursor = cnx.cursor()
                        cursor.callproc('CreateRegistroInscripcion', (id_lider, id_colab, id_pro))
                        # Confirmar los cambios
                        cnx.commit()
                        # Cerrar la conexión
                        cursor.close()
                        cnx.close()
                    else:
                        print("El usuario no se encuentre en la base de datos")
            elif ingrePro == "2":
                print("\n-----------CREACIÓN DE TAREAS-----------")
                cantiTareas = int(input("Ingrese la cantidad de tareas: "))
                i = 0
                while (i < cantiTareas):
                    newTituloTarea = input("Ingrese el titulo de la tarea:")
                    mail = input("ingrese el correo del usuario a asignar la tarea:")

                    cursor = cnx.cursor()
                    queryNombre = f'SELECT id_user, nombre FROM usuario WHERE mail = "{mail}"'
                    cursor.execute(queryNombre)
                    resultNombre = cursor.fetchall()
                    cursor.close()
                    nombre = resultNombre[0][1]
                    id_colab = resultNombre[0][0]
                    if id_colab != 0:
                        ahora = datetime.datetime.now()
                        fech_crea = ahora.strftime('%Y-%m-%d')
                        hora_crea = ahora.strftime('%H:%M:%S')
                        newFechaLimites= input("Ingrese la fecha limite(dd/mm/aa): ")
                        newHoraLimite = input("Ingrese la hora limite(hh:mm)")
                        newDescription = input("Escriba una descripcion de la tarea")
                        cursor = cnx.cursor()
                        cursor.callproc('CreateTarea', (newTituloTarea, id_pro, id_colab, id_lider, ahora, newFechaLimites, newHoraLimite, newDescription))
                        # Confirmar los cambios
                        cnx.commit()
                        # Cerrar la conexión
                        cursor.close()
                        cnx.close()

                    else:
                        print("El usuario no se encuentra en la base de datos")
                        continue
            elif ingrePro == "3":
                print("")
            else:
                print("Opción no válida")
        return

def menuProyectoAsignados(id_usuario):
    print("\n-----------PROYECTOS ASIGNADOS-----------")
    print("Lista de proyectos asignados")

    cursor = cnx.cursor()
    queryNombre = f'SELECT nomTarea, nomProyecto, id_lider FROM mostrarTareas WHERE mail = "{mail}"'
    cursor.execute(queryNombre)
    indice =1
    for row in cursor:
        print(str(indice)+". "+row)
    resultNombre = cursor.fetchall()
    indice = 1
    ingre = int(input("Elija un proyecto: "))
    if ingre <= len(cursor) and ingre>0:
        proelegido = cursor[ingre-1][0]
        print("\n-----------"+proelegido.upper()+"-----------")
        cursor = cnx.cursor()
        queryid = f'SELECT id_user, nombre FROM usuario WHERE mail = "{mail}"'
        cursor.execute(queryNombre)
        resultNombre = cursor.fetchall()
        cursor.close()
        id_pro = resPro[0][0]
        print("Menú de opciones")
        print("1. Ver participantes")
        print("2. Ver tareas")
        ingre = input("Eija una opción: ")
        if ingre.isdigit():
            if ingre == "1":
                print("\n-----------PARTICIPANTES-----------")
                conPar = "select u.nombre from Usuario u join Registro_inscripcion r on u.id_user = r.colaborador where r.proyecto = "+str(id_pro)
                participantes = connection.execute(conPar).fetchall()
                indice = 1
                for p in participantes:
                    print(str(indice)+". "+p[0])
                    indice += 1
                    
            elif ingre == "2":
                print("\n------------TAREAS------------")
                stmtTar = "select titulo from Tarea where proyecto = "+str(id_pro)+" and colaborador = "+str(id_usuario)
                tareas = connection.execute(stmtTar).fetchall()
                indice = 1
                for t in tareas:
                    print(str(indice)+". "+t[0])
                    indice += 1
                ingre = int(input("Elija una tarea: "))
                if ingre <= len(tareas):
                    tarElegida = tareas[ingre-1][0]
                    print("\n-----------"+tarElegida.upper()+"-----------")
                    stmtidTar = "select * from Tarea where titulo = '" +tarElegida+ "' and colaborador = "+str(id_usuario)
                    datosTar = connection.execute(stmtidTar).fetchmany(1)
                    id_tar = datosTar[0][0]
                    nomTar = datosTar[0][1]
                    estTar = datosTar[0][13]
                    desTar = datosTar[0][11]
                    fec_asig = datosTar[0][5]
                    fec_entr = datosTar[0][7]
                    hor_entr = datosTar[0][8]
                    id_Lider = datosTar[0][4]
                    
                    print("Nombre de la tarea: "+nomTar)
                    print("Estado de la tarea: "+estTar)
                    print("Descripción: "+desTar)
                    print("Fecha de asignación: "+str(fec_asig))
                    print("Fecha límite de entrega: "+str(fec_entr))
                    print("Hora límite de entrega: "+str(hor_entr))
                    
                    print("\nMenú de opciones")
                    print("1. Pedir ampliación")
                    print("2. Hacer tarea")
                    ingre = input("Eija una opción: ")
                    if ingre.isdigit():
                        if ingre == "1":
                            print("\n------------SOLICITUD DE AMPLIACIÓN------------")
                            amplia = input("Ingrese el motivo de la solicitud de ampliación: ")
                            ahora  = datetime.datetime.now()
                            fecha = ahora.strftime('%Y/%m/%d')
                            inReAm = "insert into Registro_ampliacion (estado,fecha,descripcion,colaborador,lider,tarea) values ('" + "pendiente" + "', '" + fecha + \
                            "', '" + amplia + "'," + str(id_usuario) + ", "+ str(id_Lider)+", "+ str(id_tar)+")"
                            envioSoli = connection.execute(inReAm)
                            
                        elif ingre == "2":
                            print("\n------------HACER TAREA------------")
                            print("Menú de opciones")
                            print("1. Abrir cuadro de texto")
                            print("2. Subir archivo")
                            opIng = input("Elija una opción: ")
                            if opIng.isdigit():
                                if opIng == "1":
                                    cuadroText = input("Ingrese su respuesta: ")
                                    print("\n---------------------------------------------------------------")
                                    print(cuadroText)
                                    print("---------------------------------------------------------------")
                                elif opIng == "2":
                                    print("\n++++++++++++++++++++++++++++++")
                                    print("+        SUBIR ARCHIVO       +")
                                    archivo = input("Ingrese la ruta del archivo que va a subir: ")
                                    archivoEnBinario = subfunciones.convertirABinario(archivo)
                                    params = {'id': 5, 'completed': True}

                                    # Ejecutar el procedimiento almacenado
                                    result = connection.execute(text("EXEC update_task :id, :completed"), params)

                                    # Imprimir el número de filas afectadas
                                    print(result.rowcount)
                                    print("++++++++++++++++++++++++++++++\n")
                                    conti = input("Presione enter para continuar ")
                else:
                    print("Opción no válida")
            else:
                print("Opción no válida")

    else:
        print("Opción no válida")



def menuProyectosCreados(id_usuario):
    print("\n-----------PROYECTOS CREADOS-----------")
    print("Lista de proyectos creados")
    conProyec = "select titulo from Proyecto WHERE lider = " + str(id_usuario)
    proyectos = connection.execute(conProyec).fetchall()
    for i in range(len(proyectos)):
        print(str(i+1)+". "+proyectos[i][0])
        
    ingre1 = int(input("Elija un proyecto: "))
    if ingre1<=len(proyectos) and ingre1>0:
        proelegido = proyectos[ingre1-1][0]
        print("\n-----------"+proelegido.upper()+"-----------")
        stmtidPro = "select * from Proyecto where titulo = '" +proelegido+ "' and lider = "+str(id_usuario)
        resPro = connection.execute(stmtidPro).fetchmany(1)
        id_pro = resPro[0][0]
        fech_crea = resPro[0][2]
        fech_cier = resPro[0][3]
        hora_cier = resPro[0][4]
        estado = resPro[0][5]
        descripcion = resPro[0][6]
        #mostrar descripcion
        print("Fecha creación: "+str(fech_crea))
        print("Fecha cierre: "+str(fech_cier))
        print("Hora cierre: "+str(hora_cier))
        print("Estado del proyecto: "+estado)
        print("Descripción de proyecto: "+descripcion)
        print("\nMenú de opciones")
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
                            subfunciones.asignarUsuarios()
                        elif ingre3 == "2":
                            subfunciones.eliminarUsuario()
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
    else:
        print("Proyecto no existente")
