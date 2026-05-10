valores = [0] * 5
soma = 0

for i in range(5):
    valores[i] = int(input(f"Digite um número para a posição {i}: "))

maior = valores[0]
menor = valores[0]

for i in range(5):
    
    if valores[i] > maior:
        maior = valores[i]
    
    if valores[i] < menor:
        menor = valores[i]
    
    soma += valores[i]

media = soma / 5
    
print(f"Valores: {valores}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Média: {media}")