def computador_escolhe_jogada(n,m):

    i = 1

    while i <= m:
        x = n - i
        y = x % m
        i = i + 1
        if y == 0:
            lance = i - 1
            if lance == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",lance,"peças.")


computador_escolhe_jogada(19,5)
