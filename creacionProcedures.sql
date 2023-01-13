use seguimientoactividades;

-- procedure para tarea
DELIMITER //
CREATE PROCEDURE update_tareaOpcion(in opcion INT, in id int ,in titulo BIT, in colaborador INT, in fecha_limite date, in hora_limite time, in hora_revision time, in descripcion varchar(100), in archivo BLOB, in calificacion int, in estado enum('pendiente', 'realizado'))
BEGIN
    IF opcion = 1 then
        UPDATE tarea t
		SET t.titulo = titulo
		WHERE t.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 2 then
        UPDATE tarea t
		SET t.colaborador = colaborador
		WHERE t.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 3 then
       UPDATE tarea t
	   SET t.fecha_limite = fecha_limite
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 4 then
       UPDATE tarea t
	   SET t.hora_limite = hora_limite
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 5 then
       UPDATE tarea t
	   SET t.fecha_revision = fecha_revision
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 6 then
       UPDATE tarea t
	   SET t.hora_revision = hora_revision
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 7 then
       UPDATE tarea t
	   SET t.descripcion = descripcion
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 8 then
       UPDATE tarea t
	   SET t.archivo = archivo
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 9 then
       UPDATE tarea t
	   SET t.calificacion = calificacion
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 10 then
       UPDATE tarea t
	   SET t.estado = estado
	   WHERE t.id = id;
	   SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSE
        -- Manejar el caso de una opción no válida
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'OPCION NO VALIDA';
	END IF;
END //
DELIMITER ;

-- procedure para usuario
DELIMITER //
CREATE PROCEDURE update_usuario(in opcion INT, in id_user int ,in nombre varchar(50), in mail varchar(50),in contrasenia varchar(20), in esLider boolean, in esColaborador boolean)
BEGIN
    IF opcion = 1 then
        UPDATE usuario u
		SET u.nombre = nombre
		WHERE t.id = id;
		SELECT 'Nombre de usuario actualizado exitosamente';
    ELSEIF opcion = 2 then
        UPDATE usuario u
		SET u.mail = mail
		WHERE u.id = id;
		SELECT 'mail actualizado exitosamente';
    ELSEIF opcion = 3 then
       UPDATE usuario u
	   SET u.contrasenia = contrasenia
	   WHERE t.id = id;
	   SELECT 'Contraseña actualizada exitosamente';
	ELSEIF opcion = 4 then
       UPDATE usuario u
	   SET u.esLider = esLider
	   WHERE t.id = id;
	   SELECT 'Contraseña actualizada exitosamente';
	ELSEIF opcion = 5 then
       UPDATE usuario u
	   SET u.esColaborador = esColaborador
	   WHERE t.id = id;
	   SELECT 'Contraseña actualizada exitosamente';
    ELSE
        -- Manejar el caso de una opción no válida
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'OPCION NO VALIDA';
	END IF;
END //
DELIMITER ;
-- update para proyecto
DELIMITER //
CREATE PROCEDURE update_proyecto(in opcion INT, in id int ,in titulo varchar(20), in fecha_cierre date, in hora_cierre time, in descripcion varchar(100), in estado enum('pendiente', 'realizado'), in lider int)
BEGIN
    IF opcion = 1 then
        UPDATE proyecto p
		SET p.titulo = titulo
		WHERE p.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 2 then
        UPDATE proyecto p
		SET p.fecha_cierre = fecha_cierre
		WHERE p.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 3 then
       UPDATE proyecto p
		SET p.titulohora_cierre = titulohora_cierre
		WHERE p.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 4 then
       UPDATE proyecto p
		SET p.estado = estado
		WHERE p.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 5 then
      UPDATE proyecto p
		SET p.descripcion = descripcion
		WHERE p.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 6 then
       UPDATE proyecto p
		SET p.lider = lider
		WHERE p.id = id;
		SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSE
        -- Manejar el caso de una opción no válida
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'OPCION NO VALIDA';
	END IF;
END //
DELIMITER ;
-- implementacion en python