import os
from controller import exibe_records

def limpa_tela():
    os.system('cls||clear')


def titulo():
    print('-'*50)
    print(f'{"Palavra Oculta":^50}')
    print('-'*50)


def menu_escolha():
    escolha = int(input('[1] Jogar\n'
                     '[2] Recordes\n'
                     '[0] Sair\n'
                     'opção: '))
    return escolha


def menu2():
    limpa_tela()
    titulo()
    print(f'{"Recordes":^50}')
    
    exibe_records()
        
    input('pressione <enter> para voltar')