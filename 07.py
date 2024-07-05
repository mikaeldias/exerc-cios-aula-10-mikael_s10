n1 = int(input('Digite um numero de 1 a 10.000: '))

total = 0
while True:
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            total += 1
        else:
            pass 
    break
if total == 2:
    print('ele é primo')
else: 
    print('Não é primo')   