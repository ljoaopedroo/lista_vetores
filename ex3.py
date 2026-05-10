valores = [0] * 10
quadrado = [0] * 10

for i in range(10):
    numero = int(input("Digite um número: "))
    valores[i] = numero
for i in range(10):
    quadrado[i] = valores[i] * valores[i]

print(valores)
print(quadrado)