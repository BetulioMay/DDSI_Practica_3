select * from edicion;
select * from partido;
select * from pista;
select * from arbitro;
select * from parejas;

insert into partido values (0, sysdate);
insert into partido values (12, sysdate);
insert into partido values (2222, sysdate);
insert into partido values (444, sysdate + 1);
insert into partido values (445, sysdate + 3);

insert into pista values (1, 'pista 1', 10);
insert into pista values (2, 'pista 2', 123);
insert into pista values (3, 'pista 3', 1234);
insert into pista values (4, 'pista 4', 345);
insert into pista values (5, 'pista 5', 35);

insert into arbitro values ('12312312A', 'arbitro1', 'arbitro1');

insert into parejas values ('12345678R', '87654321R', '09876543R', '56784321R');