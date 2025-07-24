import os
from controller import exibe_records, record
from data import dica, lista_palavras

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


def menu_1():
        recordistas = record()
        limpa_tela()
        from random import choice

        pts_totais = 0
        while True:
            pts = 0
            chances = 5
            ale_dica = choice(dica)
            ale_palavra = choice(lista_palavras[dica.index(ale_dica)])
            oculto = []
            noticia = ' '
            for l in range(len(ale_palavra)):
                oculto.append('_')

            while '_' in oculto:
                titulo()
                print(f'Pontos atuais: {pts:<3} || Pontos Totais: {pts_totais+pts}')
                print(f'Dica: {ale_dica:<13}|| Chances: {chances}')
                print(noticia)
                noticia = ' '
                if chances == 0:
                    break
                for j in oculto:
                    print(j, end=' ')
                print()
                escolha = input('Letra: ')
                if escolha not in oculto:
                    if escolha in ale_palavra:
                        for i, letra in enumerate(ale_palavra):
                            if letra == escolha: 
                                pts += chances
                                oculto[i] = escolha
                    else:
                        noticia = (f'Palavra não contém [{escolha}]')
                        chances -= 1
                elif escolha in oculto:
                    noticia = (f'Palavra já contém [{escolha}]')
                limpa_tela()

            limpa_tela()
            titulo()    
            for j in oculto:
                print(j, end=' ')
            print()
            pts_totais += pts
            if chances == 0:
                print('Voce perdeu')
                print(f'A palavra era {ale_palavra}')
                input('presione <enter> para continuar')
                break
            else:
                print(f'Parabens! Você ganhou!!! +{pts} pts')

            resp = input('presione <enter> para continuar ou [0] para sair ')
            limpa_tela()
            if resp == '0':
                break

        print(f'Pontuação final: {pts_totais}')
        for i, recordista in enumerate(recordistas):
            if recordista['pontos'] < pts_totais:
                print(f'Novo recorde!')
                nome = input('Nome: ').upper()[:3]
                recordistas.insert(i, {'nome': nome, 'pontos': pts_totais})
                recordistas.pop()
                break
        with open('record.txt', 'w') as arquivo:
            for recordista in recordistas:
                arquivo.write(f'{recordista["nome"]};{str(recordista["pontos"])}\n')