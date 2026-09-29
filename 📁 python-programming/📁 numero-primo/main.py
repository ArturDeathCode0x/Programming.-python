
def divisao_primo(n):
    if n <= 1:
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True

while True:
    num = int(input("Número: "))

    if divisao_primo(num):
        print(" primo")
    else:
        print(" não  primo")
        break