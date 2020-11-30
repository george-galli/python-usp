def maior_primo(n):
    aux = n
    while aux > 2:
        if eh_primo(aux):                #FUNCIONANDO!!!!!!!!!
            return aux
        aux -= 1
    return 2

def eh_primo(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


print("maior primo: " + str(maior_primo(100)))




    
