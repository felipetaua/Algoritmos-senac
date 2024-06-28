import random
import os
import sys
import time 
import webbrowser

def abrir_janelas():
    urls = [
        "https:www.google.com",
        "https:www.google.com",
        "https:www.google.com",
        "https:www.google.com",
        "https:www.google.com",
        "https:www.google.com",
    ]
    for i in range(5):
        url = random.choice(urls)
        webbrowser.open(url)

def evento_aleatorio():
    opcoes = 6
    escolhas_indesejadas = random.randint(1, opcoes)

    try:
        escolha = int(input(f"escolha um número entre 1 e {opcoes}"))
        if escolha < 1 or escolha > opcoes:
            raise ValueError("Número fora do intervalo")
        
    except ValueError as e:
        print(f"entrada invalida: {e}. Tente de novo!")
        evento_aleatorio()

    if escolha == escolhas_indesejadas:
        print('Ops, Ja era, você perdeu!')
        abrir_janelas()
        time.sleep(5)
        
        #para windows
        if sys.platform == 'win32':
            os.system("shutdown /s /t 1")
        #para linux
        elif sys.platform == 'linux' or sys.plataform == 'linux2':
            os.system("shutdown now")
        #para mac
        elif sys.platform == 'darwin':
            os.system("shutdown -h now")
        sys.exit()

    else:
        print('Você está seguro por enquanto!')
        evento_aleatorio()

evento_aleatorio()