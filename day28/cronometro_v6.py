import time
import tkinter as tk
from tkinter import messagebox

# Variáveis globais
janela_processamento = None  # Janela de processamento

# Função do cronômetro
def iniciar_cronometro():
    global janela_processamento

    try:
        tempo = int(entrada_tempo.get())
        if tempo <= 0:
            messagebox.showerror("Erro", "O tempo deve ser maior que zero!")
            return

        # Abrir a tela de processamento
        abrir_tela_processamento()

        if opcao.get() == 1:  # Cronômetro progressivo
            for i in range(1, tempo + 1):
                label_status.config(text=f'{i} segundos decorridos!')
                if janela_processamento:
                    label_processamento.config(text=f'{i} segundos decorridos!')
                janela.update()
                time.sleep(1)
            messagebox.showinfo("Fim", "Fim do tempo!")
        elif opcao.get() == 2:  # Cronômetro regressivo
            for i in range(tempo, 0, -1):
                label_status.config(text=f'{i} segundos restantes!')
                if janela_processamento:
                    label_processamento.config(text=f'{i} segundos restantes!')
                janela.update()
                time.sleep(1)
            messagebox.showinfo("Fim", "Fim do tempo!")
        label_status.config(text="Cronômetro finalizado!")

        # Fechar a tela de processamento automaticamente
        if janela_processamento:
            janela_processamento.destroy()
            janela_processamento = None  # Resetar a variável
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido!")

# Função para abrir a tela de processamento
def abrir_tela_processamento():
    global janela_processamento
    janela_processamento = tk.Toplevel()
    janela_processamento.title("Processamento do Cronômetro")
    janela_processamento.geometry("500x180")
    janela_processamento.configure(bg="black")

    # Label para exibir o tempo na tela de processamento
    global label_processamento
    label_processamento = tk.Label(
        janela_processamento,
        text="00:00:00",
        font=("Courier New", 24),
        fg="green",
        bg="black"
    )
    label_processamento.pack(expand=True)

# Função para sair
def sair():
    janela.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cronômetro Visual")
janela.geometry("300x240")

# Variável para armazenar a opção escolhida
opcao = tk.IntVar()

# Label de boas-vindas
label_boas_vindas = tk.Label(janela, text="Bem-vindo ao Cronômetro Visual!", font=("Arial", 12))
label_boas_vindas.pack(pady=10)

# Radio buttons para escolher o tipo de cronômetro
tk.Radiobutton(janela, text="Cronômetro Progressivo", variable=opcao, value=1).pack()
tk.Radiobutton(janela, text="Cronômetro Regressivo", variable=opcao, value=2).pack()

# Entrada para o tempo
label_tempo = tk.Label(janela, text="Defina o tempo em segundos:")
label_tempo.pack(pady=5)
entrada_tempo = tk.Entry(janela)
entrada_tempo.pack()

# Botão para iniciar o cronômetro
botao_iniciar = tk.Button(janela, text="Iniciar Cronômetro", command=iniciar_cronometro)
botao_iniciar.pack(pady=10)

# Botão para sair
botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.pack(pady=5)

# Label para mostrar o status do cronômetro
label_status = tk.Label(janela, text="", font=("Arial", 10))
label_status.pack(pady=10)

# Iniciar a interface gráfica
janela.mainloop()
