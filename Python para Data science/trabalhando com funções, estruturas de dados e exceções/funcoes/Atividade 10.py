from os import replace
'''
Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP).
Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e
filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista.
Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.
'''

frase = 'Aprender Python, aqui na Alura é muito bom'
frase_separada = frase.split()

lista_final = list(filter(lambda palavra: len(palavra) >=5, frase_separada))
print(lista_final)