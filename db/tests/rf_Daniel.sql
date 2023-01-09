select * from jugador;

insert into edicion values (123);

insert into jugador values ('12345678R', 'Juan', 'Juan', 'juan@gmail.com', 'M');
insert into jugador values ('87654321R', 'Diego', 'Diego', 'diego@gmail.com', 'M');
insert into jugador values ('09876543R', 'Sandra', 'Sandra', 'sandra@gmail.com', 'F');
insert into jugador values ('56784321R', 'Adriana', 'Adriana', 'adriana@gmail.com', 'F');

insert into pareja values ('12345678R', '87654321R');
insert into pareja values ('09876543R', '56784321R');

insert into entrenador values ('32132132R');
insert into entrenador values ('43243243R');

insert into entrena values ('32132132R', '12345678R', '87654321R', 123);
insert into entrena values ('43243243R', '09876543R', '56784321R', 123);