
ent = int(input("Digite uma sequência de números: "))

iguais = False
n_anterior = ent % 10
ent = ent // 10

while ent > 0 and not iguais
    n_atual = ent % 10
    ent = ent // 10
    if n_atual = = n_anterior:
        iguais = True
    n_anterior = n_atual
    
if iguais:
    print("Contém números adjacentes iguais")

else:
    print("Não contém")
