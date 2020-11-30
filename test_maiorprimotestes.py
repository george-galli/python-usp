def maior_primo(num):
    while num > 2:
        i = 2

        while True:
            if num % i == 0:
                break
            if i == num - 1:
                return num
            i = i + 1

            num = num - 1

def test_primo():
    assert maior_primo(97) == 97
