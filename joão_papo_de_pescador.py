def pescaria():
    peso = float(input("Digite o peso da pescaria: "))
    excesso = (peso - 50)
    aux = excesso * 4
    multa = format(aux,".2f")
    if peso <= 50:
        print("Não há multa para o peso registrado")
        pescaria()
    else:
        print("Peso excedente:",excesso,"Kg")
        print("Valor da multa: R$",multa)
        pescaria()

pescaria()





