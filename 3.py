# Exercício 1: Soma dos Valores do Dicionário
# Escreva um programa que some todos os valores de um dicionário cujas chaves são strings e os valores são inteiros.
# Dica: Use um loop `for`.
# Exemplo de entrada: {'a': 10, 'b': 20, 'c': 30}
# Exemplo de saída: 60
'''dic = {'a': 10, 'b': 20, 'c': 30}
tudo = 0
for chave, valor in dic.items():
    
    if isinstance(valor, int):
        tudo += valor  


print(f"A soma dos valores do dicionário é: {tudo}")
'''





# Exercício 2: Contar Ocorrências de Caracteres
# Escreva um programa que conte as ocorrências de cada caractere em uma string usando um dicionário.
# Dica: Use um loop `for`.
# Exemplo de entrada: "banana"
# Exemplo de saída: {'b': 1, 'a': 3, 'n': 2}
'''
def contar_ocorrencias(linha):
    contagem = {}
    
    for caractere in linha:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    
    return contagem
linha = "banana"
ocorrencias = contar_ocorrencias(linha)
print(f"Ocorrências de caracteres em '{linha}': {ocorrencias}")
'''

# Exercício 3: Filtrar Números Pares
# Escreva um programa que filtre e armazene apenas os números pares de um dicionário cujas chaves são strings e os valores são inteiros.
# Dica: Use um loop `for` e o operador `%`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: {'b': 2, 'd': 4}

# Exercício 4: Produto dos Valores do Dicionário
# Escreva um programa que calcule o produto de todos os valores de um dicionário cujas chaves são strings e os valores são inteiros.
# Dica: Use um loop `for`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: 24

# Exercício 5: Valores Acima de um Limite
# Escreva um programa que armazene em uma lista todos os valores de um dicionário que sejam maiores que um certo limite.
# Dica: Use um loop `for` e uma estrutura `if`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}, limite = 2
# Exemplo de saída: [3, 4]

# Exercício 6: Soma dos Valores com `while`
# Escreva um programa que some todos os valores de um dicionário cujas chaves são strings e os valores são inteiros, utilizando um loop `while`.
# Dica: Use `iter()` e `next()` para iterar sobre os valores do dicionário.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: 10

# Exercício 7: Valores Acima da Média
# Escreva um programa que encontre todos os valores de um dicionário que estejam acima da média de todos os valores.
# Dica: Use um loop `for` para calcular a média e outro loop `for` para encontrar os valores acima da média.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: [3, 4]

# Exercício 8: Contagem de Palavras
# Escreva um programa que conte a frequência de cada palavra em uma lista de strings e armazene os resultados em um dicionário.
# Dica: Use um loop `for`.
# Exemplo de entrada: ["apple", "banana", "apple", "orange", "banana", "apple"]
# Exemplo de saída: {'apple': 3, 'banana': 2, 'orange': 1}

# Exercício 9: Atualizar Valores do Dicionário
# Escreva um programa que percorra um dicionário e atualize seus valores, adicionando 10 a cada valor.
# Dica: Use um loop `for`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: {'a': 11, 'b': 12, 'c': 13, 'd': 14}

# Exercício 10: Remover Chaves com Valores Negativos
# Escreva um programa que remova todas as chaves de um dicionário cujos valores sejam negativos.
# Dica: Use um loop `for` e uma estrutura `if`.
# Exemplo de entrada: {'a': -1, 'b': 2, 'c': -3, 'd': 4}
# Exemplo de saída: {'b': 2, 'd': 4}

# Exercício 11: Interseção de Dois Dicionários
# Escreva um programa que encontre as chaves comuns em dois dicionários e armazene essas chaves e seus valores em um novo dicionário.
# Dica: Use loops `for` e uma estrutura `if`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 4, 'd': 5}
# Exemplo de saída: {'b': 2, 'c': 3}

# Exercício 12: Contagem de Caracteres em Palavras
# Escreva um programa que conte a frequência de cada caractere em uma lista de palavras e armazene os resultados em um dicionário.
# Dica: Use um loop `for` aninhado.
# Exemplo de entrada: ["apple", "banana"]
# Exemplo de saída: {'a': 4, 'p': 2, 'l': 1, 'e': 1, 'b': 1, 'n': 2}

# Exercício 13: Entrada de Usuário até 'Q'
# Escreva um programa que peça ao usuário para inserir valores em um dicionário até que ele digite 'Q' para sair.
# Exemplo de entrada: 
# (Usuário) a 1
# (Usuário) b 2
# (Usuário) Q
# Exemplo de saída: {'a': 1, 'b': 2}

# Exercício 15: Calculadora Simples
# Escreva um programa que apresente um menu interativo para o usuário realizar operações matemáticas básicas (soma, subtração, multiplicação e divisão) até que ele escolha sair.
# Exemplo de entrada: 
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# 5. Sair
# (Usuário escolhe 1) 4 5
# Exemplo de saída: 9


###################
##### DESAFIO #####
###################
# Exercício 16: Jogo da Forca
# Escreva um jogo da forca em que o usuário deve adivinhar uma palavra secreta com vidas infinitas até o usuário acertar a palavra.
