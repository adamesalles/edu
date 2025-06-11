---
title: Tutorial de Pandas sem SQL
hide:
  - navigation
---

# Tutorial de Pandas sem SQL

## Objetivos

- Carregar e inspecionar arquivos CSV com pandas  
- Limpar e normalizar datasets  
- Transformar e remodelar dados  
- Combinar dois conjuntos em um DataFrame unificado  
- Realizar análise exploratória básica com pandas  
- Responder a perguntas analíticas usando operações do pandas  

## Pré-requisitos

- Python 3.x instalado  
- Biblioteca pandas (`pip install pandas`)  
- Ambiente de desenvolvimento (Jupyter Notebook, VS Code, etc.)  
- Arquivos [`datasets/myanimelist.csv`](https://www.kaggle.com/datasets/marlesson/myanimelist-dataset-animes-profiles-reviews) e [`datasets/crunchyroll.csv`](https://www.kaggle.com/filipefilardi/crunchyroll-anime-ratings) disponíveis localmente.


---

## Configuração do ambiente 

```python
import pandas as pd
```

Certifique-se de que seu diretório de trabalho aponte para onde está a pasta datasets/.

---

## Carregamento e inspeção dos dados 

```python
mal = pd.read_csv('datasets/myanimelist.csv')
cr  = pd.read_csv('datasets/crunchyroll.csv')
```

Inspecione as primeiras linhas e as informações gerais:

```
mal.head()
mal.info()

cr.head()
cr.info()
```

---

## Limpeza dos dados

### MyAnimeList

- Remover duplicatas pelo título  
- Padronizar títulos para minúsculas  
- Eliminar caracteres não alfabéticos  

```python
mal_clean = mal.drop_duplicates(subset='title').copy()
mal_clean['title'] = (
    mal_clean['title']
    .str.lower()
    .str.replace(r'[^a-z\s]', '', regex=True)
)
```

### Crunchyroll

- Renomear `anime` → `title`  
- Padronizar títulos para minúsculas  
- Selecionar colunas relevantes  

```python
cr_clean = (
    cr
    .rename(columns={'anime': 'title', 'rate': 'rate'})
    .copy()
)
cr_clean['title'] = (
    cr_clean['title']
    .str.lower()
    .str.replace(r'[^a-z\s]', '', regex=True)
)
```

---

## Transformação dos dados

### Adicionar identificador da fonte

```python
mal_clean['source'] = 'MyAnimeList'
cr_clean['source'] = 'Crunchyroll'
```

### Selecionar e alinhar colunas para união

```python
mal_sel = mal_clean[['title', 'episodes', 'members', 'popularity', 'ranked', 'source']]
cr_sel  = cr_clean[['title', 'episodes', 'votes', 'votes_weight', 'rate', 'source']]
```

---

## Combinação e exploração dos dados

### Unir os DataFrames

```python
merged_df = pd.concat([mal_sel, cr_sel], ignore_index=True)
```

### Análise exploratória básica

```python
merged_df.head()
merged_df.describe(include='all')
```

---

## Perguntas

Utilize o DataFrame `merged_df` para responder:

### 1. Qual anime possui o maior número de membros no MyAnimeList?

??? success "Resposta"
    ```python
    merged_df[merged_df['source'] == 'MyAnimeList'] \
     .sort_values('members', ascending=False) \
     .head(1)['title']
    ```

### 2. Qual anime apresenta a maior avaliação média no Crunchyroll?

??? success "Resposta"
    ```python
    merged_df[merged_df['source'] == 'Crunchyroll'] \
     .sort_values('rate', ascending=False) \
     .head(1)['title']
    ```

### 3. Qual anime tem o maior número de episódios?

??? success "Resposta"
    ```python
    merged_df.sort_values('episodes', ascending=False) \
     .head(1)['title']
    ```

### 4. Qual o top 3 animes mais populares por ano no MyAnimeList?

??? success "Resposta"
    ```python
    mal_clean['start_date'] = pd.to_datetime(
    mal_clean['aired'].str.split(' to ').str[0],
    format='%b %d, %Y',
    errors='coerce'
    )
    mal_clean['year'] = mal_clean['start_date'].dt.year

    top3_pop_per_year = (
        mal_clean
        .sort_values(['year', 'popularity'])
        .groupby('year')
        .head(3)
        [['year', 'title', 'popularity']]
        .reset_index(drop=True)
    )
    ```