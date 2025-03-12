def escrever_arquivo(nome_arquivo, conteudo):
    """_summary_
    Escreve no arquivo o conteudo passado como parametro.
    Args:
        nome_arquivo (string): O nome dado ao arquivo criado
        conteudo (string): O conteudo contido no arquivo criado
    """
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f'O conteudo foi salvo no arquivo: {nome_arquivo}.')
    
def ler_arquivo(nome_arquivo):
    """_summary_
    Le o conteudo do arquivo e imprime na tela.
    Args:
        nome_arquivo (string): O nome do arquivo a ser lido
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print(f'O conteudo do arquivo {nome_arquivo} é: {conteudo}')
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')

def main(nome_arquivo, conteudo):
    """_summary_
    Função principal do programa.
    Args:
        nome_arquivo (string): O nome do arquivo a ser criado
        conteudo (string): O conteudo do arquivo a ser criado
    """ 
    print('Bem vindo ao programa de escrita e leitura de arquivos.')
    escrever_arquivo(nome_arquivo, conteudo)
    print('Fazer a leitura do arquivo ... ')
    ler_arquivo(nome_arquivo)

if __name__ == '__main__':
    arquivo = 'arquivo.txt'
    texto = 'Giovani Pires no 26º dia de Python.'
    main(arquivo, texto)
