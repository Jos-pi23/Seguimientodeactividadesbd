from sqlalchemy import create_engine, Table, MetaData, select
import pymysql

import datetime
import subfunciones

engine = create_engine('mysql+pymysql://root:GoriChoi14@localhost:3306/SeguimientoActividades')
connection = engine.connect()


def menuPrincipal(id_usuario):
    ingreOP = ""
    while ingreOP != "3":
        print("\n-----------VENTANA PRINCIPAL-----------")
        print("1. Crear proyectos")
        print("2. Ver proyectos")
        print("3. Cerrar sesión")
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
                
    connection.close()
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
    if confirma == "s":
        ins_pro = "insert into Proyecto (titulo,fecha_creacion,fecha_cierre,hora_cierre,estado,descripcion,lider) values \
            ('" + nomPro + "', '" + fech_crea + "', '" + fech_cie + "', '" + hora_cie + "', '"+ "pendiente"+"', '"+desc_pro+"', "+str(id_usuario)+")"
        resIns_pro = connection.execute(ins_pro)
        
        stmtidPro = "select id_proyecto from Proyecto where titulo = '" +nomPro+ "' and lider = "+str(id_usuario)
        resPro = connection.execute(stmtidPro).fetchmany(1)
        id_pro = resPro[0][0]
        
        ingrePro = ""
        while ingrePro != "3":
            print("\n-----------"+nomPro.upper()+"-----------")
            print("Menú de opciones")
            print("1. Asignar usuarios colaboradores")
            print("2. Crear tareas")
            print("3. Regresar")
            ingrePro = input("Ingrese una opción: ")
            if ingrePro.isdigit():
                if ingrePro == "1":
                    print("\n-----------ASIGNACIÓN DE USUARIOS-----------")
                    cantiUsuarios = int(input("Ingrese la cantidad de colaboradores: "))
                    usuariosAsig = subfunciones.asignarUsuarios(cantiUsuarios,id_pro,id_usuario)
                elif ingrePro == "2":
                    print("\n-----------CREACIÓN DE TAREAS-----------")
                    cantiTareas = int(input("Ingrese la cantidad de tareas: "))
                    tareasCreadas = subfunciones.crearTareas(cantiTareas,id_pro,id_usuario)
                elif ingrePro == "3":
                    print("")
                else:
                    print("Opción no válida")


