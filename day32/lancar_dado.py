from random import randint

def lancar_dado():
    """_summary_
    Simulação de lançamento de dado de 6 faces
    Returns:
        int: Um número aleatório de 1 a 6
    """    
    return randint(1, 6)

if __name__ == '__main__':
    print(f"O resultado do dado foi: {lancar_dado()}")
