# Introdução ao Python

Este material apresenta os fundamentos da linguagem Python. Confira o código trabalhado em aula [aqui](https://github.com/adamesalles/edu/blob/main/resources/2025/introcomp/14-05/first.py).

---

## História e características do Python

- Criado por Guido van Rossum no início dos anos 1990.
- É uma linguagem de programação de alto nível, interpretada e de propósito geral.
- Possui sintaxe clara, objetiva e fácil de aprender.
- Suporta múltiplos paradigmas: imperativo, orientado a objetos, funcional.

---

## Primeiro programa

```python
print("Olá, mundo!")
```

---

## Variáveis e tipos básicos

```python
# Inteiro
x = 10

# Ponto flutuante
pi = 3.14

# String
nome = "Eduardo"

# Booleano
ativo = True
```

---

## Operadores básicos

```python
# Aritméticos
a + b
a - b
a * b
a / b
a ** b  # Potência
a % b   # Módulo

# Comparação
a == b
a != b
a > b
a <= b

# Lógicos
and, or, not
```

---

## Estruturas de controle

### Condicional

```python
if x > 0:
    print("Positivo")
elif x == 0:
    print("Zero")
else:
    print("Negativo")
```

### Laço for

```python
for i in range(5):
    print(i)
```

### Laço while

```python
n = 5
while n > 0:
    print(n)
    n -= 1
```

---

## Funções

```python
def greet(nome):
    return f"Olá, {nome}!"

print(greet("Python"))
```

---

## Listas, tuplas e dicionários

```python
# Lista
frutas = ["maçã", "banana", "laranja"]

# Tupla
cores = ("azul", "verde", "vermelho")

# Dicionário
pessoa = {"nome": "Eduardo", "idade": 22}
```

---

## Importação de módulos

```python
import math

print(math.sqrt(16))
```

---

## Boas práticas

- Use indentação de 4 espaços.
- Nomeie variáveis de forma clara.
- Utilize comentários para explicar o código.
- Seguir a PEP 8 (guia de estilo oficial do Python).

