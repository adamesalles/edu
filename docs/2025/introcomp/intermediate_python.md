---
title: Python Intermediário
---

# Python Intermediário

Este material apresenta conceitos de nível intermediário em Python, seguidos de três exercícios práticos. Confira o código trabalhado na aula [de (21/05) aqui](https://github.com/adamesalles/edu/blob/main/resources/2025/introcomp/21-05/chamada.py) e em [(28/05) aqui](https://github.com/adamesalles/edu/blob/main/resources/2025/introcomp/21-05/chamada.py).

---

## Compreensões de listas (list comprehensions)

```python
quadrados = [x**2 for x in range(10) if x % 2 == 0]
```

---

## Expressões lambda e funções de ordem superior

```python
# Lambda
soma = lambda x, y: x + y
print(soma(3, 4))

# Funções de ordem superior
valores = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, valores))
dobros = list(map(lambda x: x * 2, valores))
```

---

## Manipulação de arquivos

```python
# Escrita
with open("exemplo.txt", "w") as f:
    f.write("Linha 1\nLinha 2\n")

# Leitura
with open("exemplo.txt", "r") as f:
    conteudo = f.readlines()
```

---

## Módulos e pacotes

```python
# Importando módulos internos
import os
import random

print(random.choice(["maçã", "banana", "uva"]))
```

---

## Tratamento de exceções

```python
try:
    x = int(input("Digite um número: "))
    print(10 / x)
except ValueError:
    print("Você não digitou um número.")
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")
finally:
    print("Fim da execução.")
```

---

## Exercício 1: Análise de Arquivo `.txt`

Escreva uma função que leia um arquivo de texto e retorne:

- O número de linhas
- O número de palavras
- A palavra mais frequente (ignorando maiúsculas/minúsculas e pontuação)

Use o arquivo `shrek.txt` como base (lá das monitoiras de Bash)

---

## Exercício 2: Jogo da Forca

Implemente um jogo da forca simples com:

- Entrada de letras pelo usuário
- Contador de tentativas
- Exibição parcial da palavra conforme os acertos
- Encerramento quando o jogador acerta tudo ou esgota as tentativas

---

## Exercício 3: Gerador de Relatório CSV

Crie um programa que:

1. Leia um arquivo CSV com as colunas: `nome`, `nota1`, `nota2`, `nota3`
2. Calcule a média de cada aluno
3. Salve um novo arquivo `relatorio.csv` com: `nome`, `média`, `situação` (`Aprovado` se média ≥ 7)

Use o módulo `csv`.

---

## Dica

Use `time.time()` ou `datetime` para medir tempo de execução, se quiser cronometrar ou registrar logs.

---

## Gabaritos

### Exercício 1: Jogo da Forca

??? example "Gabarito"
    ```python
    import string
    from collections import Counter

    def analisar_arquivo(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        texto = " ".join(linhas).lower()
        texto = texto.translate(str.maketrans("", "", string.punctuation))
        palavras = texto.split()

        mais_comum = Counter(palavras).most_common(1)[0][0]

        return len(linhas), len(palavras), mais_comum

    # Exemplo de uso
    linhas, total_palavras, palavra_frequente = analisar_arquivo("shrek.txt")
    print(f"Linhas: {linhas}")
    print(f"Palavras: {total_palavras}")
    print(f"Palavra mais frequente: {palavra_frequente}")
    ```

---

### Exercício 2: Jogo da Forca

??? example "Gabarito"
    ```python
    def jogar_forca(palavra):
        palavra = palavra.lower()
        letras_certas = set()
        tentativas = 6
        letras_erradas = set()

        while tentativas > 0:
            exibido = [letra if letra in letras_certas else "_" for letra in palavra]
            print(" ".join(exibido))

            if "_" not in exibido:
                print("Parabéns, você venceu!")
                return

            tentativa = input("Digite uma letra: ").lower()

            if tentativa in letras_certas or tentativa in letras_erradas:
                print("Letra já usada.")
                continue

            if tentativa in palavra:
                letras_certas.add(tentativa)
            else:
                letras_erradas.add(tentativa)
                tentativas -= 1
                print(f"Errado! Tentativas restantes: {tentativas}")

        print(f"Você perdeu! A palavra era: {palavra}")
    ```

    Desafio: carregar de um csv as palavras com dicas e amostrar uniformemente delas. 

    Acho legal de comentar que esse exercício lembra minha A1 de introdução à computação (de 2021): [https://github.com/adamesalles/forcaASCII](https://github.com/adamesalles/forcaASCII)

---

## Exercício 3: Gerador de Relatório CSV

??? example "Gabarito"
    ```python
    import csv

    def gerar_relatorio(entrada, saida):
        with open(entrada, "r", newline='', encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            alunos = []

            for row in reader:
                notas = [float(row["nota1"]), float(row["nota2"]), float(row["nota3"])]
                media = sum(notas) / len(notas)
                situacao = "Aprovado" if media >= 7 else "Reprovado"
                alunos.append({"nome": row["nome"], "media": round(media, 2), "situacao": situacao})

        with open(saida, "w", newline='', encoding="utf-8") as outfile:
            fieldnames = ["nome", "media", "situacao"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(alunos)

    # Exemplo de uso
    gerar_relatorio("notas.csv", "relatorio.csv")
    ```