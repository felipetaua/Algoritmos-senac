# Gasolina = R$5.49
# Alcool = R$3.69

print("Hello Word!")

# entrada
precoAlcool = float(input("Insira o valor do alcool:"))
precoGasolina = float(input("Insira o valor da gasolina"))

# processamento
resultado = precoAlcool / precoGasolina

# saida
print(resultado)

# se resultado for maior que 0.7 abastece com gasolina, caso contrario, com alcool
if resultado > 0.7:
    print("Abasteça com gasolina!")
else:
    print("Abasteça com álcool!")

