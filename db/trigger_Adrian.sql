create or replace trigger comprobarFechaPartido
before insert on se_juega_en
for each row
declare
  cursor partidos_en_pista is select * from partido p natural join se_juega_en sje where :new.num_pista = sje.num_pista;
  new_fecha date;
  dif_fechas integer;
begin
  select fecha into new_fecha from partido p where p.cod_partido = :new.cod_partido;

  for regPartido in partidos_en_pista loop
    dif_fechas := 24 * abs(regPartido.fecha - new_fecha);
    if (:new.cod_partido <> regPartido.cod_partido and dif_fechas <= 3) then
      raise_application_error(-20600, :new.cod_partido || 'No se puede asignar la pista al partido');
    end if;
  end loop;
end;