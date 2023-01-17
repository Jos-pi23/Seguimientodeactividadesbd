use seguimientoactividades;
create table Tarea_Historial(
id_tarea int primary key,
finalizacion_tarea date,
date_revision date,
calificacion int,
foreign key (id_tarea) references tarea(id_tarea)
);

DELIMITER |
create trigger historial_tarea
	after update on tarea
    for each row
    begin 
		Insert into Tarea_Historial(id_tarea,finalizacion_tarea) 
        select t.id_tarea
        from tarea t
        where t.estado='realizado' and t.id_tarea=new.id_tarea;
	end
|
DELIMITER ;

DELIMITER |
create trigger aceptar_ampliacion
	after update on registro_ampliacion
	for each row
    begin 
		update tarea set fecha_limite = date(timestampadd(day,7,now())) where id_tarea=new.tarea and new.estado = 'pendiente';
	end
|
DELIMITER ;

-- drop trigger aceptar_ampliacion;


-- ********************REPORTES***********************
create View Promedio_Notas_Tareas_realizadas
as select u.nombre, round(avg(t.calificacion),2)
	from colaborador c join tarea t on t.colaborador=c.id_colaborador join usuario u on u.id_user=c.id_colaborador
    where t.estado='realizado'
    group by t.colaborador;

-- drop view Promedio_Notas_Tareas_realizadas;
select * from Promedio_Notas_Tareas_realizadas;
select * from tarea;
create View Num_veces_Colaborador_No_Hizo_Tarea
as select u.nombre as persona, count(id_tarea) as Num_Veces_No_Hizo_Tarea
	from colaborador c join tarea t on t.colaborador=c.id_colaborador join usuario u on u.id_user=c.id_colaborador
    where t.fecha_limite>now() and estado = 'pendiente'
    group by persona;

select * from Num_veces_Colaborador_No_Hizo_Tarea;

CREATE VIEW mostrarTareas AS
SELECT t.id_tarea,t.titulo AS nomTarea,p.id_proyecto,p.titulo AS nomProyecto,t.colaborador AS id_colaborador,
u.nombre AS nomColab,t.lider AS id_lider,t.fecha_creacion,t.fecha_limite,hora_limite,t.descripcion,t.estado,t.archivo,
t.calificacion FROM Tarea t join Usuario u ON colaborador = u.id_user join Proyecto p ON t.proyecto = p.id_proyecto;

-- DROP VIEW mostrarTareas;
SELECT * FROM mostrarTareas;

-- vista usuario con ampliaciones y datos
-- drop view usuarioConAmpliacionPendiente;
CREATE VIEW usuarioConAmpliacionPendiente AS
   select u.nombre, t.titulo, ra.descripcion, t.fecha_limite as fecha_limite_tarea, ra.estado
	from ((usuario u join  colaborador c on u.id_user=c.id_colaborador) join Registro_ampliacion ra on ra.colaborador=c.id_colaborador) join Tarea t on ra.Tarea = t.id_tarea
    where ra.estado = 'pendiente'
    order by fecha_limite DESC;
-- reporte

select * from usuarioConAmpliacionPendiente;

-- ********************PROCEDURES***********************

DELIMITER |
Create procedure CreateUser_Colaborador(in u_nombre varchar(50), in u_mail varchar(50), in u_contrasenia varchar(50))
begin 
	insert into usuario (nombre,mail,contrasenia,esLider,esColaborador) values (u_nombre,u_mail, u_contrasenia,0,1);
end 
|
DELIMITER ;

CreateUser_Lider
DELIMITER |
Create procedure CreateUser_Lider(in u_nombre varchar(50), in u_mail varchar(50), in u_contrasenia varchar(50))
begin 
	insert into usuario (nombre,mail,contrasenia,esLider,esColaborador) values (u_nombre,u_mail, u_contrasenia,1,0);
end 
|
DELIMITER ;

DELIMITER //
CREATE PROCEDURE eliminar_participante(IN id_lider int, IN id_colaborador int, IN id_proyecto int)
BEGIN
DELETE FROM Tarea WHERE lider = id_lider and colaborador = id_colaborador and proyecto = id_proyecto;
DELETE FROM registro_inscripcion WHERE lider = id_lider and colaborador = id_colaborador and proyecto = id_proyecto;
END //
DELIMITER ;

-- DROP PROCEDURE eliminar_participante;
CALL eliminar_participante(1,3,13);

