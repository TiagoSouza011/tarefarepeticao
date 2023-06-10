capital_inicial = float(input("Digite o valor inicial da poupança: "))

juros = 0.005

periodos = 12

for mes in range(1, periodos+1):
    montante = capital_inicial * (1 + juros)**mes
    print(f"Montante no mês {mes}: R${montante:.2f}")