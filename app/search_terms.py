import os

from .paths import get_palabras_path


def palabras_txt_existe():
    return os.path.isfile(get_palabras_path())


def parsear_linea_terminos(linea_usuario):
    if not linea_usuario:
        return []
    terminos = [termino.strip() for termino in linea_usuario.split(",")]
    return [termino for termino in terminos if termino]


def guardar_busquedas_desde_linea(linea_usuario):
    """Procesa una linea CSV y sobrescribe palabras.txt.

    Devuelve la cantidad de terminos guardados.
    """
    terminos = parsear_linea_terminos(linea_usuario)
    if not terminos:
        return 0

    palabras_path = get_palabras_path()
    with open(palabras_path, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(terminos))

    return len(terminos)


def cargar_palabras():
    """Carga palabras.txt como set para mantener deduplicacion en ejecucion."""
    palabras_path = get_palabras_path()
    if not os.path.isfile(palabras_path):
        raise FileNotFoundError("No se encontró palabras.txt. Genera o ingresa terminos antes de activar.")

    palabras = set()
    with open(palabras_path, "r", encoding="utf-8") as file:
        for line in file:
            palabra = line.strip().lstrip("- ").strip()
            if palabra:
                palabras.add(palabra)

    return palabras
