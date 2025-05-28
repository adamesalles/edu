import sys


def imc(altura: float,
        peso: float) -> float:
    return peso/(altura**2)

def calculate_imc():
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    print(f"O seu imc é {imc(altura, peso)}")
    return None

counter = 0

while True:
    entry = input("Digite o comando: ")
    match entry:
        case 'q':
            break
        case 'imc':
            calculate_imc()
        case 'greet':
            name = input('Qual o seu nome? ')
            print(f"Olá, {name}!")
        case _:
            counter += 1
            if counter > 3:
                print("Vou explodir o seu computador!!!!!!")
                counter = 0
            else:
                print("Digite um comando!")
