import re

# funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal =4.79 #float(input("Entre o tamanho médio de palavra:"))
    ttr =0.72 #float(input("Entre a relação Type-Token:"))
    hlr =0.56 #float(input("Entre a Razão Hapax Legomana:"))
    sal =80.5 #float(input("Entre o tamanho médio de sentença:"))
    sac =2.5 #float(input("Entre a complexidade média da sentença:"))
    pal =31.6 #float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

 #A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

 #A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


#A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

#A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
def separa_palavras(frase):
    return frase.split()

#Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

#Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)



#IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
def compara_assinatura(as_a, as_b):
    calc = 0
    func = 0
    while func <= 5:
        calc = calc + abs(as_a[func] - abs(as_b[func]))
        func += 1
        similaridade = calc / 6
    return similaridade


#as_a = [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]
#as_b = [4,79, 0,72, 0,56, 80,5, 2,5, 31,6]

#compara_assinatura(as_a,as_b)



#IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto
def calcula_assinatura(texto):
    sentenças = separa_sentencas(texto)
    #print (sentenças)
    dividido_frases = []
    for frases in sentenças:
        dividido_frases.extend(separa_frases(frases))
    #print(dividido_frases)
    so_palavras = []
    for palav in dividido_frases:
        so_palavras.extend(separa_palavras(palav))
    #print(so_palavras)
    total_palavras = len(so_palavras)         #DEVOLVE TOTAL DE PALAVRAS DA LISTA DE PALAVRAS
    #print(total_palavras)
    numero_sentenças = len(sentenças)       #DEVOLVE NUMERO DE SENTENÇAS
    #print(numero_sentenças)
    numero_de_frases = len(dividido_frases)     #DEVOLVE O NUMERO DE FRASES
    #print(numero_de_frases)

    total_caracteres_sentenças = 0
    k = 0
    while k < len(sentenças):             #CALCULA O TOTAL DE CARACTERES EM TODAS AS SENTENÇAS
        total_caracteres_sentenças = total_caracteres_sentenças + len(sentenças[k])
        k += 1
    #print(total_caracteres_sentenças)
    total_caracter = 0
    i = 0
    while i < len(so_palavras):   #CALCULA O TOTAL DE CARACTERES NA LISTA DE PALAVRAS
        total_caracter = total_caracter + len(so_palavras[i])
        i = i + 1
    #print(total_caracter)
    total_caracteres_frase = 0
    m = 0
    while m < len(dividido_frases):              #CALCULA O NUMERO DE CARACTERES EM CADA FRASE
        total_caracteres_frase = total_caracteres_frase + len(dividido_frases[m])
        m += 1
    #print(total_caracteres_frase)
    wal_texto = (total_caracter) / (total_palavras)    # CALCULA O TAMANHO MEDIO DA PALAVRA
    #print(wal_texto)
    palavras_diferentes = n_palavras_diferentes(so_palavras)
    ttr_texto = palavras_diferentes  /  total_palavras    #CALCULA O TYPE-TOKEN
    #print(ttr_texto)
    hapax_legomana = n_palavras_unicas(so_palavras)
    hlr_texto = hapax_legomana / total_palavras               #CALCULA HAPAX LEGOMANA
    #print(hlr_texto)
    sal_texto = total_caracteres_sentenças / numero_sentenças   #CALCULA TAMANHO MÉDIO DA SENTENÇA
    #print(sal_texto)
    sac_texto = numero_de_frases / numero_sentenças                        #CALCULA A COMPLEXIDADE DA SENTENÇA
    #print(sac_texto)
    pal_texto = total_caracteres_frase / numero_de_frases          #CALCULA TAMANHO MEDIO DE FRASE
    #print(pal_texto)
    assinatura = [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]
    return assinatura




#texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol " \
 #       "amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um " \
 #       "planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão " \
 #       "extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."


#calcula_assinatura(texto)


#'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp
# e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
def avalia_textos(textos, ass_cp):

    textos = le_textos()

    each_texto = []
    for elemento in le_textos():   #
        each_assinatura = calcula_assinatura(texto)
        each_texto.append(compara_assinatura(each_assinatura, ass_cp))
    just_one = each_texto(0)
    resultado = 0
    for termo in range(1, len(each_texto)):
        if (just_one < each_texto[termo]):
            resultado = termo
            return resultado

    print("O autor do texto {} está infectado com COH-PIAH", resultado)









#textos = ["Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o " \
#        "outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não" \
#         " falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas " \
#         "quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; " \
#         "sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que " \
#         "trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras" \
#         " do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",
#          "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol " \
#        "amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um " \
#        "planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão " \
#       "extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."]


#ass_p = [4,79, 0,72, 0,56, 80,5, 2,5, 31,6]

#avalia_textos(textos, ass_p)
    


le_assinatura()

le_textos()
avalia_textos(textos, ass_cp)
#separa_sentencas()
#separa_frases()
#separa_palavras()
#avalia_textos()
#calcula_assinatura()
#compara_assinatura()

