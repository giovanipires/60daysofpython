import sys
import random
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)

class JogoAdivinhacao(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configurações da janela
        self.setWindowTitle("Jogo de Adivinhação")
        self.setGeometry(100, 100, 300, 200)

        # Layout vertical
        layout = QVBoxLayout()

        # Mensagem de boas-vindas
        self.mensagem = QLabel("Bem-vindo ao jogo de adivinhação!\nTente adivinhar o número entre 0 e 10.")
        layout.addWidget(self.mensagem)

        # Campo de entrada para o palpite
        self.entrada = QLineEdit(self)
        self.entrada.setPlaceholderText("Digite seu palpite (0 a 10)")
        layout.addWidget(self.entrada)

        # Botão para enviar o palpite
        self.botao = QPushButton("Enviar Palpite", self)
        self.botao.clicked.connect(self.verificar_palpite)
        layout.addWidget(self.botao)

        # Exibir tentativas restantes
        self.tentativas_restantes = 3
        self.label_tentativas = QLabel(f"Tentativas restantes: {self.tentativas_restantes}")
        layout.addWidget(self.label_tentativas)

        # Definir o layout na janela
        self.setLayout(layout)

        # Gerar número secreto
        self.numero_secreto = random.randint(0, 10)

    def verificar_palpite(self):
        try:
            palpite = int(self.entrada.text())

            if palpite < 0 or palpite > 10:
                QMessageBox.warning(self, "Entrada inválida", "Por favor, digite um número entre 0 e 10.")
                return

            self.tentativas_restantes -= 1
            self.label_tentativas.setText(f"Tentativas restantes: {self.tentativas_restantes}")

            if palpite < self.numero_secreto:
                QMessageBox.information(self, "Resultado", "O número secreto é maior.")
            elif palpite > self.numero_secreto:
                QMessageBox.information(self, "Resultado", "O número secreto é menor.")
            else:
                QMessageBox.information(self, "Parabéns!", f"Você acertou! O número era {self.numero_secreto}.")
                self.resetar_jogo()
                return

            if self.tentativas_restantes == 0:
                QMessageBox.information(self, "Fim de jogo", f"Suas tentativas acabaram! O número secreto era {self.numero_secreto}.")
                self.resetar_jogo()

        except ValueError:
            QMessageBox.warning(self, "Entrada inválida", "Por favor, digite um número válido.")

    def resetar_jogo(self):
        """Reinicia o jogo com um novo número secreto e 3 tentativas."""
        self.numero_secreto = random.randint(0, 10)
        self.tentativas_restantes = 3
        self.label_tentativas.setText(f"Tentativas restantes: {self.tentativas_restantes}")
        self.entrada.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jogo = JogoAdivinhacao()
    jogo.show()
    sys.exit(app.exec_())
