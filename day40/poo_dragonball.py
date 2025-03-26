class PersonagemDB:
    def __init__(self, nome, poder, nivel, transformacao="Base"):
        """_summary_
        Inicializar atributos do personagem
        Self garante que estes atributos sejam únicos para os personagem
        Args:
            nome (_type_): _description_
            poder (_type_): _description_
            nivel (_type_): _description_
        """
        self.nome = nome
        self.poder = poder
        self.nivel = nivel
        self.transformacao = transformacao
    
    def exibir_informacoes(self):
        """
        Exibe as informações dos personagens
        """
        print(f"Nome: {self.nome}")
        print(f"Poder: {self.poder}")
        print(f"Nivel: {self.nivel}")
        print(f"Tranformacao: {self.transformacao}")
        
    def treinar(self, horas):
        """_summary_
        Aumentar o poder dos personagem com base nas horas de treinamentos
        Args:
            horas (_type_): _description_
        """
        evolucao = horas * 10
        self.poder += evolucao
        print(f"{self.nome}, treinou por {horas} e aumentou seu poder em {evolucao}")
    
    def transformar(self, nova_transformacao):
        """_summary_
        Muda a transformacao do personagem
        Args:
            nova_transformacao (_type_): _description_
        """
        self.transformacao = nova_transformacao
        print(f"{self.nome} se transformou em {nova_transformacao}")
        
goku = PersonagemDB(
    nome= "Goku",
    poder= 9000,
    nivel= "Super Saiyajin"
)

goku.exibir_informacoes()

print("-----------------------------------------------------")

vegeta = PersonagemDB(
    nome="Vegeta",
    poder=8500,
    nivel="Saiyajin"
)

vegeta.treinar(horas=10)
vegeta.transformar(nova_transformacao="Super Saiyajin II")

vegeta.exibir_informacoes()

print("-----------------------------------------------------")