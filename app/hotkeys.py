import threading

from pynput import keyboard

from .automation import ejecutar_busquedas
from .config import TECLA_ACTIVACION, TECLA_FINALIZACION

EN_PROCESO = False
HILO_PROCESO = None
DETENER_EVENTO = threading.Event()


def _es_tecla(key, tecla_objetivo):
    key_char = getattr(key, "char", None)
    if not isinstance(key_char, str):
        return False
    return key_char.lower() == tecla_objetivo.lower()


def _worker_busquedas():
    global EN_PROCESO

    EN_PROCESO = True
    try:
        ejecutar_busquedas(DETENER_EVENTO)
    finally:
        EN_PROCESO = False


def on_press(key):
    global HILO_PROCESO

    if _es_tecla(key, TECLA_FINALIZACION):
        DETENER_EVENTO.set()
        print("🛑 Finalizando programa...")
        return False

    if not _es_tecla(key, TECLA_ACTIVACION):
        return

    if EN_PROCESO:
        return

    DETENER_EVENTO.clear()
    HILO_PROCESO = threading.Thread(target=_worker_busquedas, daemon=True)
    HILO_PROCESO.start()


def start_listener():
    global HILO_PROCESO

    print(
        f"Pulsa '{TECLA_ACTIVACION}' para iniciar y '{TECLA_FINALIZACION}' para finalizar."
    )
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if HILO_PROCESO and HILO_PROCESO.is_alive():
        HILO_PROCESO.join()
