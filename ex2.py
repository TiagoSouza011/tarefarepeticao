import random
secreto = random.randint(1, 100)

errou = False

while not errou:
    resposta = int(input('Digite um número entre 1 e 100: '))
    if resposta == secreto:
        print('Boa, você acertou!')
        errou = True
    elif resposta < secreto:
        print('Errou; O número secreto é maior.')
    else:
        print('O número secreto é menor. Tente novamente.')