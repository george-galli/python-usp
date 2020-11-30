meuCartão = int(input("Digite o número de seu cartão: "))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
    cartãoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartãoLido == meuCartão:
        encontreiMeuCartãoNaLista = True


if encontreiMeuCartãoNaLista:
    print("EBA!! Meu cartão está lá!")

else:
    print("Fodeu! Meu cartão não está lá!!")

          
