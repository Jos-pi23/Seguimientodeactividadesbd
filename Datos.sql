use SeguimientoActividades;

insert into usuario
values (
10,"Victor Garcia", "garciaromva@gmail.com","Andres1.",true,false);
insert into usuario
values (
1,"Victor Romero", "garciaromva1@gmail.com","Romero.",true,false);
insert into usuario
values (
2,"Jose Pilligua ", "josepilligua@gmail.com","Jose.",false,true);
insert into usuario
values (
3,"Joel Ocasia", "joelocasia@gmail.com","Joel.",false,true);
insert into usuario
values (
4,"Victor Menendez", "garciamenvm@gmail.com","Menendez.",true,false);
insert into usuario
values (
5,"Samuel Ocana", "samuelocana@gmail.com","Ocana1.",false,true);
insert into usuario
values (
6,"Travis Cortez", "traviscortez@gmail.com","Cortez1.",true,false);
insert into usuario
values (
7,"Cris Enrriquez", "crisenrriquez@gmail.com","Enrriquez1.",false,true);
insert into usuario
values (
8,"Said Romero", "romerosaid@gmail.com","Romero1.",false,true);
insert into usuario
values (
9,"Ben Onminitriz", "ben10@gmail.com","Omnitriz1.",false,true);

insert into lider
values(10);
insert into lider
values(6);
insert into lider
values(4);
insert into lider
values(1);
insert into colaborador
values(2);
insert into colaborador
values(3);
insert into colaborador
values(5);
insert into colaborador
values(7);
insert into colaborador
values(8);
insert into colaborador
values(9);

insert into proyecto values(
1,"programacion","2022-09-01","2022-11-30",'00:00:00','realizado',"tareas de programacion",6);
insert into proyecto values(
2,"comunicacion","2022-10-01","2022-12-31",'00:00:00','pendiente',"tareas de comunicacion",10);
insert into proyecto values(
3,"historia","2022-11-01","2023-01-01",'00:00:00','realizado',"proyecto de historia",4);
insert into proyecto values(
4,"mysql","2022-10-11","2022-11-20",'00:00:00','realizado',"proyecto de SDBDD",1);
insert into proyecto values(
5,"java","2022-09-16","2022-11-15",'00:00:00','realizado',"CODIGOS EN JAVA",6);
insert into proyecto values(
6,"myphotos","2022-5-1","2022-09-01",'00:00:00','realizado',"tareas de programacion respecto a photos",10);
insert into proyecto values(
7,"circuitos","2022-01-01","2024-03-11",'00:00:00','pendiente',"proyecto de circuito integrado con alexa",4);
insert into proyecto values(
8,"lamparas","2022-09-14","2023-10-11",'00:00:00','pendiente',"lamparas IT",1);
insert into proyecto values(
9,"proyecto de c++","2022-08-01","2022-10-29",'00:00:00','realizado',"codigo de circuitos",6);
insert into proyecto values(
10,"casa de ahorros","2022-07-01","2023-11-22",'00:00:00','pendiente',"proyecto de casa de ahorros",10);


insert into registro_inscripcion values(
6,2,1);
insert into registro_inscripcion values(
6,3,1);
insert into registro_inscripcion values(
6,5,1);
insert into registro_inscripcion values(
10,9,2);
insert into registro_inscripcion values(
10,8,2);
insert into registro_inscripcion values(
10,7,2);
insert into registro_inscripcion values(
4,2,3);
insert into registro_inscripcion values(
4,5,3);
insert into registro_inscripcion values(
4,3,3);
insert into registro_inscripcion values(
1,2,4);
insert into registro_inscripcion values(
1,5,4);
insert into registro_inscripcion values(
1,8,4);
insert into registro_inscripcion values(
6,9,5);
insert into registro_inscripcion values(
6,8,5);
insert into registro_inscripcion values(
6,7,5);
insert into registro_inscripcion values(
10,3,6);
insert into registro_inscripcion values(
10,2,6);
insert into registro_inscripcion values(
10,7,6);
insert into registro_inscripcion values(
4,2,7);
insert into registro_inscripcion values(
4,3,7);
insert into registro_inscripcion values(
4,5,7);
insert into registro_inscripcion values(
1,7,8);
insert into registro_inscripcion values(
1,8,8);
insert into registro_inscripcion values(
1,9,8);
insert into registro_inscripcion values(
6,9,9);
insert into registro_inscripcion values(
6,8,9);
insert into registro_inscripcion values(
6,7,9);
insert into registro_inscripcion values(
10,5,10);
insert into registro_inscripcion values(
10,3,10);
insert into registro_inscripcion values(
10,2,10);

insert into tarea values(
1,"HOLA MUNDO",1,2,6,"2022-09-02","00:00:00","2022-09-12","00:00:00","2022-09-13","00:00:00", "imprimir en codigo hola mundo",null,'pendiente'
);
insert into tarea values(
2,"Tema de tesis",2,9,10,"2022-10-02","00:00:00","2022-10-03","00:00:00","2022-10-13","00:00:00", "escoger el tema de la tesis",null,'realizado'
);
insert into tarea values(
3,"imperio inca",3,2,4,"2022-11-02","00:00:00","2022-11-12","00:00:00","2022-11-13","00:00:00", "investigacion del imperio inca",null,'pendiente'
);
insert into tarea values(
4,"escoger tema",4,2,1,"2022-10-12","00:00:00","2022-10-13","00:00:00","2022-10-15","00:00:00", "Seleccionar uno de los temas ",null,'realizado'
);
insert into tarea values(
5,"HOLA MUNDO java",5,9,6,"2022-11-16","00:00:00","2022-11-17","00:00:00","2022-12-01","00:00:00", "imprimir en codigo hola mundo",8,'realizado'
);
insert into tarea values(
6,"circular list",6,3,10,"2022-09-02","00:00:00","2022-09-12","00:00:00","2022-09-13","00:00:00", "crear la clases cl",10,'realizado'
);
insert into tarea values(
7,"comprar nuevos circuitos",7,5,4,"2022-01-15","00:00:00","2022-02-12","00:00:00","2022-02-13","00:00:00", "comrar 3 circuitos con tarjeta de red",10,'realizado'
);
insert into tarea values(
8,"diodos led",8,9,1,"2022-09-15","00:00:00","2022-09-17","00:00:00","2022-09-20","00:00:00", "comprar diodos led rgb",null,'pendiente'
);
insert into tarea values(
9,"HOLA MUNDO c++",9,8,6,"2022-09-02","00:00:00","2022-09-12","00:00:00","2022-09-13","00:00:00", "imprimir en codigo hola mundo en c++",10,'realizado'
);
insert into tarea values(
10,"ahorrar 10 mil",10,5,10,"2022-09-02","00:00:00","2023-09-12","00:00:00","2023-09-13","00:00:00", "cada mes reunir 1000$",null,'pendiente'
);

insert into registro_ampliacion values(
1,'pendiente',"2022-09-13","he estado enfermo",9,1,8);
insert into registro_ampliacion values(
3,'pendiente',"2022-11-13","no me llego la notificacion",2,4,3);
insert into registro_ampliacion values(
2,'aceptada',"2022-11-15","n se envio el correo",2,4,3);
insert into registro_ampliacion values(
4,'pendiente',"2022-09-14","justificacion aceptada",9,1,8);
