use seguimientoactividades;
-- vista usuario con ampliaciones y datos
drop view usuarioConAmpliacionPendiente;
CREATE VIEW usuarioConAmpliacionPendiente AS
   select u.nombre, t.titulo, ra.descripcion, t.fecha_limite as fecha_limite_tarea, ra.estado
	from ((usuario u join  colaborador c on u.id_user=c.id_colaborador) join Registro_ampliacion ra on ra.colaborador=c.id_colaborador) join Tarea t on ra.Tarea = t.id_tarea
    where ra.estado = 'pendiente'
    order by fecha_limite DESC;
-- reporte
SELECT *
from usuarioConAmpliacionPendiente;