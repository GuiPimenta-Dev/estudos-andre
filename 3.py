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
'''
def filtrar_numeros_pares(dicionario):
    resultado = {}
    for chave, valor in dicionario.items():
        if valor % 2 == 0:
            resultado[chave] = valor
    return resultado

entrada = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
saida = filtrar_numeros_pares(entrada)

print(f'Entrada: {entrada}')
print(f'Saída (números pares): {saida}')

'''


# Exercício 4: Produto dos Valores do Dicionário
# Escreva um programa que calcule o produto de todos os valores de um dicionário cujas chaves são strings e os valores são inteiros.
# Dica: Use um loop `for`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: 24
'''
def produto_valores(dicionario):
    produto = 1
    for valor in dicionario.values():
        produto *= valor
    return produto

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
resultado = produto_valores(dicionario)
print(f"O produto dos valores do dicionário {dicionario} é: {resultado}")
'''
# Exercício 5: Valores Acima de um Limite
# Escreva um programa que armazene em uma lista todos os valores de um dicionário que sejam maiores que um certo limite.
# Dica: Use um loop `for` e uma estrutura `if`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}, limite = 2
# Exemplo de saída: [3, 4]
'''
def valores_acima_limite(dicionario, limite):
    valores_acima = []
    for valor in dicionario.values():
        if valor > limite:
            valores_acima.append(valor)
    return valores_acima

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
limite = 2
resultado = valores_acima_limite(dicionario, limite)
print(f"Valores do dicionário {dicionario} acima do limite {limite}: {resultado}")
'''

# Exercício 6: Soma dos Valores com `while`
# Escreva um programa que some todos os valores de um dicionário cujas chaves são strings e os valores são inteiros, utilizando um loop `while`.
# Dica: Use `iter()` e `next()` para iterar sobre os valores do dicionário.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: 10
'''
def soma_valores(dicionario):
    soma = 0
    it = iter(dicionario.values())
    while True:
        try:
            valor = next(it)
            soma += valor
        except StopIteration:
            break
    return soma

# Exemplo de uso:
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
resultado = soma_valores(dicionario)
print(f"A soma dos valores do dicionário {dicionario} é: {resultado}")
'''
# Exercício 7: Valores Acima da Média
# Escreva um programa que encontre todos os valores de um dicionário que estejam acima da média de todos os valores.
# Dica: Use um loop `for` para calcular a média e outro loop `for` para encontrar os valores acima da média.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: [3, 4]
'''def valores_acima_da_media(dicionario):
    valores = list(dicionario.values())
    media = sum(valores) / len(valores)
    acima_da_media = []
    for valor in valores:
        if valor > media:
            acima_da_media.append(valor)
    return acima_da_media
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
resultado = valores_acima_da_media(dicionario)
print(f'Valores acima da média: {resultado}')  '''

# Exercício 8: Contagem de Palavras
# Escreva um programa que conte a frequência de cada palavra em uma lista de strings e armazene os resultados em um dicionário.
# Dica: Use um loop `for`.
# Exemplo de entrada: ["apple", "banana", "apple", "orange", "banana", "apple"]
# Exemplo de saída: {'apple': 3, 'banana': 2, 'orange': 1}
'''def contar_palavras(lista):
    frequencia = {}
    for palavra in lista:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia
lista = ["apple", "banana", "apple", "orange", "banana", "apple"]
resultado = contar_palavras(lista)
print(f'Resultado da contagem de palavras: {resultado}')'''


# Exercício 9: Atualizar Valores do Dicionário
# Escreva um programa que percorra um dicionário e atualize seus valores, adicionando 10 a cada valor.
# Dica: Use um loop `for`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Exemplo de saída: {'a': 11, 'b': 12, 'c': 13, 'd': 14}
'''
def valores(dicionario):
    dicionario_atualizado = {}
    for chave, valor in dicionario.items():
     novo_valor= valor + 10
     dicionario_atualizado[chave] = novo_valor
    
    return dicionario_atualizado
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
resultado = valores(dicionario)
print(f'Resultado da  atualização dos valores:{resultado} ')'''
# Exercício 10: Remover Chaves com Valores Negativos
# Escreva um programa que remova todas as chaves de um dicionário cujos valores sejam negativos.
# Dica: Use um loop `for` e uma estrutura `if`.
# Exemplo de entrada: {'a': -1, 'b': 2, 'c': -3, 'd': 4}
# Exemplo de saída: {'b': 2, 'd': 4}
'''def tirar_negativos(dicionario):
    dicionario_atualizado = {}
    for chave,valor in dicionario.items():
        if valor >= 0:
            dicionario_atualizado[chave] = valor
    return dicionario_atualizado
dicionario={'a': -1, 'b': 2, 'c': -3, 'd': 4} 
resultado= tirar_negativos(dicionario)
print(f"Tirando os numeros negativos o resultado é,{resultado}") '''   
# Exercício 11: Interseção de Dois Dicionários
# Escreva um programa que encontre as chaves comuns em dois dicionários e armazene essas chaves e seus valores em um novo dicionário.
# Dica: Use loops `for` e uma estrutura `if`.
# Exemplo de entrada: {'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 4, 'd': 5}
# Exemplo de saída: {'b': 2, 'c': 3}
'''
def intersecao_dicionario(dicionario1,dicionario2):

 dicionario_intersecao= {}

 for chave in dicionario1:
    if chave in dicionario2:
        dicionario_intersecao[chave] = dicionario1[chave] 
 return dicionario_intersecao
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 2, 'c': 4, 'd': 5}
resultado = intersecao_dicionario(dicionario1,dicionario2)
print(resultado)
'''

# Exercício 12: Contagem de Caracteres em Palavras
# Escreva um programa que conte a frequência de cada caractere em uma lista de palavras e armazene os resultados em um dicionário.
# Dica: Use um loop `for` aninhado.
# Exemplo de entrada: ["apple", "banana"]
# Exemplo de saída: {'a': 4, 'p': 2, 'l': 1, 'e': 1, 'b': 1, 'n': 2}
'''def contar_caracteres(palavra):
    contagem={}
    for palavra in palavra:
        
      for caracteres in palavra:
          
       if caracteres in contagem:
           
          contagem[caracteres] +=1
          
       else:
           contagem[caracteres] =1
    return contagem

palavra =["apple", "banana"]

resultado =contar_caracteres(palavra)
print(f"A frequencia de cada caractere é,{resultado}")
   '''     
       
# Exercício 13: Entrada de Usuário até 'Q'
# Escreva um programa que peça ao usuário para inserir valores em um dicionário até que ele digite 'Q' para sair.
# Exemplo de entrada: 
# (Usuário) a 1
# (Usuário) b 2
# (Usuário) Q
# Exemplo de saída: {'a': 1, 'b': 2}
'''

def entrada_usuario():
    dicionario = {}
    while True:
        entrada = input("(Usuário) Insira chave e valor (ou 'Q' para sair): ")
        
        if entrada.upper() == 'Q':
            break
        try:
            chave, valor = entrada.split()
            dicionario[chave] = int(valor)
        except ValueError:
            print("Entrada inválida. Por favor, insira no formato correto.")
    return dicionario
resultado = entrada_usuario()
print(f"Exemplo de saída: {resultado}")
'''
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
