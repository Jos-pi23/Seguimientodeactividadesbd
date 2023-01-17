from sqlalchemy import create_engine, Table, MetaData, select
import pymysql
import funciones
import mysql.connector

# Crear la conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', port=3306, database='seguimientoActividades')
cursor = cnx.cursor()

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
            ingreMail = input("Ingrese su email: ")
            
            cursor = cnx.cursor()
            query1 = f'SELECT mail FROM usuario WHERE mail = "{ingreMail}"'
            cursor.execute(query1)
            results1 = cursor.fetchall()
            print(results1)
            cursor.close()

            ingrePass = input("Ingrese su contraseña: ")
            
            cursor = cnx.cursor()
            query2 = f'SELECT contrasenia FROM usuario WHERE contrasenia = "{ingrePass}"'
            cursor.execute(query2)
            results2 = cursor.fetchall()
            cursor.close()
            
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
            print("\nSeleccione su rol:")
            print("1. Lider \n2. Colaborador")
            opcion = input("Ingrese una opción: ")


            if (opcion == "1"):
                # Ejecutar el procedimiento almacenado
                cursor.callproc('CreateUser_Lider', (newNombre, newMail, newPass))

                # Confirmar los cambios
                cnx.commit()

                # Cerrar la conexión
                cursor.close()
                cnx.close()

            elif (opcion == "2"):
                # Ejecutar el procedimiento almacenado
                cursor.callproc('CreateUser_Colaborador', (newNombre, newMail, newPass))

                # Confirmar los cambios
                cnx.commit()

                # Cerrar la conexión
                cursor.close()
                cnx.close()
                print("******** Cuenta registrada ********\n")


            else:
                print("Opción no válida")
                
        elif ingreOP == "3":
            ingresa = True
            cursor.close()
            cnx.close()
            print("\n****** Salida exitosa ******\n")
            
        else:
            print("Opción no válida")


# connection.close()