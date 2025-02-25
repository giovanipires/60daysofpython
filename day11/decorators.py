"""decorators"""

# @decorator_name

def primeiro_decorator(funcao):
    def camada():
        print("Camada 1")
        funcao()
        print("Camada 2")
    return camada

@primeiro_decorator
def funcao_dois():
    print("Camada do meio")

funcao_dois()

import time

def calcula_time(funcao):
    def camada():
        """calcular o tempo"""
        tempo_1 = time.time()
        funcao()
        tempo_2 = time.time()

        tempo_final = tempo_2 - tempo_1
        print(tempo_final)
    return camada

@calcula_time
def milhares():
    for i in range(0,10000):
        pass

milhares()

"""Pesquisar sobre flask, abaixo exemplo de uso real"""
# @app.route('/admin')
# def admin_index():
#     #Verifica se session['logado'] já foi setado
#     if('logado' not in session):
#         return redirect('index')

#     #caso o usuário esteja logado, redenriza a página /admin/index.thml
#     return render_template('/admin/index.html')
