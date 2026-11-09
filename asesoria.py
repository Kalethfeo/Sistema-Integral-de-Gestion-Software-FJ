
"""Servicio especializado para asesorías."""

from servicio import Servicio
from excepciones import DatoInvalidoError


class Asesoria(Servicio):
    """Representa el servicio de asesoría especializada."""

    def describir(self):
        """Devuelve la descripción del servicio."""
        return (
            f"{self.nombre}: "
            "asesoría especializada por hora."
        )

    def validar_parametros(self, duracion):
        """Valida la duración mínima de una asesoría."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion < 0.5
        ):
            raise DatoInvalidoError(
                "La asesoría debe durar al menos media hora."
            )

    def calcular_costo(
        self,
        duracion=1,
        impuesto=0,
        descuento=0
    ):
        """Calcula el costo de la asesoría."""

        self.validar_disponibilidad()
        self.validar_parametros(duracion)

        # El costo depende de las horas contratadas.
        return self._calcular_total(
            duracion,
            impuesto,
            descuento
        )
