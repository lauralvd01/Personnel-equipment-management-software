# Proyecto Base

- [Proyecto Base](#proyecto-base)
  - [Instalación](#instalación)
    - [Creación del proyecto:](#creación-del-proyecto)
    - [Parte con Django:](#parte-con-django)
  - [Endpoints](#endpoints)

## Instalación

* Instalar [Docker](https://docs.docker.com/engine/install/).
* Instalar [Docker Compose](https://docs.docker.com/compose/install/)
* Clonar este repositorio e ingresar el siguiente código:
```
docker-compose build
docker-compose up
```

¡Listo!

Este proyecto contiene los docker de la Base de Datos y la API. Deben añadir un tercer contenedor al archivo `docker-compose-yaml` con las configuraciones de la Vista que deseen utilizar.

A continuación se presenta una breve explicación de los pasos hechos para crearlo.

### Creación del proyecto:
* Crear el entorno virtual `python3 -m venv venv`.

Se utiliza el modulo `venv` (penúltimo argumento), que se instala en la carpeta creada `venv` (último argumento). 

* Setear entorno virtual `source venv/bin/activate`

Esto es para activar el entorno virtual, así cualquier `pip install ...` que se realice, se instalará en dicho entorno.

### Parte con Django:
Creación del modelo, en este caso se crea la entidad **Motor** con su atributo **n_serie**, el cual hace referencia a _Número de serie_. 

Luego se hace migración a la Base de Datos con los siguientes comandos:
```
python manage.py makemigrations
python manage.py migrate
```

A continuación se crea el _serializer_, esto es un componente de Django que permite transformar y manejar diferentes modelos de datos (para que Django entienda el modelo).

Luego se creó la lógica del negocio. Se utiliza la clase padre `ModelViewSet`, la cual permite heredar las acciones CRUD necesarias para el proyecto.


PD: El código está comentado en inglés, para que practiquen ;D

## Endpoints

Una vez hayan levantado los contenedores pueden utilizar [Postman](https://www.postman.com) u otra herramienta similar para probar los endpoints.
En el proyecto base se han implementado los siguientes:
```
GET: localhost:8000/motor/
POST: localhost:8000/motor/
PUT: localhost:8000/motor/{id_motor}/
DELETE: localhost:8000/motor/{id_motor}/
```
Ejemplo:
![POST request](./img/image.png)
