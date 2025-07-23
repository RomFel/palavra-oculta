palavra='oculta'
import os

def titulo():
    print('-'*50)
    print(f'{"Palavra Oculta":^50}')
    print('-'*50)

recordistas = []
while True:
    try:
        with open('record.txt', 'r') as arquivo:
            for  linha in arquivo:
                separa= linha.strip().split(';')
                recordistas.append({'nome':separa[0], 'pontos': int(separa[1])})
            break
    except FileNotFoundError:
        with open('record.txt', 'a') as arquivo:
            num = 1000
            for i in range(10):
                arquivo.write(f'ROM;{num}\n')
                num -= 100
                
while True:
    os.system('cls')
    titulo()
    menu = int(input('[1] Jogar\n'
                     '[2] Recordes\n'
                     '[0] Sair\n'
                     'opção: '))
    if menu == 1:
        os.system('cls')
        from random import choice

        pts_totais = 0

        dica = ['cor', 'fruta', 'cidade', 'time', 'objeto', 'animal']
        lista_palavras = [
            ['verde', 'amarelo', 'azul', 'vermelho','laranja', 'marrom', 'preto', 'branco', 'rosa', 'roxo'],
            
            ['manga', 'banana', 'morango', 'uva', 'abacate', 'kiwi', 'goiaba', 'abacaxi'],
            
            ['maxaranguape','olinda', 'recife', 'natal', 'londres', 'roma', 'paris', 'berlim', 'lisboa', 'touros',
             'parnamirim', 'chicago', 'toronto', 'extremoz', 'pequim', 'sydney'],
            
            ['palmeiras','fluminense', 'flamengo', 'sport', 'santos', 'internacional', 'corinthians', 'botafogo',
             'cruzeiro', 'vasco', 'liverpool', 'arsenal', 'milan', 'barcelona', 'roma', 'benfica', 'porto', 'sporting', 'borussia', 'bayern'],
            
            ['bolsa', 'borracha', 'camisa', 'sapato', 'bola', 'caneta', 'cadeira', 'dado', 'escova', 'livro',
             'caderno', 'controle', 'mesa', 'geladeira', 'carro', 'computador', 'gravata', 'controle', 'microfone'],
            
            ['abelha', 'gato', 'pato', 'tigre', 'elefante', 'zebra', 'cachorro', 'canguru', 'galinha', 'papagaio',
             'peixe', 'cobra', 'urso', 'lula', 'baleia', 'carangueijo', 'lagosta', 'andorinha', 'urubu', 'porco']
        ]

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
                os.system('cls')

            os.system('cls')
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
            os.system('cls')
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
        

    elif menu == 2:
        os.system('cls')
        titulo()
        print(f'{"Recordes":^50}')
        
        for i, recordista in enumerate(recordistas):
            print(f'{i+1:0>2}  {recordista["nome"]:<40}{recordista["pontos"]:>5}')
            
        input('pressione <enter> para voltar')
    elif menu == 0:
        break
    else:
        print('inválido')