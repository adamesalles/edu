import string
from collections import Counter
import pathlib

BASE = pathlib.Path(__file__).parent

def analisar_arquivo(nome_arquivo: str):
    with open(nome_arquivo, "r", encoding='utf-8') as f:
        linhas = f.readlines()
        
    texto = " ".join(linhas).lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    palavras = texto.split()
    
    mais_comum = Counter(palavras).most_common(10)
    print(mais_comum[0][0])
    
analisar_arquivo(BASE / "../09-04/shrek.txt")

# semana que vem mexer com sqlite e pandas