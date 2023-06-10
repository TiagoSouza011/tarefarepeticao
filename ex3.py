soma = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        break
    soma += n

print('A soma dos números digitados é:', soma)