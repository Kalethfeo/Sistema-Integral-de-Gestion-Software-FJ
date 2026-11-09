"""Clase para administrar las reservas de Software FJ."""

from datetime import datetime

from excepciones import (
    DatoInvalidoError,
    ReservaNoPermitidaError
)
from logs import registrar_evento


class Reserva:
    """Representa y administra una reserva de Software FJ."""

    def __init__(self, codigo, cliente, servicio, duracion):

        if not isinstance(codigo, str) or not codigo.strip():
            raise DatoInvalidoError(
                "El código de la reserva es obligatorio."
            )

        if cliente is None:
            raise DatoInvalidoError(
                "La reserva debe tener un cliente asignado."
            )

        if servicio is None:
            raise DatoInvalidoError(
                "La reserva debe tener un servicio asignado."
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
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def fecha_creacion(self):
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