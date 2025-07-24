from view import limpa_tela, titulo, menu_escolha, menu_1, menu2

                
while True:
    limpa_tela()
    titulo()
    menu = menu_escolha()
    if menu == 1:
        menu_1()
    elif menu == 2:
        menu2()
    elif menu == 0:
        break
    else:
        print('inválido')
