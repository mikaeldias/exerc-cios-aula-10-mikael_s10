import random

while True:
    
    
    chute = int(input('Chute um numero entre (1 a 100): '))
    sorteio_numerico = random.randint(1, 100)
    if chute == sorteio_numerico:
        print(f'Parabéns, você chutou o numero {chute}, e acertou... festa')
        break
    else:
        print(f'Poxa... O numero sorteado foi {sorteio_numerico}, e você chutou o {chute}... tente novamente.')     
    if chute > 100:
        print(f'Por favor, digite valores entre 1 a 100. \n Você digitou {chute}, esse valor está fora do padrao.')
    if chute < 1:
        print(f'Por favor, digite valores entre 1 a 100. \n Você digitou {chute}, esse valor está fora do padrao.')
print('fim do programa.')