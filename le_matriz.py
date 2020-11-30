'''(int, int) -> matriz(lista de listas)
Cria e retorna uma matriz com num_linhas linhas e num_colunas
colunas em que cada elemento é digitado pelo usuário'''
def cria_matriz(num_linhas, num_colunas):

    matriz = []  # guarda as linhas da matriz
    for i in range(num_linhas):  #cria a linha "i"
        linha = []  # lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)

        matriz.append(linha)  # adiciona linha a matriz

    #print(matriz)

    return matriz

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))

    return cria_matriz(lin, col)


lista = le_matriz()
print (lista)
for der in range(len(lista)):
    for val in range(len(lista[0])):
        print ((lista[der][val]), end= " ")
    print()





#le_matriz()

