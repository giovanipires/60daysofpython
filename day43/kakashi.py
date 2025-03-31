class Ninja:
    def __init__(self, nome, chakra):
        self.nome = nome
        self.chackra = chakra
        
    def usar_jutsu(self, custo_chakra):
        try:
            if custo_chakra > self.chackra:
                raise ValueError("Chakra insuficiente!")
            self.chackra -= custo_chakra
            print(f"O {self.nome} usou o jutsu com sucesso!")
        except ValueError as Error:
            print(f"Erro: {Error} foi detectado. O {self.nome} precisa se recuperar.")
            
if __name__ == "__main__":
    naruto = Ninja(nome="Kakashi", chakra=200)
    naruto.usar_jutsu(50)
    naruto.usar_jutsu(50)
    naruto.usar_jutsu(201)