---
title: Introdução ao LaTeX
hide:
  - navigation
---

# Introdução ao $\LaTeX$

Este guia apresenta uma introdução prática ao uso do LaTeX por meio do Overleaf, com base no documento construído em monitoria.


## Instruções para o uso do Overleaf

1. Crie uma conta em <https://www.overleaf.com/>{:target="_blank"};
2. Agora logado, crie um **"Blank Project"**, ao clicar no botão **"New Project"**.
3. Produza seu documento! Utilize `Ctrl+S` ou `Cmd+S` para processar o documento.

---

## Estrutura Básica do Documento

```latex
\documentclass{article}
```

Define o tipo do documento. Para a maioria dos textos acadêmicos simples, usamos `article`.

Conheça os outros em [Overleaf](https://tex.stackexchange.com/questions/782/what-are-the-available-documentclass-types-and-their-uses){:target="_blank"}.

---

## Pacotes Utilizados

```latex
\usepackage[utf8]{inputenc}     % Codificação do texto
\usepackage[T1]{fontenc}        % Codificação da fonte
\usepackage[brazil]{babel}      % Tradução e hifenização para português
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}             % Pacotes da American Mathematical Society
\usepackage{xcolor}             % Controle de cores
\usepackage{graphicx}           % Inclusão de imagens
\usepackage{lipsum}             % Geração de texto fictício
```

---

## Título e Autoria

```latex
\title{Monitoria do dia 30 de abril}
\author{Turma\thanks{cd2025@gmail.com}} % Thanks para rodapé
\date{\today}
```

Define o título, autor e data do documento.

Esses comandos devem ser colocados antes do `\begin{document}`, no que chamamos de preâmbulo.
O `\thanks` gera um rodapé com a informação que você quiser.
O `\today` gera a data atual.

---

## Ambientes e Comandos

### `\maketitle`

Gera a capa com título, autor e data.

### `\begin{abstract}`

Resumo do documento.

### `\tableofcontents`

Gera sumário automático baseado nas seções.

---

## 💬 Texto e Parágrafos

### Comentários

```latex
% Comentários são ignorados pelo compilador
```

### Quebra de linha

```latex
Primeira linha \\
Segunda linha
```

### Novo parágrafo

Basta deixar uma linha em branco entre os parágrafos.

---

## Estilos de Fonte

```latex
\textbf{negrito}
\textit{itálico}
\underline{sublinhado}
\texttt{monoespaçado}
\textsf{sem serifa}
\textsc{versalete}
\textsl{inclinada}
\emph{ênfase}
```

### Combinações e ambientes

```latex
{
  \bfseries
  \color{magenta}
  Texto colorido e em negrito
}
```

---

## Tamanhos de Fonte

```latex
\tiny, \scriptsize, \footnotesize, \small, \normalsize, \large, \Large, \LARGE, \huge, \Huge
```

---

## Ambiente Matemático

### No meio do texto (inline)

```latex
$x^2 = 1$
```

### Centralizado (display)

```latex
$$x^2 = 1$$
```

Dê preferência ao ambiente `align` para equações mais complexas.

```latex
\begin{align}
  x^2 + y^2 &= z^2 \\
  \int_a^b x\ \mathrm{d}x &= \frac{1}{2}x^2
\end{align}
```

---

## Símbolos e Expressões

```latex
\alpha, \beta, \gamma, \Gamma

\int_a^b x\ \mathrm{d}x

\frac{a}{b}, \sum_{i=1}^n, \lim_{x\to\infty}

\exp\left\{\int_a^b x\ \mathrm{d}x\right\}, \sin(\theta)
```

Explore mais símbolos em [Detexify](http://detexify.kirelabs.org/){:target="_blank"}.

---

## Rodapés

```latex
\footnote{Esse é um rodapé enumerado automaticamente.}
```

---

## Seções

```latex
\section{}, \subsection{}, \subsubsection{}, \paragraph{}
```

Estruturam o documento. Usadas junto com `\tableofcontents` para criar sumário.


