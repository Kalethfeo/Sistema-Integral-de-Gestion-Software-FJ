
"""
Programa principal del Sistema Integral de Gestión - Software FJ.

Ejecuta automáticamente 12 operaciones de prueba para demostrar:
- Programación orientada a objetos.
- Herencia y polimorfismo.
- Encapsulación.
- Manejo de excepciones.
- Encadenamiento de excepciones.
- Registro de eventos y errores.
"""

from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipos import AlquilerEquipos
from asesoria import Asesoria
from reserva import Reserva
from excepciones import ErrorSistema
from logs import registrar_evento, registrar_error


# Listas para almacenar los objetos del sistema.
clientes = []
servicios = []
reservas = []


def ejecutar_operacion(numero, descripcion, accion):
    """Ejecuta una operación y controla los posibles errores."""

    print(f"\nOPERACIÓN {numero}: {descripcion}")

    try:
        resultado = accion()
        print("RESULTADO:", resultado)

    except ErrorSistema as error:
        print(f"ERROR CONTROLADO: {error}")

        registrar_error(
            f"Operación {numero}: "
            f"{type(error).__name__}: {error}"
        )

    except Exception as error:
        print(f"ERROR CONTROLADO: {error}")

        # Mostrar la causa original si existe.
        if error.__cause__ is not None:
            print(f"CAUSA ORIGINAL: {error.__cause__}")

        detalle = (
            f"Operación {numero}: "
            f"{type(error).__name__}: {error}"
        )

        if error.__cause__ is not None:
            detalle += (
                f" | Causa original: {error.__cause__}"
            )

        registrar_error(detalle)

    else:
        registrar_evento(
            f"Operación {numero} correcta: {descripcion}"
        )


# --------------------------------------------------
# OPERACIONES CON CLIENTES
# --------------------------------------------------

def registrar_cliente_valido():
    cliente = Cliente(
        "1001",
        "Ana Pérez",
        "ana@example.com",
        "3101234567"
    )

    clientes.append(cliente)
    return cliente.describir()


def registrar_cliente_invalido():
    cliente = Cliente(
        "1002",
        "Luis Gómez",
        "correo-no-valido",
        "3101234568"
    )

    clientes.append(cliente)
    return cliente.describir()


def registrar_segundo_cliente():
    cliente = Cliente(
        "1003",
        "Carlos Ruiz",
        "carlos@example.com",
        "3001234567"
    )

    clientes.append(cliente)
    return cliente.describir()


# --------------------------------------------------
# OPERACIONES CON SERVICIOS
# --------------------------------------------------

def crear_sala():
    servicio = ReservaSala(
        "S01",
        "Sala de reuniones",
        50000
    )

    servicios.append(servicio)
    return servicio.describir()


def crear_alquiler():
    servicio = AlquilerEquipos(
        "S02",
        "Alquiler de portátil",
        80000
    )

    servicios.append(servicio)
    return servicio.describir()


def crear_asesoria():
    servicio = Asesoria(
        "S03",
        "Asesoría técnica",
        60000
    )

    servicios.append(servicio)
    return servicio.describir()


def crear_servicio_invalido():
    servicio = ReservaSala(
        "S04",
        "Sala inválida",
        -100
    )

    servicios.append(servicio)
    return servicio.describir()


# --------------------------------------------------
# OPERACIONES CON RESERVAS
# --------------------------------------------------

def crear_reserva_correcta():
    reserva = Reserva(
        "R001",
        clientes[0],
        servicios[0],
        2
    )

    reservas.append(reserva)
    reserva.confirmar()

    return reserva.resumen()


def crear_reserva_incorrecta():
    return Reserva(
        "R002",
        clientes[0],
        servicios[0],
        0
    ).resumen()


def cancelar_reserva():
    return reservas[0].cancelar()


# --------------------------------------------------
# CÁLCULO DE COSTOS
# --------------------------------------------------

def demostrar_calculo_flexible():
    # Impuesto del 19 % y descuento del 10 %.
    costo = servicios[0].calcular_costo(
        2,
        0.19,
        0.10
    )

    return f"Costo final: ${costo:,.2f}"


# --------------------------------------------------
# PRUEBA DE ENCADENAMIENTO DE EXCEPCIONES
# --------------------------------------------------

def probar_encadenamiento():
    reserva = Reserva(
        "R003",
        clientes[1],
        servicios[2],
        1
    )

    return reserva.procesar()


# --------------------------------------------------
# FUNCIÓN PRINCIPAL
# --------------------------------------------------

def main():

    print("=" * 62)
    print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 62)

    # Demostración de try, except, else y finally.
    try:
        print("Iniciando pruebas del sistema...")

    except Exception as error:
        registrar_error(
            f"Error durante el inicio: {error}"
        )

    else:
        registrar_evento(
            "Inicio de pruebas del sistema."
        )

    finally:
        print("Preparación de pruebas finalizada.")

    # Datos y operaciones de prueba automáticas.
    operaciones = [

        (
            "Registrar un cliente válido",
            registrar_cliente_valido
        ),

        (
            "Intentar registrar cliente con correo inválido",
            registrar_cliente_invalido
        ),

        (
            "Registrar un segundo cliente válido",
            registrar_segundo_cliente
        ),

        (
            "Crear servicio de reserva de salas",
            crear_sala
        ),

        (
            "Crear servicio de alquiler de equipos",
            crear_alquiler
        ),

        (
            "Crear servicio de asesoría especializada",
            crear_asesoria
        ),

        (
            "Intentar crear servicio con tarifa negativa",
            crear_servicio_invalido
        ),

        (
            "Crear y confirmar una reserva válida",
            crear_reserva_correcta
        ),

        (
            "Intentar crear reserva con duración inválida",
            crear_reserva_incorrecta
        ),

        (
            "Cancelar una reserva",
            cancelar_reserva
        ),

        (
            "Demostrar cálculo con impuesto y descuento",
            demostrar_calculo_flexible
        ),

        (
            "Intentar procesar una reserva sin confirmar",
            probar_encadenamiento
        )
    ]

    # Ejecución automática de las 12 operaciones.
    for numero, (descripcion, accion) in enumerate(
        operaciones,
        start=1
    ):

        ejecutar_operacion(
            numero,
            descripcion,
            accion
        )

    # Resumen final del sistema.
    print("\n" + "=" * 62)
    print("RESUMEN FINAL")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas creadas correctamente: {len(reservas)}")

    print("Los eventos y errores se guardaron en eventos.log")

    print("=" * 62)


# Punto de entrada del programa.
if __name__ == "__main__":
    main()
