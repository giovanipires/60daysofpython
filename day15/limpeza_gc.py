"""Entendendo o funcionamento do gc"""
import gc

class Saiyajin:
    def __init__(self, nome):
        self.nome = nome
        self.amigo = None
        
def contar_objetos_saiyajin():
    objetos = [obj for obj in gc.get_objects() if isinstance(obj, Saiyajin)]
    print(f"Objetos Saiyajin ativos: {len(objetos)}")

goku = Saiyajin("Goku")
vegeta = Saiyajin("Vegeta")

goku.amigo = vegeta
vegeta.amigo = goku

contar_objetos_saiyajin()
print("Contando o primeiro ciclo de objetos.")

del goku
del vegeta

contar_objetos_saiyajin()
print("Contando o segundo ciclo de objetos.")

gc.collect()
contar_objetos_saiyajin()
print("Contando após o gc!")
