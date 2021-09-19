![](https://camo.githubusercontent.com/86d9ca3437f5034da052cf0fd398299292aab0e4479b58c20f2fc37dd8ccbe05/68747470733a2f2f666173746170692e7469616e676f6c6f2e636f6d2f696d672f6c6f676f2d6d617267696e2f6c6f676f2d7465616c2e706e67)

# FastAPI

Práctica usando FastAPI para crear una API que realice un CRUD simple. Se utilizó una base de datos para guardar los registros de usuarios.
Para las vistas se utilizó el motor de plantillas Jinja2 para tener una interfaz que haga las solicitudes a la API.
Para probar el funcionamiento de la aplicación visita https://fastapi-users.herokuapp.com/

## Clonar Repositorio
`$ git clone https://github.com/MissaelLopez/fastapi-users.git`

## Acceder a la carpeta
`$ cd fastapi-users`

## Crear Entorno Virtual con virtualenv
`$ virtualenv env`

## Activar Entorno Virtual
`$ source env/bin/activate`

## Instalar dependencias
`$ pip install -r requirements.txt`

## Especificar credenciales de la base de datos
Acceder a `config/db.py` y cambiar las credenciales de la base de datos

## Ejecutar Aplicación
`$ uvicorn app:app`
