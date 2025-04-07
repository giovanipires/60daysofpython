#sudo apt-get install xvfb
#xvfb-run python3.12 automate_clicks.py
import pyautogui
import time

print("Posicione o mouse na tela e espere 5 segundos ...")
time.sleep(5)


x, y = pyautogui.position()
pyautogui.click(x, y)
print(f"Clicou na posição: {x}, {y}")

