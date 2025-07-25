import os

from controller import exibe_records, record, novo_record
from data import dica, lista_palavras
from stats import Jogador


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


def menu_2():
    limpa_tela()
    titulo()
    print(f'{"Recordes":^50}')
    exibe_records()
    input('pressione <enter> para voltar')


def cabecalho(pts_jogador, pts_totais_jogador, dica_jogador, chances_jogador, noticia_jogador):
    titulo()
    print(f'Pontos atuais: {pts_jogador:<3} || Pontos Totais: {pts_totais_jogador+pts_jogador}')
    print(f'Dica: {dica_jogador:<13}|| Chances: {chances_jogador}')
    print(noticia_jogador)    


def palavra_ocultada(jogador):
    for j in jogador.oculto:
        print(j, end=' ')
    print()


def menu_1():
        limpa_tela()
        jogador = Jogador()
        roda_jogo(jogador)


def roda_jogo(jogador):
    while True:
        jogador.nova_palavra()
        miolo_jogo(jogador)

        limpa_tela()
        titulo()    
        palavra_ocultada(jogador)
        jogador.pts_totais += jogador.pts
        if jogador.chances == 0:
            msg_palavra_nao_completa(jogador.ale_palavra)
            input(msg_continuar(boo=True))
            break
        else:
            msg_palavra_completa(jogador.pts)

        resp = input(msg_continuar())
        limpa_tela()
        if resp == '0':
            break

    final_jogo(jogador)


def miolo_jogo(jogador):
    while '_' in jogador.oculto:             
        cabecalho(jogador.pts, jogador.pts_totais, jogador.ale_dica, jogador.chances, jogador.noticia)
        
        if jogador.chances == 0:
            break
        palavra_ocultada(jogador)
        escolha = input('Letra: ')
        if escolha not in jogador.oculto:
            if escolha in jogador.ale_palavra:
                for i, letra in enumerate(jogador.ale_palavra):
                    if letra == escolha: 
                        jogador.pts += jogador.chances
                        jogador.oculto[i] = escolha
                        jogador.noticia = ''
            else:
                jogador.noticia = msg_letra_na_palavra(escolha, boo=False)
                jogador.chances -= 1
        elif escolha in jogador.oculto:
            jogador.noticia = msg_letra_na_palavra(escolha)
        limpa_tela()


def final_jogo(jogador):
    msg_pontuacao_final(jogador.pts_totais)
    novo_record(jogador.pts_totais)


def msg_letra_na_palavra(letra, boo=True):
    return f'Palavra já contém [{letra}]' if boo else f'Palavra não contém [{letra}]'


def msg_continuar(boo=True):
    return 'pressione <enter> para continuar' if boo else 'pressione <enter> para continuar ou [0] para sair '


def msg_palavra_nao_completa(palavra):
    print('Você perdeu')
    print(f'A palavra era {palavra}')


def msg_palavra_completa(pts_jogador):
    print(f'Parabéns! Você ganhou!!! +{pts_jogador} pts')


def msg_pontuacao_final(pts_final_jogador):
    print(f'Pontuação final: {pts_final_jogador}')


def msg_novo_record():
    print(f'Novo recorde!')