
# Software FJ - Sistema Integral de Gestión

Proyecto académico del curso Programación 213023 de la Universidad Nacional Abierta y a Distancia (UNAD), correspondiente a la Fase 4.

## Descripción

Aplicación de consola desarrollada en Python para gestionar clientes, servicios y reservas sin utilizar bases de datos. La información se administra mediante objetos y listas en memoria. Los eventos y errores se registran en el archivo `eventos.log`.

## Requisitos

- Python 3.10 o superior.
- Visual Studio Code (recomendado).

## Ejecución

Desde la terminal, dentro de la carpeta del proyecto, ejecutar:

```bash
py main.py
```

También se puede ejecutar mediante:

```bash
python main.py
```

## Componentes del sistema

- `entidad.py`: clase abstracta general.
- `cliente.py`: registro y validación de clientes.
- `servicio.py`: clase abstracta para los servicios.
- `reserva_sala.py`: servicio especializado en reserva de salas.
- `alquiler_equipos.py`: servicio especializado en alquiler de equipos.
- `asesoria.py`: servicio especializado en asesorías.
- `reserva.py`: administración, confirmación, cancelación y procesamiento de reservas.
- `excepciones.py`: excepciones personalizadas.
- `logs.py`: registro de eventos y errores.
- `main.py`: ejecución principal y demostración de las operaciones.
- `eventos.log`: archivo de registro de eventos y errores.

## Nota sobre la sobrecarga de métodos

Python no implementa sobrecarga tradicional de métodos por firma como otros lenguajes. En este proyecto se demuestra un cálculo flexible mediante parámetros opcionales en el método `calcular_costo(duracion, impuesto, descuento)`.

Esto permite realizar diferentes variantes de cálculo según los argumentos proporcionados.

## Pruebas

El archivo `main.py` ejecuta doce (12) operaciones, tanto válidas como inválidas, para comprobar el funcionamiento del sistema.

Las pruebas incluyen:

- Registro y validación de clientes.
- Creación de servicios especializados.
- Validación de tarifas y duraciones.
- Creación, confirmación y cancelación de reservas.
- Cálculo de costos con impuestos y descuentos.
- Manejo y control de excepciones.
- Encadenamiento de excepciones.
- Registro de eventos y errores.

Los errores controlados no detienen la ejecución general del programa.

## Registro de evidencias

Los resultados de las operaciones se muestran en la consola y los eventos y errores quedan registrados en el archivo `eventos.log`.

## Autoría

Proyecto desarrollado colaborativamente como actividad académica del curso Programación 213023 de la UNAD.
