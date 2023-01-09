insert into jugador values ('12345678W', 'Pepito', 'Grillo', 'grillo@gmail.com', 'M');
insert into jugador values ('87654321W', 'Pepita', 'Grilla', 'grilla@gmail.com', 'F');
insert into jugador values ('09876543W', 'Goku', 'Son', 'son@gmail.com', 'M');
insert into jugador values ('56784321W', 'Piedra', 'piedril', 'piedril@gmail.com', 'F');

-- Funciona bien
insert into pareja values ('12345678W', '09876543W');
-- Funciona mal
insert into pareja values ('12345678W', '87654321W');