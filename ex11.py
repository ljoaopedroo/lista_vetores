valores = [0] * 5

for i in range(5):
    valores[i] = int(input("Digite um número: "))

maior = valores[0]
menor = valores[0]

for i in range(5):
    
    if valores[i] > maior:
        maior = valores[i]
        posiçao_maior = i
    
    if valores[i] < menor:
        menor = valores[i]
        posiçao_menor = i
print()
print(f"Posição do maior valor: {posiçao_maior}")
print(f"Posição do menor valor: {posiçao_menor}")