"""Trabalhando com arquivos"""

# arquivo = open('olaMundo.txt', 'w')
# arquivo.write('Olá mundo Python!')
# arquivo.close()

# arquivo1 = open('exemplo.txt', 'a')
# arquivo1.write('Editando um arquivo existente na pasta.')
# arquivo1.close()

# arquivo_leitura = open('exemplo.txt','r')
# print(arquivo_leitura)
# conteudo = arquivo_leitura.read()
# print(conteudo)
# arquivo_leitura.close()

# arquivo2 = open('olaMundo2.txt', 'w')
# arquivo2.write('Olá novamente mundo Python')
# arquivo2.write('\n Continue a estudar, desafio dos 60 dias em Python.')
# arquivo_lido = open('olaMundo2.txt', 'r')
# apresentar_conteudo = arquivo_lido.read()
# print(apresentar_conteudo)
# arquivo.close()

#sempre quando o bloco de código acabar ele vai fechar automaticamente o arquivo
# with open('olaMundo2.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

#ainda melhor, pois testa e retorna mensagem se não identificado,
# e sempre quando o bloco de código acabar ele vai fechar automaticamente o arquivo
try:
    with open('olaMundo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print('Arquivo não encontrado.')

try:
    with open('olaMundo3.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print('Arquivo não encontrado.')
