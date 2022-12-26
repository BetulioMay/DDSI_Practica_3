
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

Error creando triggers i_plscope: https://community.oracle.com/tech/developers/discussion/2347028/reproducable-error-with-script-sys-i-plscope-sig-identifier
*/

/*
Nuevo partido: ...num_pista, fecha

for todos los partidos que se juegan en pista ->
    select p.cod_partido from partido p natural join se_juega_en sje
    where :new.cod_partido <> p.cod_partido and 
*/

-- Se asume que existe el partido y que se quiere insertar en la tabla
-- que relaciona el partido con la pista.
/*create or replace trigger comprobarFechaPartido
before insert on se_juega_en                -- insert into se_juega_en values (cod_partido, num_pista)
for each row
declare
  cursor partidos_en_pista is select * from partido p natural join se_juega_en sje
  where :new.num_pista = sje.num_pista;     -- (cod_partido, fecha, num_pista)
  new_fecha DATE;
  dif_fechas int;
begin
  -- Obtenemos la fecha del partido en cuestion
  select fecha into new_fecha from partido p where p.cod_partido = :new.cod_partido;

  for regPartido in partidos_en_pista loop
    -- if regPartido.fecha - :new.fecha > 3 -> ERROR
    dif_fechas := 24 * (regPartido.fecha - new_fecha);
    if dif_fechas <= 3 then
      -- Excepcion. No se puede insertar
      -- dbms_output.put_line('ERROR: Se solapan los partidos');
      raise_application_error(-20600, :new.cod_partido || ' no se puede asignar la pista al partido');
    end if;
  end loop;
end;
*/
/* Partidos */
insert into partido values (0, sysdate);
insert into partido values (12, sysdate);
insert into partido values (2222, sysdate);
insert into partido values (444, sysdate + 1);
select * from partido;

/* Pistas */
insert into pista values (1, 'pista 1', 10);
insert into pista values (2, 'pista 2', 123);
insert into pista values (3, 'pista 3', 1234);
insert into pista values (4, 'pista 4', 345);
insert into pista values (5, 'pista 5', 35);

select to_char(fecha, 'HH:MM:SS') from partido;
select * from pista;

/* TEST TRIGGER */
-- se_juega_en(num_pista, cod_partido)

-- Deberia funcionar
insert into se_juega_en values (1, 0);
insert into se_juega_en values (1, 444);

-- Deberia disparar el trigger
insert into se_juega_en values (1, 0);
insert into se_juega_en values (1, 12);
select * from se_juega_en;

--- Deberia funcionar
insert into se_juega_en values (3, 12);
insert into se_juega_en values (3, 444);

-- Deberia disparar
insert into se_juega_en values (3, 12);
insert into se_juega_en values (3, 13);

insert into partido values (13, sysdate + 2);

drop table se_juega_en;
