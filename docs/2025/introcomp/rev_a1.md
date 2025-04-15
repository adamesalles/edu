---
hide:
  - navigation
---

# Regex, Grep, Sed, Awk, Find — Guia Prático com Roteiros de Filme

!!! note "Sobre este tutorial"
    Este guia é baseado no [Grymoire UNIX tutorials](https://www.grymoire.com/Unix/) e exemplificado com roteiros de filmes.

## 1. Introdução

Vamos explorar ferramentas poderosas para processamento de texto no Unix:

- **regex**: expressões regulares
- **grep**: busca por padrões
- **sed**: edição de fluxos de texto
- **awk**: processamento orientado a campos
- **find**: busca de arquivos no sistema

Usaremos dois arquivos como base:

```bash
assets/shrek.txt
assets/bee_movie.txt
```

### Preparação do ambiente

```bash
mkdir -p src/assets
cd src/assets
wget https://raw.githubusercontent.com/adamesalles/edu/refs/heads/main/resources/2025/introcomp/09-04/shrek.txt
wget https://raw.githubusercontent.com/adamesalles/edu/refs/heads/main/resources/2025/introcomp/09-04/bee_movie.txt
cd ..
```

!!! tip "Dica"
    Você pode usar `curl -O URL` no lugar do `wget`, se preferir.

### Criando um script executável

1. Crie um novo arquivo chamado `analisar.sh`:

```bash
touch analisar.sh
```

2. Edite-o com seu editor favorito (ex: `nano`, `vim`, `code`) e adicione:

```bash
#!/bin/bash
cd assets
ls -lh
```

3. Torne-o executável:

```bash
chmod +x analisar.sh
```

4. Execute-o:

```bash
./analisar.sh
```

---

## 2. grep

```bash
grep 'princess' assets/shrek.txt
cat assets/bee_movie.txt | grep -wi 'buzz' | wc -w
```

!!! note "Flags úteis"
    - `-i`: ignora maiúsculas/minúsculas
    - `-E`: ativa regex estendida
    - `-r`: busca recursiva
    - `-A1`, `-B1`: linhas após/antes

---

## 3. Expressões Regulares (Regex)

!!! tip "Dica"
    Regex é uma linguagem para busca e manipulação de strings baseada em padrões.

Exemplos:

```bash
grep 'Donkey' assets/shrek.txt
grep -E 'D[o0]nkey|Bee' assets/*.txt
grep -i '^b' assets/bee_movie.txt
cat assets/shrek.txt | grep -i 'ogre'
```

Referências:

  - [Regex101](https://regex101.com/) - Teste suas expressões regulares
  - [Regexr](https://regexr.com/) - Aprenda regex com exemplos


## 4. sed

```bash
sed 's/Shrek/OGRE/g' assets/shrek.txt
```

!!! warning "Cuidado"
    `sed -i` altera arquivos diretamente. Use com atenção!

!!! note "Nota"
    Você pode usar o `|` para encadear comandos `sed`.
    ```bash
    cat assets/shrek.txt | sed 's/friend/enemy/g' | grep 'enemy'
    sed 's/Shrek/OGRE/g' assets/shrek.txt | grep 'OGRE'
    ```


Referências:

  - [Sed One-Liners](https://www.grymoire.com/Unix/Sed.html#uh-1) - Exemplos práticos

---

## 5. awk

```bash
awk '/Buzz/{print $0}' assets/bee_movie.txt
awk '{print $1, $NF}' assets/shrek.txt
```

!!! tip "Dica"
    Ideal para extração de colunas e análise por linha

---

## 6. find

```bash
find assets -type f -name '*.txt'
find . -mtime -1 -type f -exec grep 'Fiona' {} \;
```

!!! note "Nota"
    `find` é útil para aplicar comandos como `grep` em arquivos localizados

---

## 7. ls

Listagens básicas:

```bash
ls
ls -l
ls -lh assets/
ls -lhS assets/
ls -lhaS assets/
```

!!! tip
    Combine `ls` com `grep`, `head`, `tail`, e `sort` para análises mais poderosas

---

## 8. wc

```bash
wc assets/shrek.txt
cat assets/bee_movie.txt | wc -l
cat assets/shrek.txt | grep 'love' | wc -w
```

---

## 9. sort

```bash
sort assets/bee_movie.txt | head -10
grep -i "Shrek" assets/shrek.txt | sort -r | tail -10
cat assets/bee_movie.txt | grep 'bee' | sort | uniq -c | sort -nr | head
```

---

## Exercícios

### 1. Encontre todas as linhas com `{Shouting}`, `{Roaring}`, `{Laugh}` ou `{Laughing}` no script do Shrek.

??? example "Gabarito"
    ```bash
    grep -E '\{(Shouting|Roaring|Laugh|Laughing)\}' assets/shrek.txt
    ```

### 2. Use `grep` com regex para encontrar linhas que começam com a letra `T`.

??? example "Gabarito"
    ```bash
    grep '^T' assets/*.txt
    ```

### 3. Use `sed` para substituir todas as ocorrências de “Bee” por “Wasp” no arquivo do Bee Movie (sem sobrescrever o original).

??? example "Gabarito"
    ```bash
    sed 's/Bee/Wasp/g' assets/bee_movie.txt > assets/bee_movie_wasp.txt
    ```

### 4. Use `awk` para extrair apenas as duas primeiras palavras de cada linha.

??? example "Gabarito"
    ```bash
    awk '{print $1, $2}' assets/*.txt
    ```

### 5. Liste os arquivos `.txt` em `assets/`, ordenados por tamanho decrescente.

??? example "Gabarito"
    ```bash
    ls -lhS assets/*.txt
    ```

### 6. Use `grep` para contar quantas vezes a palavra “love” aparece em cada roteiro.

??? example "Gabarito"
    ```bash
    grep -oi 'love' assets/shrek.txt | wc -l
    grep -oi 'love' assets/bee_movie.txt | wc -l
    ```

### 7. Use `head` para extrair as duas primeiras linhas do roteiro e mostrar o título e o ano.

??? example "Gabarito"
    ```bash
    head -n2 assets/shrek.txt
    head -n2 assets/bee_movie.txt
    ```

### 8. Crie um script chamado `resumo.sh` que:

  - Extraia o nome do filme da linha `Title:`
  - Conte quantidade de linhas, palavras e caracteres
  - Extraia o ano da linha `Publication:`

??? example "Gabarito"
    ```bash
    #!/bin/bash
    echo "Nome do filme: $(grep -m1 'Title' \"$1\" | awk -F'Title: ' '{print $2}')"
    echo "Quantidade de linhas: $(cat \"$1\" | wc -l)"
    echo "Quantidade de palavras: $(cat \"$1\" | wc -w)"
    echo "Quantidade de caracteres: $(cat \"$1\" | wc -c)"
    echo "Ano de lançamento: $(grep -m1 'Publication' \"$1\" | awk -F'Publication: ' '{print $2}')"
    ```
---
