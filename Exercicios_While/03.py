senha_correta = 'python é show'
senha_digitada = ''

while senha_digitada != senha_correta:
    senha_digitada = input('Por favor, digite a senha: ').lower()
    if senha_digitada != senha_correta:
        print('Você errou a senha... tente novamente.')

print('Acesso liberado. Você acertou a senha.')