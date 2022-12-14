
create table stock (
    Cproducto int not null primary key,
    cantidad int default 0
);


create table pedido (
    Cpedido int not null primary key,
    Ccliente int not null,
    fecha_pedido date
);

create table detalle_pedido (
    Cpedido references pedido(Cpedido),
    Cproducto references stock(Cproducto),
    cantidad int default 1,
    primary key (Cproducto, Cpedido)
);

select * from stock;
insert into stock values (1, 10);
insert into stock values (2, 23);
insert into stock values (3, 15);
insert into stock values (4, 4);

/* Drop tables */
drop table detalle_pedido;
drop table pedido;
drop table stock;