def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    jogar = int(input())

    if jogar == 1:
        print("Você escolheu uma partida isolada!")
        return partida()
    if jogar == 2:
        print("Você escolheu um campeonato!")
        return campeonato()
    else:

        return main()
    
def partida():

    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))

    joga_c = False


    if n % (m + 1) == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
        joga_c = True


    while n > 0:
        if joga_c:
            lance_c = computador_escolhe_jogada(n,m)
            n = n - lance_c
            if lance_c == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador tirou",lance_c,"peças.")
                tabuleiro_lance(n)
                lance_u = usuario_escolhe_jogada()
            joga_c = False
        else:
            lance_u = usuario_escolhe_jogada(n,m)
            n = n - lance_u
            if lance_u == 1:
                print("Você tirou uma peça")
            else:
                print("Você tirou",lance_u,"peças")
            tabuleiro_lance(n)
            return computador_escolhe_jogada(n,m)
            joga_c = True







        print("Fim de jogo! O computador ganhou!")



def tabuleiro_lance(n):
    if n == 1:
        print("Agora resta uma peça no tabuleiro")
    else:
        print("Agora restam %i peças no tabuleiro"%n)
        return n



def computador_escolhe_jogada(n,m):

    lance_c = 1

    while lance_c != m:
        if (n - lance_c) % (m + 1) == 0:
            return lance_c
        else:
            lance_c = lance_c + 1
            return lance_c


def usuario_escolhe_jogada(n,m):
    lanceok = True
    while lanceok:
        lance_u = int(input("Quantas peças você vai tirar?"))
        if lance_u > m or lance_u < 1:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            return lance_u



main()


 #def campeonato():

