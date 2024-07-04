print('O programa a seguir, realiza a soma de dois valores. \nCaso deseje finalizar o programa, digite 0.')

while True:
    n1 = float(input('Digite um numero para somar: '))
    n2 = float(input('Digite outro numero para somar: '))
    soma = n1 + n2 
    print(soma)
    if n1 or n2 == 0:
        break   
print('fim...  Você digitou zero em um dos campos.')    
