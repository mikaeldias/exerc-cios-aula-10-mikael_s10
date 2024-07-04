n =  int(input('Digite um numero para fatorar: '))
fatorial = 1

while n > 1:
    fatorial *= n
    n -= 1
    print(fatorial)
print(f'O fatorial de {n}, é {fatorial}')        