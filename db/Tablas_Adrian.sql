create table espectador(
    dni varchar(9) not null, 
    nombre varchar(50),
    apellidos varchar(100),
    correo_electronico varchar(81),
    contrasenia varchar(30),
    PRIMARY KEY (dni)
);

create table comprador(
    dni varchar(9) not null references espectador(dni),
    primary key (dni)
);

create table compra(
    cod_compra varchar(14) not null,
    primary key (cod_compra)
);

create table compra_finalizada(
    cod_compra references compra(cod_compra),
    n_entradas number(2,0) not null,
    tipo_entrada varchar(2),
    primary key (cod_compra)
);

create table compra_pagada(
    cod_compra references compra_finalizada(cod_compra),
    precio number(6,2) not null,
    primary key (cod_compra)
);

create table inicia(
    cod_compra references compra(cod_compra),
    fecha_compra timestamp,
    dni references espectador(dni) not null,
    primary key (cod_compra,fecha_compra)
);

create table entrega(
    cod_compra references compra(cod_compra),
    dni references comprador(dni),
    primary key (cod_compra)
);

create table paga(
    cod_compra references compra(cod_compra) not null,
    fecha_pago timestamp,
    dni references comprador(dni),
    primary key (fecha_pago,dni)
);

create table devuelve(
    cod_compra references compra_pagada(cod_compra) not null,
    dni references comprador(dni),
    primary key (dni)
);

create table hecha(
    cod_compra references compra(cod_compra),
    cod_edicion references edicion(cod_edicion) not null,
    primary key (cod_compra)
);

-- Disparador RS2.1
--Un espectador solo puede pagar una compra por día.Si el espectador ya había realizado una compra y la había pagado, no se le dejará pagar otra compra y se devuelve un mensaje de error”.
 insert into espectador(dni,nombre) values ('12345678A','Pepe');
 insert into espectador(dni,nombre) values ('57761873P','Paco');
 insert into comprador values ('57761873P');
 insert into comprador values ('12345678A');
 insert into compra values ('1235448');
 insert into compra values ('321');
 insert into inicia values ('321','30/11/2002-17:04:30','12345678A');
 insert into inicia values ('1235448','30/11/2002-19:04:30','57761873P');

 --inserta bien
 insert into paga values ('1235448', '28/11/2002-20:04:30', '57761873P');
 insert into paga values ('321', '30/11/2002-20:04:30', '12345678A');
 --da error
 insert into paga values ('321', '30/11/2002-23:04:30', '12345678A');
 --da error
 insert into paga values ('321', '31/11/2002-17:04:30', '12345678A');
 --inserta bien
 insert into paga values ('321', '5/12/2002-23:04:30', '12345678A');