create database SeguimientoActividades;
use SeguimientoActividades;
create table Lider(
  id_lider int primary key,
  foreign key (id_lider) references Usuario(id_user)
);

create table Colaborador(
  id_colaborador int primary key,
  foreign key (id_colaborador) references Usuario(id_usuario)
);

CREATE TABLE Registro_inscripcion(
  lider int,
  colaborador int,
  proyecto int,
  primary key(lider,colaborador,proyecto),
  foreign key (colaborador) references Colaborador(id_colaborador),
  foreign key (lider) references Lider(id_lider),
  foreign key (proyecto) references Proyecto(id_proyecto)
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
  descripcion varchar(50) not null,
  calificacion int default 0 Check(calificacion<11 and calificacion>-1),
  estado enum('pendiente', 'realizado') not null
);

CREATE TABLE Usuario (
	id_user INT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    mail VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(20) NOT NULL,
    esLider BOOLEAN NOT NULL,
    esColaborador BOOLEAN NOT NULL,
    PRIMARY KEY(id_user)
);

CREATE TABLE Proyecto (
	id_proyecto INT AUTO_INCREMENT,
	titulo VARCHAR(50) NOT NULL,
    fecha_creacion DATE NOT NULL,
    fecha_cierre DATE NOT NULL,
    hora_cierre TIME NOT NULL,
    estado ENUM('pendiente','realizado') NOT NULL,
	descripcion  VARCHAR(200) NOT NULL,
    lider INT NOT NULL,
    PRIMARY KEY(id_proyecto),
    FOREIGN KEY(lider) REFERENCES Lider(id_lider)
);

CREATE TABLE Registro_ampliacion (
	id_resAmpliacion INT AUTO_INCREMENT,
    estado ENUM('pendiente','aceptada') NOT NULL,
    fecha DATE NOT NULL,
	descripcion  VARCHAR(100) NOT NULL,
    colaborador INT NOT NULL,
    lider INT NOT NULL,
    tarea INT NOT NULL,
    PRIMARY KEY(id_proyecto),
    FOREIGN KEY(lider) REFERENCES Lider(id_lider),
    FOREIGN KEY(tarea) REFERENCES Tarea(id_tarea)
);
