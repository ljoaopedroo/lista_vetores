contador = 0
valores = [5,8,98,76,54,23,12,11,2,8]

for i in range(10):
    if valores[i] % 2 == 0:
        contador += 1
print(f"No vetor {valores} temos {contador} números pares")