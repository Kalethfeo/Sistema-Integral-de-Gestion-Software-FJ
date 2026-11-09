# Software FJ - Sistema Integral de Gestión

Proyecto académico del curso Programación (UNAD), Fase 4.

## Descripción
Aplicación de consola desarrollada en Python para gestionar clientes, servicios y reservas sin utilizar bases de datos. La información se administra mediante objetos y listas en memoria. Los eventos y errores se registran en `eventos.log`.

## Requisitos
- Python 3.10 o superior.
- Visual Studio Code (recomendado).

## Ejecución
Desde la terminal, dentro de la carpeta del proyecto:

```bash
python main.py
```

## Componentes
- `Entidad`: clase abstracta general.
- `Cliente`: registro y validación de clientes.
- `Servicio`: clase abstracta para los servicios.
- `ReservaSala`, `AlquilerEquipos`, `Asesoria`: servicios especializados.
- `Reserva`: confirmación, cancelación y procesamiento.
- `excepciones.py`: excepciones personalizadas.
- `logs.py`: registro de eventos y errores.

## Nota sobre sobrecarga
Python no implementa sobrecarga tradicional de métodos por firma como otros lenguajes. En este proyecto se demuestra un cálculo flexible mediante parámetros opcionales en `calcular_costo(duracion, impuesto, descuento)`.

## Pruebas
El archivo `main.py` ejecuta doce operaciones, tanto válidas como inválidas, y muestra que los errores se controlan sin detener la ejecución general.
