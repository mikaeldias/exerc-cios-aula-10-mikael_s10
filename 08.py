n1 = int(input('Digite um numero inteiro: '))

while True:
    alocando_em_lista = [int(digito) for digito in str(n1)]
    print(alocando_em_lista)
    break
print(sum(alocando_em_lista))