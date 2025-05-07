---
title: Próximos passos com LaTeX
hide:
  - navigation
---

# Próximos passos com $\LaTeX$

Este guia apresenta recursos mais avançados do LaTeX, úteis para matemática, apresentações, ilustrações, tabelas e formatação rica com pacotes como `tcolorbox` e `beamer`.

---

## Listas

### Lista não-enumerada (itemize)

```latex
\begin{itemize}
  \item Maçã
  \item Banana
  \item Laranja
\end{itemize}
```

### Lista enumerada (enumerate)

```latex
\begin{enumerate}
  \item Primeiro item
  \item Segundo item
  \item Terceiro item
\end{enumerate}
```

### Lista descritiva (description)

```latex
\begin{description}
  \item[HTML] Linguagem de marcação para web.
  \item[CSS] Folhas de estilo.
  \item[JavaScript] Linguagem de programação para interação.
\end{description}
```

### Lista aninhada

```latex
\begin{itemize}
  \item Frutas
    \begin{itemize}
      \item Maçã
      \item Uva
    \end{itemize}
  \item Legumes
    \begin{itemize}
      \item Cenoura
      \item Batata
    \end{itemize}
\end{itemize}
```

---

## Matemática Avançada

### Ambientes matemáticos

```latex
\begin{equation}
E = mc^2
\end{equation}

Recomendo o uso do pacote `physics` para fórmulas mais complexas.

\begin{align}
f(x) &= \int_{-\infty}^{\infty} e^{-x^2}\, \dd x \\
     &= \sqrt{\pi}
\end{align}
```

### Teoremas e demonstrações

```latex
\usepackage{amsthm}

\newtheorem{teo}{Teorema}

\begin{teo}[Pitágoras]
Seja um triângulo retângulo com catetos $a$, $b$ e hipotenusa $c$. Então:
$$
a^2 + b^2 = c^2
$$
\end{teo}
```

---

## Tabelas

```latex
\begin{tabular}{|c|c|c|}
\hline
Nome & Idade & Nota \\
\hline
Ana & 20 & 9.5 \\
Bruno & 22 & 8.7 \\
\hline
\end{tabular}
```

### Tabela com caption

O exemplo abaixo requer `\usepackage{booktabs}`.

```latex
\begin{table}[h]
  \centering
  \caption{Notas dos alunos}
  \begin{tabular}{l c}
  \toprule
  Nome & Nota \\
  \midrule
  Clara & 9.3 \\
  Daniel & 7.8 \\
  \bottomrule
  \end{tabular}
\end{table}
```


Recomendo o site [Tables Generator](https://www.tablesgenerator.com/) para criar tabelas complexas.

---

## Inserção de Figuras

```latex
\usepackage{graphicx}

\begin{figure}[h]
  \centering
  \includegraphics[width=0.5\textwidth]{exemplo.png}
  \caption{Exemplo de imagem}
  \label{fig:exemplo}
\end{figure}
```

---

## Caixas e Destaques com `tcolorbox`

```latex
\usepackage{tcolorbox}

\begin{tcolorbox}[colback=blue!5!white, colframe=blue!75!black, title=Resumo]
Este é um resumo importante destacado em uma caixa.
\end{tcolorbox}
```

Leia a documentação do `tcolorbox` em [tcolorbox](https://www.ctan.org/pkg/tcolorbox){:target="_blank"}.

---

## Apresentações com Beamer

### Estrutura básica

```latex
\documentclass{beamer}
\title{Minha Apresentação}
\author{Seu Nome}
\date{\today}

\begin{document}

\frame{\titlepage}

\begin{frame}{Introdução}
  Este é o conteúdo do primeiro slide.
\end{frame}

\end{document}
```
Encontre outros temas tradicionais em [deic.uab.cat](https://deic.uab.cat/~iblanes/beamer_gallery/){:target="_blank"}.

Experimente outros temas modernos disponíveis no Beamer neste [link](https://github.com/martinbjeldbak/ultimate-beamer-theme-list). Recomendo o tema `metropolis` inicialmente.

---

## Hyperlinks com `hyperref` e `hypersetup`

```latex
\usepackage{xcolor}
\usepackage[colorlinks=true, linkcolor=blue, urlcolor=magenta]{hyperref}
```

### Exemplo de uso

```latex
Veja o \href{https://www.overleaf.com}{Overleaf} para editar LaTeX online.

\tableofcontents
\section{Introdução}
\label{sec:intro}

Referência interna: veja a Seção~\ref{sec:intro}.
```

---

## Gráficos com TikZ e PGFPlots

### TikZ básico

```latex
\usepackage{tikz}

\begin{tikzpicture}
  \draw[->] (0,0) -- (2,0) node[right]{$x$};
  \draw[->] (0,0) -- (0,2) node[above]{$y$};
  \draw[blue, thick] (0,0) -- (1.5,1.5);
\end{tikzpicture}
```

### PGFPlots com função via gnuplot

```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.17}
\usepgfplotslibrary{external}
\usepgfplotslibrary{fillbetween}

\begin{tikzpicture}
\begin{axis}[
  title=Função Seno,
  xlabel=$x$, ylabel=$\sin(x)$,
  samples=100, domain=0:6.28,
  grid=major
]
\addplot[blue, thick] {sin(deg(x))};
\end{axis}
\end{tikzpicture}
```

---

## Referências e Citações

```latex
\usepackage{biblatex}
\addbibresource{referencias.bib}
\begin{document}
\cite{exemplo2023}
\printbibliography
\end{document}
```
### Exemplo de arquivo `.bib`

```bibtex
@article{exemplo2023,
  author = {Autor, A.},
  title = {Título do Artigo},
  journal = {Nome do Jornal},
  year = {2023},
  volume = {1},
  number = {1},
  pages = {1-10}
}
```
### Citação no texto

```latex
A pesquisa de \cite{exemplo2023} mostra que...
```

---

### Adicionando código-fonte

```latex
\usepackage{minted}
\setminted[python]{
    frame=lines,
    framesep=2mm,
    baselinestretch=1.2,
    bgcolor=gray!20,
    fontsize=\footnotesize,
    linenos
}
\begin{minted}{python}
def hello_world():
    print("Hello, World!")
hello_world()
\end{minted}
```

Você pode usar `\inputminted` para incluir arquivos de código diretamente.

```latex
\inputminted{python}{caminho/para/seu_arquivo.py}
```

Ou código em linha com `\mintinline`:

```latex
Teste \mintinline{python}{print("Hello, World!")}.
```

---

## Dicas Finais

- Use `\pause` para controlar a ordem de aparecimento dos elementos nos slides.
- Utilize o template da EMAp no [Overleaf](https://www.overleaf.com/latex/templates/emap-beamer-template/tzcwbhjddmrk){:target="_blank"}.
- Com `tcolorbox`, você pode criar caixas com equações, listas e código.
- Para importar imagens, preste atenção ao caminho e extensão do arquivo.
- Explore o pacote `tikz` para criar gráficos e diagramas diretamente no LaTeX.

