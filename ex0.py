while True:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o último valor: '))

    if valor1 < valor2:
        for i in range(valor1, valor2+1):
            print(i)
    elif valor1 > valor2:
        for i in range(valor1, valor2-1, -1):
            print(i)
    else:
        print('Os valores são iguais!')

    outra= input('Deseja fazer outra consulta? (s/n) \n Resp: ')
    if outra.lower() == 'n':
        break

