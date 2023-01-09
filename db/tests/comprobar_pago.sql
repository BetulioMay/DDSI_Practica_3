-- Disparador RS2.1
--Un espectador solo puede pagar una compra por día.Si el espectador ya había realizado una compra y la había pagado, no se le dejará pagar otra compra y se devuelve un mensaje de error�?.
insert into espectador(dni,nombre) values ('7557761','Pepe');
insert into espectador(dni,nombre) values ('577618','Paco');
insert into comprador values ('577618');
insert into comprador values ('7557761');
insert into compra values ('1235448');
insert into compra values ('321');
 
--inserta bien
insert into paga values ('1235448', to_timestamp('28/11/2002-20:04:30', 'DD/MM/YYYY-HH24:MI:SS'), '577618');
insert into paga values ('321',  to_timestamp('30/11/2002-20:04:30', 'DD/MM/YYYY-HH24:MI:SS'), '7557761');
--da error
insert into paga values ('321', to_timestamp('30/11/2002-23:04:30', 'DD/MM/YYYY-HH24:MI:SS'), '7557761');
--da error
insert into paga values ('321', to_timestamp('01/12/2002-17:04:30', 'DD/MM/YYYY-HH24:MI:SS'), '7557761');
--inserta bien
insert into paga values ('321', to_timestamp('05/12/2002-23:04:30', 'DD/MM/YYYY-HH24:MI:SS'), '7557761');
