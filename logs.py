"""Registro de eventos y errores en un archivo de texto."""

import logging
from pathlib import Path

RUTA_LOG = Path(__file__).with_name("eventos.log")

logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
)

def registrar_evento(mensaje: str) -> None:
    logging.info(mensaje)

def registrar_error(mensaje: str) -> None:
    logging.error(mensaje)
