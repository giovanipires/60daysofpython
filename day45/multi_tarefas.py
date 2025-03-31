#threads
import threading
import time

def tarefa(nome, tempo_execucao):
    print(f"Tarefa {nome} iniciada ...")
    time.sleep(tempo_execucao)
    print(F"Finalizada a tarefa {nome}.")
    
thread1 = threading.Thread(target=tarefa, args=("Download tarefa 1", 3))
thread2 = threading.Thread(target=tarefa, args=("Download tarefa 2", 4))
thread3 = threading.Thread(target=tarefa, args=("Download tarefa 3", 6))

#iniciando threads
thread1.start()
thread2.start()
thread3.start()

#aguardando as tarefas
thread1.join()
thread2.join()
thread3.join()

print("Todas as tarefas foram finalizadas.")