def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))

    k = n % (m + 1)

    if k == 0:
        print("Você começa!")
        return usuario_escolhe_jogada(n,m)
    else:
        print("Computador começa!")
        return computador_escolhe_jogada(n,m)

    aux = True

    while aux:
        n = n - lance_c
        if n == 0:
            print("fim do jogo! O computador ganhou!")
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro")

