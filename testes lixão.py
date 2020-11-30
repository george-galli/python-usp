
def compara_assinatura(as_a, as_b):  
    calc = 0
    xot = 0
    while xot <= 5:
        calc = calc + abs(as_a[xot] - abs(as_b[xot])
        xot += 1
        similaridade = calc / 6
    print(similaridade)


as_a = [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]
as_b = [4,79, 0,72, 0,56, 80,5, 2,5, 31,6]

compara_assinatura(as_a,as_b)