def menuProyectoAsignados(id_usuario):
    print("\n-----------PROYECTOS ASIGNADOS-----------")
    print("Lista de proyectos asignados")
    stmt = "select p.titulo from Proyecto p join Tarea t on p.id_proyecto = t.proyecto where t.colaborador = "+str(id_usuario)
    proyectos = connection.execute(stmt).fetchall()
    indice = 1
    for e in proyectos:
        print(str(indice)+". "+e[0])
        indice += 1
    
    ingre = int(input("Eija un proyecto: "))
    if ingre <= len(proyectos) and ingre>0:
        proelegido = proyectos[ingre-1][0]
        print("\n-----------"+proelegido.upper()+"-----------")
        stmtidPro = "select id_proyecto from Proyecto where titulo = '" +proelegido+ "'"
        resPro = connection.execute(stmtidPro).fetchmany(1)
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
                ingre = int(input("Eija una tarea: "))
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
                stmt4= "select nomColab from mostrarTareas where id_proyecto ="+str(id_pro)+" and id_lider ="+str(id_usuario)
                participantes = connection.execute(stmt4).fetchall()
                print("\n-----------PARTICIPANTES-----------")
                for i in range(len(participantes)):
                    print(str(i+1)+". "+participantes[i][0])
                print("\nMenú de opciones")
                print("1. Agregar participante")
                print("2. Eliminar participante")
                print("0. regresar")
                ingre3 = input("Elija una opción: ")
                if ingre3.isdigit():
                    if ingre3 == "1":
                        print("\n------------AGREGACIÓN DE PARTICIPANTES------------")
                        numParti = input("Ingrese la cantidad de participantes que desea agregar: ")
                        subfunciones.asignarParticipantes(numParti,id_usuario,id_pro)
                    elif ingre3 == "2":
                        print("\n------------ELIMINACIÓN DE PARTICIPANTES------------")
                        numParti = input("Ingrese la cantidad de participantes que desea eliminar")
                        subfunciones.eliminarParticipante(numParti,id_usuario,id_pro)
            elif ingre2 == "2":
                print("\n------------TAREAS------------")
                stmtTareas = "select * from mostrarTareas where id_proyecto = " +str(id_pro)+" and id_lider = "+str(id_usuario)
                tareas = connection.execute(stmtTareas).fetchmany()
                for i in range(len(tareas)):
                    print(str(i+1)+". "+tareas[i][1])
                ingre4 = input("\nElija una tarea: ")
                print("0. Regresar ")
                while ingre4 !="0":
                    if ingre <= len(tareas):
                        if ingre4.isdigit():
                            tarElegida = tareas[ingre-1][1]
                            print("\n-----------"+tarElegida.upper()+"-----------")
                            stmtidTar = "select * from mostrarTareaa where nomTarea = '" +tarElegida+ "' and id_lider = "+str(id_usuario)
                            datosTar = connection.execute(stmtidTar).fetchmany(1)
                            id_tar = datosTar[0][0]
                            nomTar = datosTar[0][1]
                            estTar = datosTar[0][-3]
                            desTar = datosTar[0][-4]
                            fec_asig = datosTar[0][7]
                            fec_entr = datosTar[0][8]
                            hor_entr = datosTar[0][9]
                            id_Colab = datosTar[0][4]
                            nom_Colab = datosTar[0][5]
                            archivo = datosTar[0][-2]
                            hor_revis = datosTar[0][-5]
                            calificacion = datosTar[0][-1]
                            print("Nombre de la tarea: "+nomTar)
                            print("Colaborador: "+nom_Colab)
                            print("Estado de la tarea: "+estTar)
                            print("Descripción: "+desTar)
                            print("Fecha de asignación: "+fec_asig)
                            print("Fecha de entrega: "+fec_entr)
                            print("Hora de entrega: "+hor_entr)
                            print("\nMenú de opciones")
                            print("1. Revisar ampliación")
                            print("2. Revisar tarea")
                            ingre = input("Eija una opción: ")
                            if ingre.isdigit():
                                if ingre == "1":
                                    print("\n------------SOLICITUD RECIBIDA------------")
                                    conSoli = "select descripcion, fecha_limite_tarea from usuarioConAmpliacionPendiente where nombre = '" +nom_Colab+ "' and titulo = "+tarElegida+"')"
                                    solElegida = connection.execute(conSoli).fetchmany(1)
                                    print("Descripción: "+solElegida[0][0])
                                    print("Fecha limite de la tarea: "+solElegida[0][1])
                                    print("\nMenú de opciones")
                                    print("1. Aceptar solicitud")
                                    print("2. Rechazar solicitud")
                                    ingre = input("Eija una opción: ")
                                    if ingre.isdigit():
                                        if ingre == "1":
                                            stmtEli = "update registro_ampliacion set estado = 'aceptada' where colaborador = "+str(id_Colab)+" and lider = "+str(id_usuario) +")"
                                            connection.execute(stmtEli)
                                            print("Solicitud aprobada")
                                            
                                        elif ingre == "2":
                                            print("Solicitud rechazada")
                                        else:
                                            print("Opción no válida")
                                elif ingre == "2":
                                    print("\n------ Visualización de la tarea ------")
                                    print("Menú de opciones")
                                    print("1. Calificar tarea")
                                    print("2. Rechazar tarea")
                                    ingre = input("Eija una opción: ")
                                    if ingre.isdigit():
                                        if ingre == "1":
                                            nota = input("Ingrese la calificación: ")
                                            actualizarNota = f"call update_tareaOpcion({9},{id_tar},'{tarElegida}',{id_Colab},'{fec_entr}','{hor_entr}','{hor_revis}','{desTar}' \
                                                {archivo},{nota},'realizado')"
                                            connection.execute(actualizarNota)
                                        elif ingre == "2":
                                            print("Tarea rechazada")
                                            
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
