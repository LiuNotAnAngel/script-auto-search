#python script.py


from pynput import keyboard
import pyautogui
import os
import time
import random

def on_press(key):
    toSearch = set()
    base_dir = os.path.dirname(__file__)
    palabras_path = os.path.join(base_dir, "palabras.txt")
    with open(palabras_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            toSearch.add(line)
    print(toSearch)
    try:
        if key.char == 'l':
            print("Starting...")
            while toSearch:
                time.sleep(random.uniform(1, 20))
                pyautogui.hotkey('ctrl', 'n')
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
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()