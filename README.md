# API de Tareas (Django + DRF)

## Instalación
- **Asegúrate de tener instalado Python 3.11 o superior. Luego instala Django y DRF con:**

-pip install django djangorestframework

- **Crear la base de datos**

-python manage.py makemigrations

-python manage.py migrate

- **Ejecutar el servidor**

-python manage.py runserver

- **Crear una tarea**

Método: POST

URL: http://127.0.0.1:8000/api/v1/tareas/

Body (JSON):

{
  "titulo": "Estudiar Django",
  "hecho": false
}

Respuesta esperada: 201 Created

## Recursos y URIs

- **/api/v1/tareas/**  
- **/api/v1/tareas/{id}/**

## Verbos y Códigos

- **GET /api/v1/tareas/** → Lista paginada de tareas.  
  - 200 OK

- **POST /api/v1/tareas/** → Crea una tarea. Body JSON: `{ "titulo": "texto", "hecho": false }`  
  - 201 Created; errores de validación: 400 Bad Request

- **GET /api/v1/tareas/{id}/** → Muestra detalle de una tarea en particular.  
  - 200 OK; si no existe: 404 Not Found

- **PATCH /api/v1/tareas/{id}/** → Actualiza parcial (`titulo` o `hecho`).  
  - 200 OK; validación: 400 Bad Request; inexistente: 404 Not Found

- **DELETE /api/v1/tareas/{id}/** → Elimina.  
  - 204 No Content; inexistente: 404 Not Found


## Reglas REST
1. **Stateless** (sin sesiones): cada petición HTTP trae lo necesario para responder y es independiente de otras peticiones.
2. **JSON**: Todas las peticiones y respuestas utilizan el formato JSON.
3. **Versionado en la ruta**: buena práctica para hacer cambios sin afectar a clientes que usan la version anterior.
4. **Idempotencia**: Ejecutar repetidamente una petición no cambia el resultado.
  - `GET` **no** cambia estado.  
  - `PATCH` repetido con el mismo body deja el **mismo estado** del recurso.  
  - `DELETE` sobre un recurso inexistente debe devolver 404 (no cambia estado).


## Diagrama de arquitectura

1. [Cliente (curl/SPA)]: Envía las peticiones a la API.
 |
2. HTTP/JSON: Capa de comunicación entre cliente y servidor.
 |
3. [ API /api/v1 (DRF ViewSets/URLs) ]: Recibe las peticiones y define las rutas.
 |
4. [ Lógica/Serializers (validación) ]: Validan los datos y los convierten a objetos o JSON.
 |
5. [ Modelo Django (ORM) ]: Conecta el código con la base de datos. Mapea la base de datos.
 |
6. [ DB SQLite (local) ]: Almacena los datos de forma permanente.
