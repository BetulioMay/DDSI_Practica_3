/* Creacion tablas */
/*Tabla jugador*/
create table jugador(
    dni_jug number(8) primary key
);

/*Tabla Pareja*/
create table pareja(
    dni1,
    dni2,
    primary key (dni1, dni2),
    foreign key (dni1) references jugador(dni_jug),
    foreign key (dni2) references jugador(dni_jug)
);

/*Tabla Participa*/
create table participan(
    dni_1,
    dni_2,
    cod_edicion references edicion(cod_edicion),
    primary key (dni_1, dni_2, cod_edicion),
    foreign key (dni_1, dni_2) references pareja(dni1, dni2)
);

/*Tabla Edicion*/
create table edicion(
    cod_edicion number(3) primary key
);

/*Tabla Entrena*/
create table entrena(
    dni_entr,
    dni_1,
    dni_2,
    cod_edicion references edicion(cod_edicion),
    primary key (dni_entr, dni_1, dni_2, cod_edicion),
    foreign key (dni_1, dni_2) references pareja(dni1, dni2),
    foreign key (dni_entr) references entrenador(dni_entr)
);

/*Tabla entrenador*/
create table entrenador(
    dni_entr number(8) primary key
);







create table partido(
    cod_partido number(6) primary key,
    fecha date not null
);
create table pista(
    num_pista number(2) primary key,
    nombre_pista varchar(30) not null,
    capacidad number(4) not null
);
create table arbitro(
    dni_arb varchar(9) primary key,
    nombre varchar(50) not null,
    apellidos varchar(100) not null
);

