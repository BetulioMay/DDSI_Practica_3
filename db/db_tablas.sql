
/* Tablas Entidades */

create table edicion(
    cod_edicion number(3) primary key
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

create table jugador(
    dni_jug number(8) primary key
);

create table entrenador(
    dni_entr number(8) primary key
);

/* Tablas Relaciones */

create table pareja(
    dni1,
    dni2,
    primary key (dni1, dni2),
    foreign key (dni1) references jugador(dni_jug),
    foreign key (dni2) references jugador(dni_jug)
);

create table parejas(
    dni1_1,
    dni1_2,
    dni2_1,
    dni2_2,
    primary key (dni1_1,dni1_2,dni2_1,dni2_2),
    foreign key (dni1_1, dni1_2) references pareja(dni1, dni2),
    foreign key (dni2_1, dni2_2) references pareja(dni1, dni2)
);
create table participan(
    dni_1,
    dni_2,
    cod_edicion references edicion(cod_edicion),
    primary key (dni_1, dni_2, cod_edicion),
    foreign key (dni_1, dni_2) references pareja(dni1, dni2)
);

create table entrena(
    dni_entr,
    dni_1,
    dni_2,
    cod_edicion references edicion(cod_edicion),
    primary key (dni_entr, dni_1, dni_2, cod_edicion),
    foreign key (dni_1, dni_2) references pareja(dni1, dni2),
    foreign key (dni_entr) references entrenador(dni_entr)
);

create table juegan(
    cod_partido references partido(cod_partido) primary key,
    dni1_1,
    dni1_2,
    dni2_1,
    dni2_2,
    foreign key (dni1_1,dni1_2,dni2_1,dni2_2) references parejas(dni1_1,dni1_2,dni2_1,dni2_2)
);

create table hospeda(
    cod_edicion references edicion(cod_edicion),
    cod_partido references partido(cod_partido) primary key
);

create table arbitra(
    dni_arb references arbitro(dni_arb),
    cod_partido references partido(cod_partido) primary key
);

create table se_juega_en(
    num_pista references pista(num_pista),
    cod_partido references partido(cod_partido) primary key
);
