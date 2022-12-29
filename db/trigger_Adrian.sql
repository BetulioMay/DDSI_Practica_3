create or replace trigger comprobarPago
before insert on paga
for each row
declare
  cursor pago_comprador is select * from paga p where :new.dni = p.dni;
  fecha timestamp;
  dif_fechas float;
begin
  select fecha_pago into fecha from paga p where p.dni = :new.dni;

  for regPago in pago_comprador loop
    dif_fechas := :new.fecha_pago - regPago.fecha_pago;
    if (dif_fechas >= 1) then
      raise_application_error(-20600, :new.dni || 'No se puede realizar otro pago');
    end if;
  end loop;
end;