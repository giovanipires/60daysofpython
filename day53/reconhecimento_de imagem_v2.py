import cv2
import numpy as np
import matplotlib.pyplot as plt

#caminho da imagem
caminho_imagem = '/home/giovani/Imagens/catBigode.jpg'

try:
    # Carrega a imagem em modo colorido (BGR)
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_COLOR)

    if imagem is None:
        print("Erro: Não foi possível carregar a imagem. Verifique o caminho.")
    else:
        print("Imagem carregada com sucesso! Dimensões:", imagem.shape)

        # Converte de BGR (OpenCV) para RGB (matplotlib)
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

        # Exibe usando matplotlib (mais seguro para ambientes sem GUI)
        plt.imshow(imagem_rgb)
        plt.title("Visualização da Imagem")
        plt.axis('off')  # Remove eixos
        plt.show()

        # Caso esteja rodando localmente com GUI e deseje testar com OpenCV:
        # cv2.imshow('Imagem com OpenCV', imagem)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

except Exception as e:
    print("Erro ao processar a imagem:", e)