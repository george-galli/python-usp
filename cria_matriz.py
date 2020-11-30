'''(int, int, valor) -> matriz(lista de listas)
Cria e retorna uma matriz com num_linhas linhas e num_colunas
colunas em que cada elemento é igual ao valor dado'''

def cria_matriz(num_linhas, num_colunas, valor):

    matriz = []  # guarda as linhas da matriz
    for i in range(num_linhas):  #cria a linha "i"
        linha = []  # lista vazia
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)  # adiciona linha a matriz

    print(matriz)



    return matriz

cria_matriz(5, 8, 2)