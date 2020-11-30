def soma_matrizes(m1, m2):

    
    #checar se as funções têm o mesmo tamanho
    num_linha1, num_linha2 = len(m1), len(m2)
    num_col1, num_col2 = len(m2[0]), len(m2[0])

    resultado = []

    if (num_linha1 == num_linha2)and (num_col1 == num_col2):
        # caso verdadeiro fazer a soma
        for i in range(num_linha1):
            linha = [0] * num_col1
            resultado.append(linha)
            for j in range(num_col1):
                resultado.append
                resultado[i][j] = m1[i][j] + m2[i][j]  

    else:
        return False
         
   
    #print("soma_matrizes(m1, m2) => {}".format(resultado)) #TIRAR ANTES DE ENVIAR
    return resultado

#m1 = [[1], [2], [3]]
#m2 = [[2, 3, 4], [5, 6, 7]]

#m1 = [[1, 2, 3], [4, 5, 6]]
#m2 = [[2, 3, 4], [5, 6, 7]]

#soma_matrizes(m1, m2)




    
