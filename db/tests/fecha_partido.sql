/* TEST TRIGGER */
-- se_juega_en(num_pista, cod_partido)

/* Insertar los partidos */
insert into partido values (0, sysdate);
insert into partido values (12, sysdate);
insert into partido values (2222, sysdate);
insert into partido values (444, sysdate + 1);
insert into partido values (445, sysdate + 3);
select * from pista;

/* insertar las pistas */
insert into pista values (1, 'pista 1', 10);
insert into pista values (2, 'pista 2', 123);
insert into pista values (3, 'pista 3', 1234);
insert into pista values (4, 'pista 4', 345);
insert into pista values (5, 'pista 5', 35);

-- select to_char(fecha, 'HH:MM:SS') from partido;
-- select * from pista;

-- Deberia funcionar
insert into se_juega_en values (1, 0);
insert into se_juega_en values (1, 444);

-- Deberia disparar el trigger
insert into se_juega_en values (1, 0);
insert into se_juega_en values (1, 12);
select * from se_juega_en;

--- Deberia funcionar
insert into se_juega_en values (3, 12);
insert into se_juega_en values (3, 445);

-- Deberia disparar
insert into se_juega_en values (3, 12);
insert into se_juega_en values (3, 2222);

drop table se_juega_en;