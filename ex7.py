valores = [0] * 10
posição_maior = 0

for i in range (10):
    valores[i] = int(input("Digite um número: "))
    
maior = valores[0]

for i in range(1, 10):
    if valores[i] > maior:
        maior = valores[i]
        posição_maior = i
print()
print(f"O vetor criado é: {valores}")
print(f"Maior elemento do vetor: {maior}")
print(f"Posição do maior elemento: {posição_maior}")