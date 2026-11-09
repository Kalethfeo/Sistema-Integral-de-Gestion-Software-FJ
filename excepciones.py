
"""Excepciones personalizadas del sistema Software FJ."""


class ErrorSistema(Exception):
    """Excepción principal del sistema."""
    pass


class DatoInvalidoError(ErrorSistema):
    """Error cuando los datos ingresados son incorrectos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Error cuando un servicio no está disponible."""
    pass


class ReservaNoPermitidaError(ErrorSistema):
    """Error cuando una operación sobre una reserva no está permitida."""
    pass


class RecursoNoEncontradoError(ErrorSistema):
    """Error cuando no se encuentra un recurso solicitado."""
    pass
