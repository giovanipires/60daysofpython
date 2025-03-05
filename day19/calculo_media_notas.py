print('Bem vindo ao cálculo de médias')

def calcular_media_notas(notas):
    """_summary_
    Função simples de cálculo de média de notas
    Args:
        notas (lista): Notas que foram tiradas pelo aluno

    Returns:
        float: média de notas
    """  
    media = sum(notas) / len(notas)
    #round arredonda a media para 2 casas decimais
    return round(media, 2)

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

print(calcular_media_notas([nota1, nota2, nota3, nota4]))
