
"""Modelo y validaciones de clientes."""

import re
from entidad import Entidad
from excepciones import DatoInvalidoError


class Cliente(Entidad):
    """Representa un cliente del sistema Software FJ."""

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        telefono: str
    ):
        """Inicializa un cliente y valida sus datos."""

        super().__init__(identificacion)

        # Validar el nombre.
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatoInvalidoError(
                "El nombre del cliente es obligatorio."
            )

        if not re.fullmatch(
            r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+",
            nombre.strip()
        ):
            raise DatoInvalidoError(
                "El nombre contiene caracteres no permitidos."
            )

        # Validar el correo electrónico.
        if not isinstance(correo, str) or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+",
            correo.strip()
        ):
            raise DatoInvalidoError(
                "El correo electrónico no tiene un formato válido."
            )

        # Validar el teléfono.
        if (
            not isinstance(telefono, str)
            or not telefono.isdigit()
            or not 7 <= len(telefono) <= 15
        ):
            raise DatoInvalidoError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        # Atributos privados para aplicar encapsulación.
        self.__nombre = nombre.strip()
        self.__correo = correo.strip().lower()
        self.__telefono = telefono

    @property
    def nombre(self):
        """Permite consultar el nombre del cliente."""
        return self.__nombre

    @property
    def correo(self):
        """Permite consultar el correo electrónico."""
        return self.__correo

    @property
    def telefono(self):
        """Permite consultar el teléfono."""
        return self.__telefono

    def describir(self) -> str:
        """Devuelve una descripción del cliente."""
        return (
            f"Cliente {self.__nombre} "
            f"(ID: {self.identificador})"
        )
