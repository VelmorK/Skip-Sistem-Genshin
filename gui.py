import tkinter as tk
import threading
from automation import skip_dialogues

def start_automation():
    # Ejecutamos la automatización en un hilo separado para que la GUI no se bloquee
    thread = threading.Thread(target=skip_dialogues)
    thread.daemon = True
    thread.start()

def create_main_window():
    root = tk.Tk()
    root.title("Skip de Diálogos - Genshin Impact")
    root.geometry("400x200")

    label = tk.Label(root, text="Bienvenido al programa de Skip de Diálogos", font=("Arial", 14))
    label.pack(pady=20)

    start_button = tk.Button(root, text="Iniciar Automatización", font=("Arial", 12), command=start_automation)
    start_button.pack(pady=10)

    root.mainloop()
