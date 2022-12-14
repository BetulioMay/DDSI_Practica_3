# Setup del proyecto

<blockquote>
	<p>Se supone que se tiene python3 ya instalado. Si no se tiene instalado, lo puede instalar en https://www.python.org/downloads.</p>
	<p>Tambien se supone que se tiene git instalado (esta instalado por defecto en distros Linux). En caso de no ser asi (caso Windows), instalarlo en https://git-scm.com/downloads</p>
</blockquote>

### Clonar repositorio

- Hacer `fork` al repositorio en la parte superior derecha (Boton _fork_).
	- Se creara un repositorio https://github.com/tu_nombre_de_usuario/DDSI_Seminario_1
	- Clonar repositorio.
	- Crear un nuevo repositorio remoto que apunte al repositorio original.
	```bash
	git remote add upstream https://github.com/BetulioMay/DDSI_Seminario_1
	```

### Instalación de dependencias

- Actualizar `pip`
```bash
python3 -m pip install --upgrade pip
```

- Instalar dependencias
```bash
pip3 install -r requirements.txt
```

#### Oracle Instant Client
Para conectarnos a la base de datos de Oracle desde Python, Python necesita un conjunto de librerias para ser cliente de la base de datos, para ello necesitamos instalarnos el _instant_client_ de Oracle. Aqui dejo un link a un video tutorial (de los muchos que hay) para tomar de guia asi como el link de descarga del _instant_client_ en la pagina web de Oracle:
- [Oracle Instant client](https://www.oracle.com/database/technologies/instant-client/downloads.html).
- [Video tutorial](https://www.youtube.com/watch?v=v0TkfVFGO5c).

### Configurar variables de entorno

- Copiar y pegar lo que hay en `.envrc` en un nuevo archivo `.env`
```powershell
cp .envrc .env
```

Rellenar en `.env` los campos correspondientes a las variables de entorno locales.

## Ejecución

- Linux
```bash
bash run.sh
```
- Windows
```powershell
.\run.ps1
```

## Contribuir al proyecto

- Actualiza tu repositorio con el repositorio _upstream_
```bash
git pull upstream master
```
- Hacer los cambios que sean oportunos: arreglar bugs, agregar una nueva funcionalidad, cumplir tareas, etc. Haciendo `commit` de tus cambios (agrega cuantos creas necesarios por el camino, no tengas miedo) con un mensaje que refleje de la mejor manera posible y breve tales cambios.
- Comprobar que los cambios se efectúen de manera correcta.
- Actualizar tus cambios con tu repositorio https://github.com/tu_nombre_de_usuario/DDSI_Seminario_1.
```bash
git push origin master
```
- Finalmente crear una _pull request_ para aportar tu contribución.

## Objetivos
Ver [ROADMAP.md](https://github.com/BetulioMay/DDSI_Seminario_1/blob/master/ROADMAP.md).

## Referencias
- [Docs cx_Oracle](https://cx-oracle.readthedocs.io/)

## Para noobs de Python
- _Naming convention_ (convención de nombres):
	- Usar siempre _snake_case_, NO _camelCase_.
- Usaremos un paradigma modular:
	- Todo son procedimientos (funciones).
	- Agrupar funciones en ficheros _.py_ (modulos).
