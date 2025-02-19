#strings
# personagem = 'He-Man'
frase = 'Pela força de Grayskull, eu sou o He-Man!'
# discurso = """Lutamos não apenas por poder, mas pela justiça."""
# novo_discurso = discurso.replace("justiça", "justiça e amor")
# impacto = personagem + discurso
# acao = 'Espada de Grayskull'
# socar = 'Pow'
# acerto = 'Pei'
# inimigo = 'Esqueleto'
# # frase_cortar = frase[24:41]

# print(personagem)
# print(frase)
# print(discurso)
# print(frase + discurso)
# print(impacto)
# print(personagem + ' usa ' + acao)
# print(personagem + ' soca Esqueleto ' + socar * 3 + " " + " " + acerto * 2 + " ")
# print(frase.upper())
# print('Ohh não, é o ' + inimigo)
# print('Ohh não, é o ' + inimigo.upper())
# print(novo_discurso)
# print(frase_cortar)

#f-string
# nome = "Giovani"
# sobrenome = "Pires"
# nome_completo = f"{nome} {sobrenome}"

# print(nome_completo)

#format e concatenação
# inimigo_novo = 'Homem Peixe'
# frase_nova = "O {} guerreiro mais forte de {}, com sua espada e seus amigos ele venceu o ".format("He-Man", "Grayskull") + inimigo_novo.upper()
# print(frase_nova)

#pesquisa em strings
# castelo = 'Grayskull'
# print(castelo in frase)
# print(frase.find("Grayskull"))
# print(frase.count("Grayskull"))

#multilinhas em python """ texto """ e \n
multi = """ A luta de He-Man contra as forças do mal representa a busca pela justiça e a promoção da 
bondade, pois, a mensagem é de que agir com integridade e fazer o que é certo é fundamental. 
"""
multi2 = 'A luta de He-Man contra as forças do mal representa a busca pela justiça e a promoção da \n bondade, pois, a mensagem é de que agir com integridade e fazer o que é \n certo é fundamental.'


print(multi)
print(multi2)
print(multi2.split())