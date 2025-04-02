import time

#Criando um decorator
def medir_tempo_execucao(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Iniciando em {start_time}.")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Finalizando em {end_time}.")
        total_time = end_time - start_time
        print(f"O tempo total foi de:  {total_time}.")
        return result
    return wrapper

@medir_tempo_execucao
def tarefa_1():
    print("Rodando  função ...")
    time.sleep(3)
    print("Função finalizada!")

tarefa_1()

@medir_tempo_execucao
def tarefa_2():
    print("Rodando  função ...")
    time.sleep(2)
    print("Função finalizada!")

tarefa_2()