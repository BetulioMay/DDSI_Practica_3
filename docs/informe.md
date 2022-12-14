# Seminario 1. DDSI

Para este seminario donde debemos de implementar un sencillo SI, hemos decidido utilizar el lenguaje de programación Python que mantendrá una conexión con la base de datos de la escuela Oracle.

> Repositorio del proyecto en Github: https://github.com/BetulioMay/DDSI_Seminario_1.

## Tareas de instalación

- Para el funcionamiento del SI debemos de tener instalado el intérprete Python (su versión 3). Podemos descargar el instalador desde su página web: https://www.python.org/downloads/, o en su defecto también se puede encontrar en la mayoría de gestores de paquetes (p.e. `apt`, `yum`, `pacman`, `chocolatey`, ...).

- Actualizar el gestor de paquetes `pip`

```sh
python -m pip install --upgrade pip
```

- Instalar dependencias:
  - Es necesario tener un compilador de C/C++ y añadido en el _PATH_ para la compilación de las dependencias (en especial el paquete `wheel`). Por defecto viene instalado en la mayoría de distribuciones Linux. En caso de tener Windows, se puede conseguir instalando las _Build Tools_ de Visual Studio, en [este link](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022) se puede descargar el instalador en la página web de Microsoft.

```sh
pip install --upgrade -r ./requirements.txt
```

- Se necesita tener instalado el _instant client_ de Oracle.
  - Son librerías que necesita Python para poder conectarse como cliente a la base de datos.
  - Se puede instalar desde la página oficial de Oracle en [este link](https://www.oracle.com/database/technologies/instant-client/downloads.html).
    - Elegir la arquitectura del sistema operativo que este usando, descomprimir el `zip` y agregar la ubicación de las librerías al _PATH_ así como crear una variable de entorno _TNS_ADMIN_ con valor igual a la ubicación previamente dicha.

### Configurar variables de entorno

- Copiar y pegar lo que hay en `.envrc` en un nuevo archivo `.env`

```sh
cp .envrc .env
```

- Rellenar en `.env` los campos correspondientes a las credenciales de la base de datos a las que se pretende tener conexión.

>

<blockquote>
	<p>
		En su defecto, se pueden exportar las variables de entorno correspondientes a los descritos en `.envrc`, dejando `.env` vacío.
	</p>
	<p>
		NOTA: El campo DEV si vale 1, se activa un logger con información de conexión. Desactivarlo poniendo a 0 este valor.
	</p>
</blockquote>


## Ejecución

- Linux

```bash
bash run.sh
```

- Windows

```powershell
.\run.ps1
```

## Fuentes y referencias

- Documentación oficial de la librería `cx_Oracle`: https://cx-oracle.readthedocs.io/.

## Autores y contribución

- César A. Mayora Suárez: Instalación y elección de dependencias, transacción "Dar de alta pedido".
- Daniel Pérez: transacción "Mostrar tablas".
- Adrian Ladron de Guevara Alvarez: transacción "Creación y borrado de tablas".
