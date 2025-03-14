import time
import tkinter as tk
from tkinter import messagebox

# Variáveis globais
pausado = False
tempo_restante = 0

# Função para iniciar o cronômetro
def iniciar_cronometro():
    global pausado, tempo_restante

    if pausado:
        pausado = False
        botao_pausar.config(text="Pausar")
        atualizar_cronometro()
        return

    try:
        horas = int(entrada_horas.get())
        minutos = int(entrada_minutos.get())
        segundos = int(entrada_segundos.get())

        if horas < 0 or minutos < 0 or segundos < 0:
            messagebox.showerror("Erro", "Os valores não podem ser negativos!")
            return

        tempo_total = horas * 3600 + minutos * 60 + segundos
        if tempo_total <= 0:
            messagebox.showerror("Erro", "O tempo deve ser maior que zero!")
            return

        tempo_restante = tempo_total
        botao_iniciar.config(state=tk.DISABLED)
        botao_pausar.config(state=tk.NORMAL)
        botao_zerar.config(state=tk.NORMAL)
        pausado = False
        atualizar_cronometro()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")

# Função para pausar/continuar o cronômetro
def pausar_cronometro():
    global pausado
    pausado = not pausado
    if pausado:
        botao_pausar.config(text="Continuar")
    else:
        botao_pausar.config(text="Pausar")
        atualizar_cronometro()

# Função para zerar o cronômetro
def zerar_cronometro():
    global pausado, tempo_restante
    pausado = True
    tempo_restante = 0
    label_tempo.config(text="00:00:00")
    botao_iniciar.config(state=tk.NORMAL)
    botao_pausar.config(state=tk.DISABLED)
    botao_zerar.config(state=tk.DISABLED)

# Função para atualizar o cronômetro
def atualizar_cronometro():
    global tempo_restante, pausado

    if tempo_restante <= 0:
        label_tempo.config(text="00:00:00")
        messagebox.showinfo("Fim", "Fim do tempo!")
        botao_iniciar.config(state=tk.NORMAL)
        botao_pausar.config(state=tk.DISABLED)
        botao_zerar.config(state=tk.DISABLED)
        return

    if not pausado:
        horas = tempo_restante // 3600
        minutos = (tempo_restante % 3600) // 60
        segundos = tempo_restante % 60
        label_tempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        tempo_restante -= 1
        janela.after(1000, atualizar_cronometro)

# Função para sair
def sair():
    janela.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cronômetro Visual")
janela.geometry("400x300")

# Label de boas-vindas
label_boas_vindas = tk.Label(janela, text="Bem-vindo ao Cronômetro Visual!", font=("Arial", 14))
label_boas_vindas.pack(pady=10)

# Frame para entrada de horas, minutos e segundos
frame_tempo = tk.Frame(janela)
frame_tempo.pack(pady=10)

tk.Label(frame_tempo, text="Horas:").grid(row=0, column=0, padx=5)
entrada_horas = tk.Entry(frame_tempo, width=5)
entrada_horas.grid(row=0, column=1, padx=5)

tk.Label(frame_tempo, text="Minutos:").grid(row=0, column=2, padx=5)
entrada_minutos = tk.Entry(frame_tempo, width=5)
entrada_minutos.grid(row=0, column=3, padx=5)

tk.Label(frame_tempo, text="Segundos:").grid(row=0, column=4, padx=5)
entrada_segundos = tk.Entry(frame_tempo, width=5)
entrada_segundos.grid(row=0, column=5, padx=5)

# Label para exibir o tempo restante
label_tempo = tk.Label(janela, text="00:00:00", font=("Arial", 24))
label_tempo.pack(pady=20)

# Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_iniciar = tk.Button(frame_botoes, text="Iniciar", command=iniciar_cronometro)
botao_iniciar.grid(row=0, column=0, padx=5)

botao_pausar = tk.Button(frame_botoes, text="Pausar", command=pausar_cronometro, state=tk.DISABLED)
botao_pausar.grid(row=0, column=1, padx=5)

botao_zerar = tk.Button(frame_botoes, text="Zerar", command=zerar_cronometro, state=tk.DISABLED)
botao_zerar.grid(row=0, column=2, padx=5)

botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.pack(pady=10)

# Iniciar a interface gráfica
janela.mainloop()
