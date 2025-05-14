numero = 2  # Começamos com o primeiro número par
soma = 0

while numero <= 50:
    soma += numero
    numero += 2  # Passa para o próximo número par

print(f"A soma de todos os números pares entre 1 e 50 é {soma}.")
