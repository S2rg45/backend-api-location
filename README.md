

# Prueba

En este repositorio se crean tres repositorio

# Process_location
    - En este endpoint me permite procesar todas las locations que se envian dentro de una lista, para poder saber cual es la distancia entre dos puntos que se proporciona
    
# Location_name
    - Dentro de este endpoint podemos saber en Redis cuales son los names de las locations que se han ingresado a la API

# Status_task
    -En este Enpoint me permite actualizar en la BD de MongoDB el status del task que esta procesando Celery, con respecto a los IDs_Task

# Infraestructura

Se implementa una arquitectura de codigo hexagonal, implementado en POO


# Despliegue de Infraestructura

    - se implementa workflow de github actions llamado build-api.yml
    - Se despliega infraestructura dentro de AWS con terraform


# Servicios que se despliega

    - Lambda
    - ECR


## Contexto del trabajo

## Body para hacer pruebas

    - { "locations":
        [
            {
                "name":"trisl",
                "latitude": "8.9760567978",
                "longitude": "5.700796896"
            },
            {
                "name":"illkod",
                "latitude": "1.79477769",
                "longitude": "3.47776556"
            },
            {
                "name":"iollkd",
                "latitude": "3.6566565477",
                "longitude": "-5.589098"
            }
        ]
    }

    - Con ese Body se pueden hacer pruebas con una lista de locaciones 
    


| **Cargo**						 | **Nombre**		     |  
|--------------------------------|-----------------------|
| **Caso de Uso**  				 |                       |   
| **Servicios**                  | /api/process_location |
|                                | /api/location_name    |
|                                | /api/status_task      |
|                                |                       |
|                                |                       |
| **Arquitectura**               | Servicios             |
| **Database**                   | redis, mongodb        |
| **Events**                     | Celery                |


# Tecnologias que se implementaron
    - FastApi
    - Celery
    - Redis
    - MongoDB

# Ecuacion de validacion de distancia entre dos puntos

    - haversine formula

## URL repositorio

[https://github.com/S2rg45/backend-api-location](https://github.com/S2rg45/backend-api-location.git)
