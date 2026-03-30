escolha_usuario = 9309
# 0 > sai do programa
# 1 > entra no programa

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("404 Fatal Error!")