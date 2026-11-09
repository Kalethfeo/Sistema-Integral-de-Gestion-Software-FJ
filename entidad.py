
"""Clase abstracta común para las entidades del sistema."""

from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError


class Entidad(ABC):
    """Clase base abstracta para las entidades de Software FJ."""

    def __init__(self, identificador: str):

        if (
            not isinstance(identificador, str)
            or not identificador.strip()
        ):
            raise DatoInvalidoError(
                "El identificador es obligatorio."
            )

        # Atributo protegido mediante encapsulación.
        self._identificador = identificador.strip()

    @property
    def identificador(self) -> str:
        """Permite consultar el identificador."""
        return self._identificador

    @abstractmethod
    def describir(self) -> str:
        """Método que deben implementar las clases hijas."""
        pass