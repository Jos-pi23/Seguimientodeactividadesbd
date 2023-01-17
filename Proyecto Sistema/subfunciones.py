from sqlalchemy import create_engine, Table, MetaData, select
import pymysql

import datetime

engine = create_engine('mysql+pymysql://root:GoriChoi14@localhost:3306/SeguimientoActividades')
connection = engine.connect()

def asignarUsuarios(cant,id_pro,id_lider):
    indice = 1
    for i in range(cant):
        correo = input("Ingrese el correo del usuario: ")
        confirma = input("¿Continuar?: (s/n) ")
        if confirma == "s":
            stmtuser = "select id_user from Usuario where mail = '" + str(correo) + "'"
            tup_id = connection.execute(stmtuser).fetchmany(1)
            id_colab = tup_id[0][0]
            ins_reg = "insert into Registro_inscripcion values ("+str(id_lider)+","+str(id_colab)+","+str(id_pro)+")"
            resIns_reg = connection.execute(ins_reg)
            print("******* Usuario "+str(indice)+" creado *******")
            indice += 1
        

def eliminarUsuario(cant):
    print("Usuario eliminado exitosamente")



def asignarTarea(inf_tarea, id_colab,id_lider,id_proy):
    ins_tarea = "insert into Tarea (titulo,proyecto,colaborador,lider,fecha_creacion,hora_creacion,fecha_limite,hora_limite, \
    fecha_revision,hora_revision,descripcion,estado) values ('" + inf_tarea[0] + "', " + str(id_proy) + ", " + str(id_colab) + ", " + str(id_lider) + \
    ", '"+ inf_tarea[1] + "', '" + inf_tarea[2] +"', '"+ inf_tarea[3] + "', '" + inf_tarea[4]+ "', '" +inf_tarea[5]+"', '"+inf_tarea[6]+"', '"+ \
    inf_tarea[7]+"', '"+"pendiente"+"')"
    resIns_tar = connection.execute(ins_tarea)
    print("\n******* Tarea creada y asignada *******\n")
        
        
def crearTareas(cant,id_proyec,id_lider):
    for i in range(cant):
        titulo = input("Ingrese el titulo de la tarea: ")
        ahora  = datetime.datetime.now()
        fech_crea = ahora.strftime('%Y-%m-%d')
        hora_crea = ahora.strftime('%H:%M:%S')
        fech_entr = input("Ingrese fecha límite de entrega con el formato (aaaa-mm-dd): ")
        hora_entr = input("Ingrese la hora límite de entrega con el formato (hh:mm:ss): ")
        fech_rev = input("Ingrese la fecha de revisión con el formato (aaaa-mm-dd): ")
        hora_rev = input("Ingrese la hora de revisión con el formato (hh:mm:ss): ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        inf_tarea = (titulo,fech_crea,hora_crea,fech_entr,hora_entr,fech_rev,hora_rev,descripcion)
        ingreso = input("¿Desea continuar? (s/n): ")
        if ingreso == "s":
            correo = input("Ingrese el correo del colaborador a asignarle la tarea: ")
            stmtuser = "select id_user from Usuario where mail = '" + str(correo) + "'"
            tup_id = connection.execute(stmtuser).fetchmany(1)
            id_colab = tup_id[0][0]
            asignarTarea(inf_tarea,id_colab,id_lider,id_proyec)
            
        else: 
            print("Datos no guardados")

def convertirABinario(archivo):
	with open(archivo, 'rb') as f:
		blob = f.read()
	return blob