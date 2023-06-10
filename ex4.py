import random
resul = random.randint(0, 1)


num_jogadas = int(input('Digite o número de vezes que você quer jogar a moeda: '))

num_caras = 0
num_coroas = 0

for i in range(num_jogadas):
    if resul == 0:
        print('Cara')
        num_caras += 1
    else:
        print('Coroa')
        num_coroas += 1

print('Número total de caras: ', num_caras)
print('Número total de coroas: ', num_coroas)

if num_caras > num_coroas:
    print('\nO número de de caras foi maior')
else:
    print('\nO número de de coroas foi maior')