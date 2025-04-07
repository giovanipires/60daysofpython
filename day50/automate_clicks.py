#sudo apt-get install xvfb
#xvfb-run python3.12 automate_clicks.py
import pyautogui
import time

print("Posicione o mouse na tela e espere 5 segundos ...")
time.sleep(5)


# x, y = pyautogui.position()
# pyautogui.click(x, y)
# print(f"Clicou na posição: {x}, {y}")

while True:
    time.sleep(5)
    x, y = 640, 512
    pyautogui.click(x, y)
    print(f"Clicou na primeira posição: {x}, {y}")

    x, y = 600, 512
    time.sleep(5)
    pyautogui.click(x, y)
    print(f"Clicou na segunda posição: {x}, {y}")