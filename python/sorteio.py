import random

#forma 1
numeroAleatorio = random.randint(0,1000)
print(f"O número sorteado foi {numeroAleatorio}")


#forma 2
def sortear(minimo, maximo):
    return random.randint(minimo, maximo)

minimo = 1
maximo = 10
sorteado = sortear(minimo, maximo)

num = int(input("insira qualquer número: "))

while True:
    if num > 10 or num < 0:
        print("O númemero tem que ser entre 1 e 10")
        num = int(input("insira qualquer número: "))
    
    if sorteado < num:
        print("O número sorteado é menor")
        num = int(input("insira qualquer número: "))
    elif sorteado > num:
        print("o número sorteado é maior")
        num = int(input("insira qualquer número: "))
    elif sorteado == num:
        print("Acertou! Parabens!")
        break