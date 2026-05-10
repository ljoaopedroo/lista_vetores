valores = [0] * 10
count = 0
soma = 0

for i in range(10):
    valores[i] = int(input("Digite um número: "))

for i in range (10):
    if valores[i] < 0:
        count += 1
    
    else:
        soma += valores[i]

print()
print(f"Quantidade de números negativos: {count}")
print(f"Soma dos números positivos: {soma}")