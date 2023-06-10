candidatos = {
    1: "Candidato Jair Rodrigues",
    2: "Candidato Carlos Luz",
    3: "Candidato Neves Rocha",
    4: "Nulo",
    5: "Branco"
}

votos = {candidato: 0 for candidato in candidatos}


while True:
    print("As opções são:")
    for key, value in candidatos.items():
        print(f"{key}. {value}")
    print("6. Encerrar votação")
    voto = int(input("Entre com o seu voto: "))

    if voto == 6:
        break
    elif voto in candidatos:
        votos[voto] += 1
    else:
        print("Opção inválida. Tente novamente.")



total_votos = sum(votos.values())

print("\nResultado da votação:")
for candidato, votos_candidato in votos.items():
    print(f"{candidatos[candidato]}: {votos_candidato} votos ({votos_candidato / total_votos * 100:.2f}%)")

candidato_vencedor = max(votos, key=votos.get)
if votos[candidato_vencedor] == votos[4] or votos[candidato_vencedor] == votos[5]:
    print("A eleição foi para segundo turno.")
else:
    print(f"O vencedor da eleição é o {candidatos[candidato_vencedor]} com {votos[candidato_vencedor]} votos.")