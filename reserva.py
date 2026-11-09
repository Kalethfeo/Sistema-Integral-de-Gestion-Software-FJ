
"""Clase para administrar las reservas de Software FJ."""

from datetime import datetime

from cliente import Cliente
from servicio import Servicio
from excepciones import (
    DatoInvalidoError,
    ReservaNoPermitidaError
)
from logs import registrar_evento


class Reserva:
    """Representa y administra una reserva de Software FJ."""

    def __init__(self, codigo, cliente, servicio, duracion):
        """Inicializa una reserva y valida sus datos."""

        if not isinstance(codigo, str) or not codigo.strip():
            raise DatoInvalidoError(
                "El código de la reserva es obligatorio."
            )

        if not isinstance(cliente, Cliente):
            raise DatoInvalidoError(
                "La reserva debe tener un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise DatoInvalidoError(
                "La reserva debe tener un servicio válido."
            )

        servicio.validar_disponibilidad()
        servicio.validar_parametros(duracion)

        self.__codigo = codigo.strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        self.__fecha_creacion = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    @property
    def codigo(self):
        """Permite consultar el código de la reserva."""
        return self.__codigo

    @property
    def cliente(self):
        """Permite consultar el cliente de la reserva."""
        return self.__cliente

    @property
    def servicio(self):
        """Permite consultar el servicio reservado."""
        return self.__servicio

    @property
    def duracion(self):
        """Permite consultar la duración de la reserva."""
        return self.__duracion

    @property
    def estado(self):
        """Permite consultar el estado de la reserva."""
        return self.__estado

    @property
    def fecha_creacion(self):
        """Permite consultar la fecha de creación."""
        return self.__fecha_creacion

    def confirmar(self):
        """Confirma una reserva que se encuentra pendiente."""

        if self.__estado != "Pendiente":
            raise ReservaNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"

        registrar_evento(
            f"Reserva {self.__codigo} confirmada."
        )

        return self.__estado

    def cancelar(self):
        """Cancela una reserva que aún no ha sido procesada."""

        if self.__estado == "Cancelada":
            raise ReservaNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        if self.__estado == "Procesada":
            raise ReservaNoPermitidaError(
                "No se puede cancelar una reserva procesada."
            )

        self.__estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.__codigo} cancelada."
        )

        return self.__estado

    def procesar(self):
        """Procesa una reserva confirmada y demuestra excepciones."""

        try:
            if self.__estado != "Confirmada":
                raise ReservaNoPermitidaError(
                    "La reserva debe estar confirmada para procesarse."
                )

        except ReservaNoPermitidaError as error:
            raise RuntimeError(
                "No fue posible procesar la reserva."
            ) from error

        else:
            self.__estado = "Procesada"

            registrar_evento(
                f"Reserva {self.__codigo} procesada correctamente."
            )

            return self.__estado

        finally:
            registrar_evento(
                f"Finalizó intento de procesamiento "
                f"de reserva {self.__codigo}."
            )

    def resumen(self):
        """Devuelve un resumen de la reserva y su costo."""

        costo = self.__servicio.calcular_costo(
            self.__duracion
        )

        return (
            f"{self.__codigo} | "
            f"{self.__cliente.nombre} | "
            f"{self.__servicio.nombre} | "
            f"{self.__duracion} | "
            f"${costo:.2f} | "
            f"{self.__estado}"
        )
