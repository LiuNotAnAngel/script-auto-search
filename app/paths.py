import os
import sys


def get_base_dir():
    """Devuelve el directorio del ejecutable o del script actual."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_palabras_path():
    return os.path.join(get_base_dir(), "palabras.txt")
