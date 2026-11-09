
"""Servicio especializado para la reserva de salas."""

from servicio import Servicio
from excepciones import DatoInvalidoError


class ReservaSala(Servicio):
    """Representa el servicio de reserva de salas."""

    def describir(self):
        """Devuelve la descripción del servicio."""
        return (
            f"{self.nombre}: "
            "reserva de sala por hora."
        )

    def validar_parametros(self, duracion):
        """Valida la duración mínima de una reserva."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion < 1
        ):
            raise DatoInvalidoError(
                "La sala debe reservarse mínimo por una hora."
            )

    def calcular_costo(
        self,
        duracion=1,
        impuesto=0,
        descuento=0
    ):
        """Calcula el costo de la reserva de sala."""

        self.validar_disponibilidad()
        self.validar_parametros(duracion)

        # Cargo fijo de aseo simulado.
        return self._calcular_total(
            duracion,
            impuesto,
            descuento,
            cargo_fijo=10000
        )
