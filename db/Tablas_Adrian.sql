create table espectador(
    dni varchar(8) not null, 
    nombre varchar(50),
    apellidos varchar(100),
    correo_electronico varchar(81),
    contrasenia varchar(30),
    PRIMARY KEY (dni)
);

create table comprador(
    dni varchar(8) not null references espectador(dni),
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