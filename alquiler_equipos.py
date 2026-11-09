
"""Servicio especializado para el alquiler de equipos."""

from servicio import Servicio
from excepciones import DatoInvalidoError


class AlquilerEquipos(Servicio):
    """Representa el servicio de alquiler de equipos."""

    def describir(self):
        """Devuelve la descripción del servicio."""
        return (
            f"{self.nombre}: "
            "alquiler de equipos por día."
        )

    def validar_parametros(self, duracion):
        """Valida la duración mínima del alquiler."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion < 1
        ):
            raise DatoInvalidoError(
                "El alquiler debe ser mínimo de un día."
            )

    def calcular_costo(
        self,
        duracion=1,
        impuesto=0,
        descuento=0
    ):
        """Calcula el costo del alquiler de equipos."""

        self.validar_disponibilidad()
        self.validar_parametros(duracion)

        # Recargo simulado del 5 % por seguro del equipo.
        return self._calcular_total(
            duracion,
            impuesto,
            descuento,
            recargo=0.05
        )
