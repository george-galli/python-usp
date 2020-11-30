lista = ["Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o " \
        "outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não" \
         " falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas " \
         "quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; " \
         "sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que " \
         "trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras" \
         " do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",
          "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol " \
        "amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um " \
        "planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão " \
       "extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."]
   
confere = 0
referencia = 100
while confere < len(lista):
    confere+= 1

    print(confere)
        #text = textos[i]
        #calc = calcula_assinatura(textos[i])
#compara = compara_assinatura(calcula_assinatura(textos[confere]), ass_cp)
    #if compara < referencia:
        #referencia = compara
        #indice_texto = confere
        #confere += 1
    #print("O autor do texto", indice_texto+1, "está infectado com COH-PIAH")
    #return indice_texto



referencia = [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]
text = le_textos()
calcula_assinatura(text) # Funciona corretamente
avalia_textos(text, referencia) # Não funciona
