# Grupo 1

Este es el repositorio del *Grupo 1*, cuyos integrantes son:

* Darael Badilla - 201821046-3
* Daniela Stuven - 202030014-3
* Diego Tobar - 201930050-4
* Laura Levraud - 202490033-1
* **Tutor**: Ariane Carvajal
* **Profesor**: Wladimir Ormazabal

## Wiki

Puede acceder a la Wiki mediante el siguiente [enlace](https://gitlab.com/inf236-2024-1/grupo001/-/wikis/home)

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

Se puede abrir el localhost:7777 para ver el framework Vue.js sobre el cual se trabajará la creación del front-end. Por el momento nuestro código se muestra en "Hola Mundo" abajo de la página.


## Herramientas

Entrar en el contedor del backend (en ejecucción) por consola desde la carpeta inf23620241:

```
docker exec -it inf236_backend sh
```

Acceder a la base de datos por consola la carpeta inf23620241:

```
docker exec -it inf236_backend_mariadb mysql -p
```



## Resolución de problemas de leventamiento

Teníamos problemas para leventar los contenedores, después de haber borrado las imágenes para hacer un nuevo build desde cero.

De hecho, el build de los contenedores del backend funcionaba, pero el up mostraba los dos contenedores "mysql" y "inf23620241-backend" reiniciandose constantenemente. El "inf23620241-backend" se reiniciaba porque no podia conectar con la database "db" leventada gracias a la imagen "mysql", ya que esta no funcionaba. El log de "mysql" mostraba este error :

![LogErrorMysql](<img\LogErrorMysql29-05-2024.jpg>)


Se buscó una solución, y encontramos la propuesta de reemplazar `--default-authentication-plugin=mysql_native_password` en el archivo _docker-compose.yaml_ (que parece obsoleto; Deprecated), con `--mysql-native-password=ON` lo que sólo implica el requisito del package `cryptography` anadido en el archivo _requirements.txt_.

Todavia no sabemos porqué lo que funcionó la primera vez con el proyecto_base que no funciona ahora, ni con nuestro proyecto ni con el proyecto_base, pero esta solución parece un menor cambio que aun nos permite hacer funcionar el backend.