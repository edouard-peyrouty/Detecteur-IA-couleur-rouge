import threading
import requests
import time
import os

def keep_alive():
    while True:
        time.sleep(15 * 60)
        try:
            requests.get('https://detecteur-ia-couleur-rouge.onrender.com/')
        except:
            pass

def start():
    if os.environ.get('RENDER'):
        threading.Thread(target=keep_alive, daemon=True).start()