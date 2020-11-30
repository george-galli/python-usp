# soma dos algarismos digitados
num = int(input("Digite um número qualquer: "))


soma = 0

while num != 0:
    x = num % 10
    num = num // 10
    soma = (soma + x)

print(soma)
    
