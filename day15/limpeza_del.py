"""Entendendo o funcionamento do gc"""
import gc

class Saiyajin:
    def __init__(self, nome):
        self.nome = nome
        
def contar_objetos_saiyajin():
    objetos = [obj for obj in gc.get_objects() if isinstance(obj, Saiyajin)]
    print(f"Objetos Saiyajin ativos: {len(objetos)}")

goku = Saiyajin("Goku")
print(f"O saiyajin {goku} foi criado.")
print(f"O saiyajin {goku.nome} foi criado.")
contar_objetos_saiyajin()

del goku
print("O personagem foi deletado ... ")
contar_objetos_saiyajin()
