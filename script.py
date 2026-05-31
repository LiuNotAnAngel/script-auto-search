
from pynput import keyboard
import pyautogui
import os
import sys
import time
import random

def get_base_dir():
    """Devuelve el directorio donde está el ejecutable (si está empaquetado) 
    o el directorio del script (si se ejecuta como script)."""
    if getattr(sys, 'frozen', False):
        # Modo ejecutable: directorio del .exe
        return os.path.dirname(sys.executable)
    else:
        # Modo desarrollo: directorio del script actual
        return os.path.dirname(os.path.abspath(__file__))


def cargar_palabras():
    palabras = set()
    palabras_path = os.path.join(get_base_dir(), "palabras.txt")

    with open(palabras_path, "r", encoding="utf-8") as file:
        for line in file:
            palabra = line.strip().lstrip("- ").strip()
            if palabra:
                palabras.add(palabra)

    return palabras

def on_press(key):
    toSearch = cargar_palabras()
    print(toSearch)
    try:
        if key.char == 'l':
            print("Starting...")
            while toSearch:
                time.sleep(random.uniform(1, 10))
                pyautogui.hotkey('ctrl', 't')
                word = toSearch.pop()
                pyautogui.write(word)
                pyautogui.press('enter')
                print(word + " sent.")
                # simular scroll aleatorio o tab aleatorio
                simulation = random.choice([True, False])
                if not simulation:
                    scroll_simulate()
                else:
                    tab_simulate()
    except AttributeError:
        pass

def scroll_simulate():
    scroll = random.randint(1, 5)
    pyautogui.scroll(-scroll * 100)
    time.sleep(random.uniform(1, 2))
    pyautogui.scroll(scroll * random.randint(0, scroll * 100))

def tab_simulate():
    nums_tabs = random.randint(1, 5)
    for i in range(nums_tabs):
        pyautogui.press('tab')
        time.sleep(random.uniform(0.5, 1.5))
    if random.choice([True, False]):
        pyautogui.press('enter')
        time.sleep(random.uniform(1, 2))
        pyautogui.hotkey('alt', 'left') 


def start_listener():
    """Inicia el listener de teclado. Llamar desde otro módulo para arrancar."""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    start_listener()