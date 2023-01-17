conn = engine.connect()
parametrosUsuario = {'opcion': 0, 'id_user': 0, 'nombre': '', 'mail': '', 'contrasenia': '', 'esLider': 'False', 'esColaborador': 'False'}
parametrosUsuario[opcion] = int(input(ingrese la opcion que quiere cambiar: ))
if parametrosUsuario[opcion] = 1:
	parametrosUsuario['nombre'] = input("Ingrese ahora su nombre: ") // llenar dependiendo del caso
	stmt = text("EXEC update_usuario @opcion = :opcion, @id_user = :id_user, @nombre = :nombre, @mail = :mail, @contrasenia = :contrasenia, @esLider = :esLider, @esColaborador = :esColaborador")
	conn.execute(stmt, **params)
elif parametrosUsuario[opcion] = 2:
	parametrosUsuario['mail'] = input("Ingrese ahora su mail: ") // llenar dependiendo del caso
	stmt = text("EXEC update_usuario @opcion = :opcion, @id_user = :id_user, @nombre = :nombre, @mail = :mail, @contrasenia = :contrasenia, @esLider = :esLider, @esColaborador = :esColaborador")
	conn.execute(stmt, **params)
elif parametrosUsuario[opcion] = 3:
	parametrosUsuario['contrasenia'] = input("Ingrese ahora su contrasenia: ") // llenar dependiendo del caso
	stmt = text("EXEC update_usuario @opcion = :opcion, @id_user = :id_user, @nombre = :nombre, @mail = :mail, @contrasenia = :contrasenia, @esLider = :esLider, @esColaborador = :esColaborador")
	conn.execute(stmt, **params)
elif parametrosUsuario[opcion] = 4:
	parametrosUsuario['esLider'] = Bool(input("Ingrese ahora si quiere ser lider o no (escriba True/false): ")) // llenar dependiendo del caso
	stmt = text("EXEC update_usuario @opcion = :opcion, @id_user = :id_user, @nombre = :nombre, @mail = :mail, @contrasenia = :contrasenia, @esLider = :esLider, @esColaborador = :esColaborador")
	conn.execute(stmt, **params)
elif parametrosUsuario[opcion] = 5:
	parametrosUsuario['esColaborador'] = Bool(input("Ingrese ahora si quiere ser colaborador o no (escriba True/false): ")) // llenar dependiendo del caso
	stmt = text("EXEC update_usuario @opcion = :opcion, @id_user = :id_user, @nombre = :nombre, @mail = :mail, @contrasenia = :contrasenia, @esLider = :esLider, @esColaborador = :esColaborador")
	conn.execute(stmt, **params)
else:
  print("opcion no valida")
