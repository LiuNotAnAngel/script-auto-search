import random
import time

import pyautogui

from .config import ESPERA_MAX_SEGUNDOS, ESPERA_MIN_SEGUNDOS, TAB_MAX, TAB_MIN
from .search_terms import cargar_palabras


def _espera_detenible(stop_event, minimo, maximo):
    espera = random.uniform(minimo, maximo)
    return stop_event.wait(timeout=espera)


def scroll_simulate(stop_event=None):
    scroll = random.randint(1, 5)
    pyautogui.scroll(-scroll * 100)
    if stop_event and _espera_detenible(stop_event, 1, 2):
        return
    if not stop_event:
        time.sleep(random.uniform(1, 2))
    pyautogui.scroll(scroll * random.randint(0, scroll * 100))


def tab_simulate(stop_event=None):
    nums_tabs = random.randint(TAB_MIN, TAB_MAX)
    for _ in range(nums_tabs):
        if stop_event and stop_event.is_set():
            return
        pyautogui.press("tab")
        if stop_event and _espera_detenible(stop_event, 1, 3):
            return
        if not stop_event:
            time.sleep(random.uniform(1, 3))

    if random.choice([True, False]):
        pyautogui.press("enter")
        if stop_event and _espera_detenible(stop_event, 1, 5):
            return
        if not stop_event:
            time.sleep(random.uniform(1, 5))
        pyautogui.hotkey("alt", "left")


def ejecutar_busquedas(stop_event):
    try:
        to_search = cargar_palabras()
    except FileNotFoundError as exc:
        print(f"❌ {exc}")
        return

    if not to_search:
        print("⚠️ No hay terminos validos en palabras.txt.")
        return

    print("Starting...")
    while to_search and not stop_event.is_set():
        if _espera_detenible(stop_event, ESPERA_MIN_SEGUNDOS, ESPERA_MAX_SEGUNDOS):
            break

        pyautogui.hotkey("ctrl", "t")
        word = to_search.pop()
        pyautogui.write(word)
        pyautogui.press("enter")
        print(word + " sent.")

        if stop_event.is_set():
            break

        if random.choice([True, False]):
            tab_simulate(stop_event)
        else:
            scroll_simulate(stop_event)

    if stop_event.is_set():
        print("⏹️ Proceso detenido por tecla de finalización.")
    else:
        print("✅ Proceso completado.")
