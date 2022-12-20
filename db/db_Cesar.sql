

/* Creacion tablas */

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
create table parejas(
    dni1_1,
    dni1_2,
    dni2_1,
    dni2_2,
    primary key (dni1_1,dni1_2,dni2_1,dni2_2),
    foreign key (dni1_1, dni1_2) references pareja(dni_j1, dni_j2),
    foreign key (dni2_1, dni2_2) references pareja(dni_j1, dni_j2)
);
create table participan(
    dni_1,
    dni_2,
    cod_edicion references edicion(cod_edicion),
    primary key (dni_1, dni_2, cod_edicion),
    foreign key (dni_1, dni_2) references pareja(dni_j1, dni_j2)
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

-- TRIGGER RS3.1

/*
LINKS de ayuda:
Como obtener las diferencia entre fechas: https://stackoverflow.com/questions/9488475/how-can-i-get-the-difference-in-hours-between-two-dates
*/

create or replace trigger comprobarFechaPartido
before insert on partido
declare
  cursor partidos is select * from partidos;
  dif_fechas int;
begin
  for regPartido in partidos loop
    -- if regPartido.fecha - :new.fecha > 3 -> ERROR
    dif_fechas := 24 * (regPartido.fecha - :new.fecha);
    if dif_fechas <= 3 then
      insert into partidos values (:new.cod_partido, :new.fecha);
    end if;
  end loop;
end;


