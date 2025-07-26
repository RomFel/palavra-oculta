import os


def limpa_tela():
    os.system('cls||clear')


def record():
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
    return recordistas


def exibe_records():
    recordistas = record()
    for i, recordista in enumerate(recordistas):
        print(f'{i+1:0>2}  {recordista["nome"]:<40}{recordista["pontos"]:>5}')


def novo_record(rec):
    from view import msg_novo_record
    recordistas = record()
    for i, recordista in enumerate(recordistas):
        if recordista['pontos'] < rec:
            msg_novo_record()
            nome = input('Nome: ').upper()[:3]
            recordistas.insert(i, {'nome': nome, 'pontos': rec})
            recordistas.pop()
            break
    with open('record.txt', 'w') as arquivo:
        for recordista in recordistas:
            arquivo.write(f'{recordista["nome"]};{str(recordista["pontos"])}\n')