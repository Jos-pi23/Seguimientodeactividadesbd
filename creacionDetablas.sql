create database SeguimientoActividades;
use SeguimientoActividades;
create table Lider(
  id_lider int primary key,
  foreign key (id_lider) references Usuario(id_usuario),
);
create table Colaborador(
  id_colaborador int primary key,
  foreign key (id_colaborador) references Usuario(id_usuario),
);
create table Registro_inscripcion(
  colaborador int,
  foreign key (colaborador) references Colaborador(id_colaborador),
  lider int,
  foreign key (lider) references Lider(id_lider),
);
create table Tarea(
  id_tarea int primary key,
  proyecto  int,
  foreign key (proyecto) references Proyecto(id_proyecto),
  colaborador int,
  foreign key (colaborador) references Colaborador(id_colaborador),
  lider int,
  foreign key (lider) references Lider(id_lider),
  fecha_creacion date not null,
  hora_creacion time not null,
  fecha_limite date not null,
  hora_limite time not null,
  fecha_revision date not null,
  hora_revision time not null,
  descripcion varchar(50),
  calificacion int default 0 Check(calificacion<11 and calificacion>-1),
  estado enum('pendiente', 'realizado') not null
);
