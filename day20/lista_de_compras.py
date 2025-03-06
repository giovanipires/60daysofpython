# Constantes para as opções do menu
ADICIONAR_ITEM = '1'
REMOVER_ITEM = '2'
VER_LISTA = '3'
SAIR = '4'

lista_compras = []

def adicionar_item():
    item = input("Digite o item a ser adicionado: ")
    lista_compras.append(item)
    print(f"{item} foi adicionado à lista.")

def remover_item():
    if not lista_compras:
        print("A lista está vazia.")
        return

    item = input("Digite o item a ser removido: ")
    if item in lista_compras:
        lista_compras.remove(item)
        print(f"{item} foi removido da lista.")
    else:
        print("Item não encontrado na lista.")

def ver_lista():
    if not lista_compras:
        print("A lista está vazia.")
    else:
        print("\nSua lista de compras:")
        for i, item in enumerate(lista_compras, 1):
            print(f"{i}. {item}")

def main():
    while True:
        print("\n1. Adicionar item")
        print("2. Remover item")
        print("3. Ver lista")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == ADICIONAR_ITEM:
            adicionar_item()
        elif opcao == REMOVER_ITEM:
            remover_item()
        elif opcao == VER_LISTA:
            ver_lista()
        elif opcao == SAIR:
            print("Obrigado por usar o programa!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
