 insert into espectador(dni,nombre) values ('12345678A','Pepe');
 insert into espectador(dni,nombre) values ('57761873P','Paco');
 insert into comprador values ('57761873P');
 insert into comprador values ('12345678A');
 insert into compra values ('1235448');
 insert into compra values ('321');
 insert into compra_finalizada values ('321', '5', 'A');
 insert into compra_finalizada values ('1235448', '6', 'B');
 insert into inicia values ('321',to_timestamp('30/11/2002-17:04:30', 'DD/MM/YY-HH24:MI:SS'),'12345678A');
 insert into inicia values ('1235448',to_timestamp('30/11/2002-19:04:30', 'DD/MM/YY-HH24:MI:SS'),'57761873P');
 
 select * from compra_finalizada;
 
 select * from compra_pagada;
 select * from paga;
 
 /*delete from compra_pagada;
 delete from paga;
 commit;*/