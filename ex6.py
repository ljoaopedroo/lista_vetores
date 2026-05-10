vetor = [0] * 10

for i in range(10):
    vetor[i] = int(input(f"Digite o valor da posição {i}: "))

maior = vetor[0]
menor = vetor[0]

for i in range(1, 10):
    if vetor[i] > maior:
        maior = vetor[i]

    if vetor[i] < menor:
        menor = vetor[i]

print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")