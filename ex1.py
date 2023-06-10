quest = int(input('Digite um valor entre 1 a 10: '))
while True:
    if quest < 1 or quest > 10 :
        print('Digite um valor entre 1 a 10.')

    n = 1
    for n in range(1, 11):
        resposta = quest * n
        print(f'{quest} x {n} = {resposta}')
    
    outra = input('Deseja fazer outra consulta? (s/n) \n Resposta: ')
    if outra.lower() == 'n':
        break