-- procedure para tarea
DELIMITER //
CREATE PROCEDURE update_tareaOpcion(in opcion INT, in id_tarea int ,in titulo BIT, in colaborador INT, in fecha_limite date, in hora_limite time, in hora_revision time, in descripcion varchar(100), in archivo BLOB, in calificacion int, in estado enum('pendiente', 'realizado'))
BEGIN
    IF opcion = 1 then
        UPDATE tarea t
		SET t.titulo = titulo
		WHERE t.id_tarea = id_tarea;
		-- SELECT 'Titulo de tarea actualizado exitosamente';
    ELSEIF opcion = 2 then
        UPDATE tarea t
		SET t.colaborador = colaborador
		WHERE t.id_tarea = id_tarea;
		-- SELECT 'Colaborador asignadoa la tarea actualizado exitosamente';
    ELSEIF opcion = 3 then
       UPDATE tarea t
	   SET t.fecha_limite = fecha_limite
		WHERE t.id_tarea = id_tarea;
	   -- SELECT 'Fecha Limite de la actualizada exitosamente';
    ELSEIF opcion = 4 then
       UPDATE tarea t
	   SET t.hora_limite = hora_limite
		WHERE t.id_tarea = id_tarea;
	  --  SELECT 'Hora limite de la tarea actualizada exitosamente';
    ELSEIF opcion = 5 then
       UPDATE tarea t
	   SET t.fecha_revision = fecha_revision
		WHERE t.id_tarea = id_tarea;
	   -- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 6 then
       UPDATE tarea t
	   SET t.hora_revision = hora_revision
		WHERE t.id_tarea = id_tarea;
	  --  SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 7 then
       UPDATE tarea t
	   SET t.descripcion = descripcion
		WHERE t.id_tarea = id_tarea;
	   -- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 8 then
       UPDATE tarea t
	   SET t.archivo = archivo
		WHERE t.id_tarea = id_tarea;
	   -- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 9 then
       UPDATE tarea t
	   SET t.calificacion = calificacion
		WHERE t.id_tarea = id_tarea;
	  --  SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 10 then
       UPDATE tarea t
	   SET t.estado = estado
		WHERE t.id_tarea = id_tarea;
	   -- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSE
        -- Manejar el caso de una opción no válida
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'OPCION NO VALIDA';
	END IF;
END //
DELIMITER ;
drop procedure update_usuario;
-- procedure para usuario
DELIMITER //
CREATE PROCEDURE update_usuario(in opcion INT, in id_user int ,in nombre varchar(50), in mail varchar(50),in contrasenia varchar(20), in esLider boolean, in esColaborador boolean)
BEGIN
    IF opcion = 1 then
        UPDATE usuario u
		SET u.nombre = nombre
		WHERE t.id_user = id_user;
		-- SELECT 'Nombre de usuario actualizado exitosamente';
    ELSEIF opcion = 2 then
        UPDATE usuario u
		SET u.mail = mail
		WHERE t.id_user = id_user;
		-- SELECT 'mail actualizado exitosamente';
    ELSEIF opcion = 3 then
       UPDATE usuario u
	   SET u.contrasenia = contrasenia
		WHERE t.id_user = id_user;
	   -- SELECT 'Contraseña actualizada exitosamente';
	ELSEIF opcion = 4 then
       UPDATE usuario u
	   SET u.esLider = esLider
		WHERE t.id_user = id_user;
	  --  SELECT 'Contraseña actualizada exitosamente';
	ELSEIF opcion = 5 then
       UPDATE usuario u
	   SET u.esColaborador = esColaborador
		WHERE t.id_user = id_user;
	 --   SELECT 'Contraseña actualizada exitosamente';
    ELSE
        -- Manejar el caso de una opción no válida
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'OPCION NO VALIDA';
	END IF;
END //
DELIMITER ;

-- update para proyecto
DELIMITER //
CREATE PROCEDURE update_proyecto(in opcion INT, in id_proyecto int ,in titulo varchar(20), in fecha_cierre date, in hora_cierre time, in descripcion varchar(100), in estado enum('pendiente', 'realizado'), in lider int)
BEGIN
    IF opcion = 1 then
        UPDATE proyecto p
		SET p.titulo = titulo
		WHERE p.id_proyecto = id_proyecto;
		-- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 2 then
        UPDATE proyecto p
		SET p.fecha_cierre = fecha_cierre
		WHERE p.id_proyecto = id_proyecto;
		-- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 3 then
       UPDATE proyecto p
		SET p.titulohora_cierre = titulohora_cierre
		WHERE p.id_proyecto = id_proyecto;
		-- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 4 then
       UPDATE proyecto p
		SET p.estado = estado
		WHERE p.id_proyecto = id_proyecto;
		-- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 5 then
      UPDATE proyecto p
		SET p.descripcion = descripcion
		WHERE p.id_proyecto = id_proyecto;
		-- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSEIF opcion = 6 then
       UPDATE proyecto p
		SET p.lider = lider
		WHERE p.id_proyecto = id_proyecto;
		-- SELECT 'Descripcion de tarea actualizada exitosamente';
    ELSE
        -- Manejar el caso de una opción no válida
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'OPCION NO VALIDA';
	END IF;
END //
DELIMITER ;
