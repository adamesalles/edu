---
title: Tutorial de Pandas e SQLite
hide:
  - navigation
---

# Tutorial de Pandas e SQLite

Este tutorial interativo em Python utiliza o **marimo**, um ambiente moderno de notebooks.

Neste notebook, você aprenderá a:
- Criar e consultar um banco de dados SQLite com `sqlite3`
- Carregar, explorar e manipular dados usando `pandas`
- Utilizar as células do `marimo` para tornar a experiência interativa

---

**Nota**: Este ambiente é semelhante ao Jupyter Notebook, outra ferramenta popular. No entanto, o `marimo` oferece melhor estrutura, reatividade e controle de versão.

Após instalar o marimo, basta digitar `marimo edit seu_arquivo.py` no terminal para abrir o notebook no navegador. Leia mais sobre o marimo [aqui](https://docs.marimo.io).

## Configuração Inicial

```python
import sqlite3
import pandas as pd
import seaborn as sns
```

## Carregando o Conjunto de Dados Titanic

Utilizaremos o conjunto de dados Titanic, disponível na biblioteca `seaborn`.

```python
df_titanic = sns.load_dataset('titanic')
df_titanic.head()
```

## Criando um Banco de Dados SQLite em Memória

```python
conn = sqlite3.connect(":memory:")
df_titanic.to_sql("passengers", conn, index=False, if_exists="replace")
```

## Consultando Dados com SQL

```python
query = "SELECT * FROM passengers LIMIT 5;"
df_query = pd.read_sql_query(query, conn)
df_query
```

## Análise Exploratória com Pandas

### Estatísticas Descritivas

```python
df_titanic.describe(include='all')
```

### Contagem de Sobreviventes por Classe

```python
df_titanic.groupby('class')['survived'].sum()
```

## Operações Avançadas com Pandas

### Merge (Junção) de DataFrames

```python
df_info = pd.DataFrame({
    'class': ['First', 'Second', 'Third'],
    'description': ['Primeira Classe', 'Segunda Classe', 'Terceira Classe']
})

df_merged = pd.merge(df_titanic, df_info, on='class', how='left')
df_merged[['class', 'description']].drop_duplicates()
```

### Filtrando Dados

```python
df_titanic[df_titanic['age'] < 18]
```

### Criando Novas Colunas

```python
df_titanic['is_minor'] = df_titanic['age'] < 18
df_titanic[['age', 'is_minor']].head()
```

## Salvando e Carregando DataFrames com SQLite

```python
df_titanic.to_sql("titanic_backup", conn, index=False, if_exists="replace")
df_loaded = pd.read_sql("SELECT * FROM titanic_backup", conn)
df_loaded.head()
```

---


### Exercício 1: Contagem de passageiros por sexo e sobrevivência

Escreva uma consulta SQL para contar o número de passageiros por sexo e status de sobrevivência (`survived`).

??? success "Resposta"
    ```python
    query = """
    SELECT sex, survived, COUNT(*) as total
    FROM passengers
    GROUP BY sex, survived;
    """
    df_result = pd.read_sql_query(query, conn)
    df_result
    ```

---

### Exercício 2: Passageiros mais jovens por classe

Utilize pandas para encontrar o passageiro mais jovem em cada classe (class), exibindo também seu nome, idade e sexo.

??? success "Resposta"
    ```python
    df_titanic.loc[df_titanic.groupby("class")["age"].idxmin(), ["class", "age", "sex", "who"]]
    ```

---

### Exercício 3: Porcentagem de menores de idade por classe

Crie uma nova coluna is_minor e calcule a porcentagem de menores de idade (idade < 18) por classe utilizando groupby.

??? success "Resposta"
    ```python
    df_titanic['is_minor'] = df_titanic['age'] < 18
    percent_minors = df_titanic.groupby('class')['is_minor'].mean() * 100
    ```

---

## Extras

- Faça [esse tutorial de SQL](https://github.com/adamesalles/edu/blob/main/resources/2025/introcomp/assets/sqlite-tutorial.sql);
- Veja o [um exemplo de arquivo marimo](https://github.com/adamesalles/edu/blob/main/resources/2025/introcomp/04-06/pandas_and_sqlite.py).