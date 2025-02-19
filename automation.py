import pyautogui
import time

def skip_dialogues():
    print("Iniciando automatización de diálogos...")
    try:
        while True:
            # Busca en pantalla el cuadro de diálogo usando una imagen de referencia
            dialog_location = pyautogui.locateOnScreen('resources/dialog_box.png', confidence=0.8)
            if dialog_location:
                print("Diálogo detectado. Saltando...")
                # Simula la pulsación de la tecla 'enter' (o la que corresponda)
                pyautogui.press('enter')
                time.sleep(1)  # Espera para evitar pulsaciones repetidas
            else:
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("Automatización detenida.")
