# import pathlib
from pathlib import Path
import random
from copy import deepcopy
from typing import List
from icecream import ic
import math
# numeros = [numero for numero in range(13)]

nomes = ['Eduardo', 'Nina', 'Yuri', 'Trajano']
BASE = Path(__file__).parent
print(BASE)

# print("Meus números:", numeros)
# print("Números pares:", list(filter(lambda x: x % 2 == 0, numeros)))
# print("Meus números ao quadrado:", list(map(lambda x: x**2, numeros)))

# print("Nomes grandes:", list(filter(lambda x: len(x) > 4, nomes)))
# print("Nomes pequenos:", list(filter(lambda x: len(x) <= 4, nomes)))
# print("Nomes pequenos (map):", list(map(lambda x: len(x) <= 4, nomes)))

# print("PARE DE GRITAR!!!", list(map(lambda x: x.upper() + "!", nomes)))

# with open(BASE / '../09-04/shrek.txt',
#           'r', encoding='utf-8') as f:
#     conteudo = f.readlines()
    
# p = random.random()
# tamanho = len(nomes)

# print(nomes)
# print(p*tamanho)
# print(nomes[math.floor(p*tamanho)])


# try:
#     x = int(input("Insira um número: "))
#     print(10 / x)
# except ValueError:
#     print("Você não digitou um número!")
# except ZeroDivisionError:
#     print("Ainda não é possível dividir por zero, experimente a matemática 3.")
# except KeyboardInterrupt:
#     print("Tchau, tchau!")
# except Exception as e:
#     print("Erro desconhecido:", e)


def chamada(pessoas: List[List[str]], pesos: List[float]):
    """Retorna um gerador que retorna os nomes das pessoas na ordem de chamada."""
    grupos = deepcopy(pessoas)

    while any(grupos):
        ativos = [(i, g) for i, g in enumerate(grupos) if g]
        # print(ativos)
        indices, _ = zip(*ativos)
        pesos_ativos = [pesos[i] for i in indices]
        soma = sum(pesos_ativos)
        norm = [p / soma for p in pesos_ativos]

        escolha = random.choices(indices, weights=norm)[0]
        yield grupos[escolha].pop(0)

# Exemplo de uso
minhas_pessoas = [
    ['Eduardo', 'Nina'],     # alta prioridade (50%)
    ['Yuri', 'Pedro'],       # média (30%)
    ['Luis', 'João']         # baixa (20%)
]

meus_pesos = [.4, 0.25, 0.35]

# minha_chamada = chamada(minhas_pessoas, meus_pesos)

# for pessoa in minha_chamada:
#     print("Próximo:", pessoa)
    
my_dict = {}
for grupo in minhas_pessoas:
    for pessoa in grupo:
        my_dict[pessoa] = []

M = 1000
for _ in range(M):
    minha_chamada = chamada(minhas_pessoas, meus_pesos)
    for i, pessoa in enumerate(minha_chamada):
        my_dict[pessoa].append(i)

for pessoa, ordem in my_dict.items():
    print("Pessoa: ", pessoa)
    for pos in range(6):
        print(f"Quantidade de vezes em {pos + 1}: ", ordem.count(pos)/M)

# print(next(minha_chamada), next(minha_chamada))