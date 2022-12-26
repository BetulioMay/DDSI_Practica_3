-- TRIGGER RS3.1

/*
LINKS de ayuda:
Como obtener las diferencia entre fechas: https://stackoverflow.com/questions/9488475/how-can-i-get-the-difference-in-hours-between-two-dates

Error creando triggers i_plscope: https://community.oracle.com/tech/developers/discussion/2347028/reproducable-error-with-script-sys-i-plscope-sig-identifier
*/

-- Se asume que existe el partido y que se quiere insertar en la tabla
-- que relaciona el partido con la pista.
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
    -- if regPartido.fecha - :new.fecha > 3 -> ERROR
    dif_fechas := 24 * abs(regPartido.fecha - new_fecha);
    if (:new.cod_partido <> regPartido.cod_partido and dif_fechas <= 3) then
      -- Excepcion. No se puede insertar
      -- dbms_output.put_line('ERROR: Se solapan los partidos');
      raise_application_error(-20600, :new.cod_partido || 'No se puede asignar la pista al partido');
    end if;
  end loop;
end;
