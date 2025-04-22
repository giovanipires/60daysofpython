import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Configurar para usar X11 antes de importar cv2
os.environ['QT_QPA_PLATFORM'] = 'xcb'

# Carregar uma imagem (em cores)
try:
    imagem = cv2.imread('/home/giovani/Imagens/catBigode.jpg', cv2.IMREAD_COLOR)
    if imagem is None:
        print("Erro: Não foi possível carregar a imagem, verifique o caminho.")
    else:
        print("Imagem carregada com sucesso! Dimensões:", imagem.shape)
        cv2.imshow('Teste', imagem)
        cv2.waitKey(0)  # Espera até que uma tecla seja pressionada
        cv2.destroyAllWindows()
except Exception as e:
    print("Erro:", e)
    
# Não vai rodar diretamente via terminal do visual ou o run