# Grupo 2

Este es el repositorio del *Grupo 2*, cuyos integrantes son:

* Marcelo García - 201830013-6
* Santiago López - 201713063-6
* Daniela Stuven - 202030014-3
* Diego Tobar - 201930050-4
* **Tutor**: Cristobal Moraga
* **Profesor**: Wladimir Ormazabal
Este es el repositorio que dará continuidad al proyecto hecho en 2024 - 01 en INF236
## Wiki

Puede acceder a la Wiki mediante el siguiente [enlace](https://gitlab.com/inf236-2024-1/grupo001/-/wikis/home)

## Video Prototipo

Se puede acceder al prototipo de la vista de un Mecánico en el siguiente video: https://youtu.be/oqKZcD7FfYY

## Instalación

* Instalar y activar [Docker](https://docs.docker.com/engine/install/).
* Instalar y activar (si no viene junto a Docker) [Docker Compose](https://docs.docker.com/compose/install/)
* Instalar [Node.js](https://nodejs.org/en/download)
* Clonar este repositorio e ingresar el siguiente código en las carpetas respectivas:

En la carpeta inf23620241:

```
docker-compose build
docker-compose up
```

Y lo mismo en la carpeta inf23620241/inf236-frontend:

```
docker-compose build
docker-compose up
```

¡Listo!

Se puede abrir el localhost:7777 para ver el framework Vue.js sobre el cual se está trabajando el front-end. Actualmente, en la página se puede ver el inicio de sesión e ingresando con un usuario autorizado, ingresa a la vista que corresponda según el rol (Los usuarios con acceso se pueden encontrar en grupo001\inf23620241\inf236backend\tempDB\users.json). 


## Herramientas

Entrar en el contedor del backend (en ejecucción) por consola desde la carpeta inf23620241:

```
docker exec -it inf236_backend sh
```

Acceder a la base de datos por consola la carpeta inf23620241:

```
docker exec -it inf236_backend_mariadb mysql -p
```



## Resolución de problemas de levantamiento

Teníamos problemas para leventar los contenedores, después de haber borrado las imágenes para hacer un nuevo build desde cero.

De hecho, el build de los contenedores del backend funcionaba, pero el up mostraba los dos contenedores "mysql" y "inf23620241-backend" reiniciandose constantenemente. El "inf23620241-backend" se reiniciaba porque no podia conectar con la database "db" leventada gracias a la imagen "mysql", ya que esta no funcionaba. El log de "mysql" mostraba este error :

![LogErrorMysql](<img\LogErrorMysql29-05-2024.jpg>)


Se buscó una solución, y encontramos la propuesta de reemplazar `--default-authentication-plugin=mysql_native_password` en el archivo _docker-compose.yaml_ (que parece obsoleto; Deprecated), con `--mysql-native-password=ON` lo que sólo implica el requisito del package `cryptography` anadido en el archivo _requirements.txt_.

Todavia no sabemos porqué lo que funcionó la primera vez con el proyecto_base que no funciona ahora, ni con nuestro proyecto ni con el proyecto_base, pero esta solución parece un menor cambio que aun nos permite hacer funcionar el backend.

**Actualización 15/09:** Funciona comentando '--mysql_native_password=ON' para levantar el backend