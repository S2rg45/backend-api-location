

# Prueba

Esta repositorio se crean siete enpoint para poder controlar tema de productos dentro de una empresa, se puede regisrtrar usuarios y generar login para poder tener permisos de crear productos


# Infraestructura

Se implementa una arquitectura de codigo hexagonal, implementado en POO


## Contexto del trabajo

| **Cargo**						 | **Nombre**		     |  
|--------------------------------|-----------------------|
| **Caso de Uso**  				 |                       |   
| **Servicios**                  | /api/products         |
|                                | /api/register         |
|                                | /api/login            |
|                                | /api/user/me          |
|                                |                       |
| **Arquitectura**               | Servicios             |
| **Database**                   | sqlite3               |


## Security

Se crea una capa de seguridad para que se puedan crear usuarios que solamente puedan utilizar ellos los servicios creados, la contrasena esta encriptada por "bcrypt", y se guarda de esta manera en Base de datos.

Se genera un login que genera un token con codifica "JsonWeb token", por el usuario e email, para generar la validacion al momento de querer utilizar cualquier servicio.


## URL repositorio

https://github.com/S2rg45/fin_backend_api.git