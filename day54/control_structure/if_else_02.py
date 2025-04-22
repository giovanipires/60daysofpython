from colorama import Fore, Style

def faixa_etaria(idade):
    """_summary_

    Args:
        idade (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if 0 <= idade < 18:
        return 'Menor de idade.'
    elif idade in range(18, 64):
        return 'Adulto.'
    elif idade in range(65, 100):
        return 'Melhor idade.'
    elif idade >= 100:
        return 'Centenário.'
    else:
        return Fore.RED + 'Idade inválida.' + Style.RESET_ALL

if __name__ == '__main__':
    for idade in (17, 23, 35, 87, 101, 44, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
