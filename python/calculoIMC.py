#entrada
peso = float(input("Insira o peso em Kg: "))
altura = float(input("Insira a altura em m: "))

#processamento
imc = peso / (altura * altura)

#saida
print(f"o seu IMC é: {imc}")

if imc < 18.5:
    print("Magreza - 0")
elif imc < 24.9:
    print("Normal - 0")
elif imc < 19.9:
    print("Sobrepeso - I")
elif imc < 39.9:
    print("Obsesidade - II")
else:
    print("Obesidade Grave - III")
