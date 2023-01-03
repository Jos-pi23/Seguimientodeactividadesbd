from sqlalchemy import create_engine, Table, MetaData, select
import pymysql
import funciones


engine = create_engine('mysql+pymysql://root:GoriChoi14@localhost:3306/SeguimientoActividades')
connection = engine.connect()

ingresa = False
while ingresa == False:
    print("++++++++++++++++++++++++++++++")
    print("+         BIENVENIDO         +")
    print("++++++++++++++++++++++++++++++")
    print("Menu de opciones")
    print("1. Ingresar a cuenta")
    print("2. Crear cuenta")
    print("3. Salir")
    ingreOP = input("Ingrese una opción: ")
    if ingreOP.isdigit():
        if ingreOP == "1":
            print("\n-----------INICIO SESIÓN-----------")
            ingreUser = input("Ingrese su email: ")
            stmt1 = "select mail from usuario where mail = '" + str(ingreUser) + "'"
            results1 = connection.execute(stmt1).fetchmany(1)
            ingrePass = input("Ingrese su contraseña: ")
            stmt2 = "select contrasenia from usuario where mail = '" + str(ingreUser) + "'"
            results2 = connection.execute(stmt2).fetchmany(1)
            
            if (len(results1) == 1 and len(results2) == 1):
                # codigo del usuario
                stmtuser = "select id_user from Usuario where mail = '" + str(ingreUser) + "'"
                tup_id = connection.execute(stmtuser).fetchmany(1)
                id_user = tup_id[0][0]
                print("****** Ingreso completado ******")
                ingresa = True
                funciones.menuPrincipal(id_user)
            else:
                print("-----------------------------------")
                print("\n| Usted no se encuentra registrado |")
                print("|    Por favor cree una cuenta     |\n")
                print("-----------------------------------")
                
        elif ingreOP == "2":
            print("\n-----------CREACIÓN DE CUENTA-----------")
            newNombre = input("Ingrese su nombre: ")
            newMail = input("Ingrese un email: ")
            newPass = input("Ingrese una contraseña: ")
            print("\n¿Desea ser lider?")
            print("1. True \n2. False")
            opLi = input("Ingrese una opción: ")
            esLider = False
            if (opLi == "1"):
                esLider = True
            
            print("\n¿Desea ser colaborador?")
            print("1. True \n2. False")
            opCo = input("Ingrese una opción: ")
            esColaborador = False
            if (opCo == "1"):
                esColaborador = True
            stmtIns = "insert into Usuario (nombre,mail,contrasenia,esLider,esColaborador) values ('" + newNombre + "', '" + newMail + \
                                                "', '" + newPass + "'," + str(esLider) + ", "+ str(esColaborador)+")"
            resultIns = connection.execute(stmtIns)
            print("******** Cuenta registrada ********\n")
        
        elif ingreOP == "3":
            ingresa = True
            connection.close()
            print("\n****** Salida exitosa ******\n")
            
        else:
            print("Opción no válida")


# connection.close()