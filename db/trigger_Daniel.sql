/*
1.4 Y RS2

1.4 = Datos de salida de las parejas que un entrenador ha entrenado 

RS2: Una pareja solo puede ser formada por jugadores del mismo sexo 
*/

create or replace trigger comprobarSexo
before insert on pareja
for each row
declare
    sex1 varchar(1);
    sex2 varchar(1);
begin
    select sexo into sex1 from jugador j where :new.dni1 = j.dni_jug;
    select sexo into sex2 from jugador j where :new.dni2 = j.dni_jug;

    if (sex1 <> sex2) then
        raise_application_error(-20600, ' 2 jugadores de diferente sexo no pueden ser pareja');
    end if;
end;

insert into jugador values ('12345678W', 'Pepito', 'Grillo', 'grillo@gmail.com', 'M');
insert into jugador values ('87654321W', 'Pepita', 'Grilla', 'grilla@gmail.com', 'F');
insert into jugador values ('09876543W', 'Goku', 'Son', 'son@gmail.com', 'M');
insert into jugador values ('56784321W', 'Piedra', 'piedril', 'piedril@gmail.com', 'F');

-- Funciona bien
insert into pareja values ('12345678W', '09876543W');
-- Funciona mal
insert into pareja values ('12345678W', '87654321W');