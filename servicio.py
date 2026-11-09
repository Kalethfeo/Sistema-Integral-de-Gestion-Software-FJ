
"""Clase abstracta que representa los servicios de Software FJ."""

from abc import abstractmethod
from entidad import Entidad
from excepciones import (
    DatoInvalidoError,
    ServicioNoDisponibleError
)


class Servicio(Entidad):
    """Clase base abstracta para los servicios del sistema."""

    def __init__(self, codigo, nombre, tarifa_base, disponible=True):
        # Inicializar y validar primero la clase padre Entidad.
        super().__init__(codigo)

        # Validar el nombre.
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatoInvalidoError(
                "El nombre del servicio es obligatorio."
            )

        # Validar la tarifa.
        if (
            not isinstance(tarifa_base, (int, float))
            or isinstance(tarifa_base, bool)
            or tarifa_base <= 0
        ):
            raise DatoInvalidoError(
                "La tarifa base debe ser un número positivo."
            )

        # Validar disponibilidad.
        if not isinstance(disponible, bool):
            raise DatoInvalidoError(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self._codigo = self.identificador
        self._nombre = nombre.strip()
        self._tarifa_base = float(tarifa_base)
        self._disponible = disponible

    @property
    def codigo(self):
        """Permite consultar el código del servicio."""
        return self._codigo

    @property
    def nombre(self):
        """Permite consultar el nombre del servicio."""
        return self._nombre

    @property
    def tarifa_base(self):
        """Permite consultar la tarifa base."""
        return self._tarifa_base

    @property
    def disponible(self):
        """Permite consultar la disponibilidad."""
        return self._disponible

    def validar_disponibilidad(self):
        """Comprueba si el servicio está disponible."""

        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self._nombre} no está disponible."
            )

    def _calcular_total(
        self,
        duracion,
        impuesto,
        descuento,
        cargo_fijo=0,
        recargo=0
    ):
        """Realiza los cálculos comunes de los servicios."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise DatoInvalidoError(
                "La duración debe ser un número mayor que cero."
            )

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 1
        ):
            raise DatoInvalidoError(
                "El impuesto debe estar entre 0 y 1."
            )

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 1
        ):
            raise DatoInvalidoError(
                "El descuento debe estar entre 0 y 1."
            )

        if (
            not isinstance(cargo_fijo, (int, float))
            or isinstance(cargo_fijo, bool)
            or cargo_fijo < 0
        ):
            raise DatoInvalidoError(
                "El cargo fijo no puede ser negativo."
            )

        if (
            not isinstance(recargo, (int, float))
            or isinstance(recargo, bool)
            or recargo < 0
        ):
            raise DatoInvalidoError(
                "El recargo no puede ser negativo."
            )

        subtotal = self._tarifa_base * duracion
        subtotal += cargo_fijo
        subtotal += subtotal * recargo

        total = subtotal * (1 - descuento)
        total *= (1 + impuesto)

        return round(total, 2)

    @abstractmethod
    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        """Cada servicio implementa su propio cálculo."""
        pass

    @abstractmethod
    def describir(self):
        """Describe las características del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        """Valida los parámetros específicos de cada servicio."""
        pass
