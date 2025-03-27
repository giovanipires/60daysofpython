class Veiculo:
    def __init__(self, marca, modelo, velocidade_max):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_max = velocidade_max
  
    def ligar_motor(self):
        print(f"O carro foi ligado, o modelo é {self.modelo} e a marca é {self.marca}.")

    def acelerar(self):
        print(f"O {self.modelo} está acelerando e sua velocidade máxima é {self.velocidade_max}.")
            
    def acender_luzes(self):
        print(f"O {self.modelo} está ligando seus faróis.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidade_max, portas):
        super().__init__(marca, modelo, velocidade_max)
        self.portas = portas
        
    def abrir_portas(self):
        print(f"O {self.modelo} da marca {self.marca} está abrindo suas {self.portas} porta.")
    
meu_veiculo = Veiculo(marca="Nissan", modelo="Kicks", velocidade_max=240)
meu_carro = Carro(marca="Fiat", modelo="147", velocidade_max=160, portas=3)

meu_veiculo.acelerar()
meu_veiculo.ligar_motor()
meu_veiculo.acender_luzes()

meu_carro.abrir_portas()
