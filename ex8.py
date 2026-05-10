notas = [0] * 15
soma = 0
media = 0

for i in range(15):
    notas[i] = float(input("Digite a nota do aluno: "))

for i in range(15):
    soma += notas[i]

media = soma / 15

print(f"Média: {media:.2f}")