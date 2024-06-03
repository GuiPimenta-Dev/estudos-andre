# Tópicos para estudar:


# Booleanos (https://panda.ime.usp.br/aulasPython/static/aulasPython/aula05.html)
# Condicionais (https://www.hashtagtreinamentos.com/estruturas-condicionais-no-python?gad_source=1&gclid=Cj0KCQjw3tCyBhDBARIsAEY0XNkhqehM5sFoA8OpJgtRrGEYQW_IJIS-UQnRKbA0nyvweXsbUhTBxVcaAhpZEALw_wcB)
"""
== -> Igualdade
!= -> Diferença
> -> Maior que
< -> Menor que
"""
# Lista (https://www.hashtagtreinamentos.com/listas-no-python?gad_source=1&gclid=Cj0KCQjw3tCyBhDBARIsAEY0XNn4i3dikKuwPB2R1c-M4Jk3XaEzlxOoX4ei2hmd6zKAmdylzQP-XlAaAhLREALw_wcB)

# Exercicio 1: Comparação de Strings
# Instrucao: Escreva um programa que peça ao usuário duas strings e verifique se são iguais, ignorando maiúsculas e minúsculas.
# Tópicos para estudar:
# - Entrada de dados (input)
# - Manipulação de strings (lower)
# - Estruturas condicionais (if, else)
# - Impressão de dados (print)
'''
palavra = input("insira uma palavra")
palavra_2 = input("insira uma palavra")

minusculo = palavra.lower()
minusculo_2 = palavra_2.lower()
  

if minusculo == minusculo_2:
    print("são iguais")
else:
    print("não são iguais")
'''


# Exercício 2: Números Pares e Ímpares
# Instrucao: Escreva um programa que peça ao usuário um número inteiro e verifique se ele é par ou ímpar.
# Tópicos para estudar:
# - Entrada de dados (input)
# - Conversão de tipos (int)
# - Operadores aritméticos (%)
# - Estruturas condicionais (if, else)
# - Impressão de dados (print)
'''
numero = int(input("insira um numero"))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
'''

# Exercício 3: Verificação de Idade
# Instrucao: Escreva um programa que peça ao usuário sua idade e verifique se ele é maior de idade (18 anos ou mais).
# Tópicos para estudar:
# - Entrada de dados (input)
# - Conversão de tipos (int)
# - Estruturas condicionais (if, else)
# - Impressão de dados (print)
'''
idade = int(input("idade do usuario"))
if idade >=18 :
  print("você é maior de idade")
else:
  print("você é menor de idade")
'''
# Exercício 4: Devolva a priemira e ultima palavra de uma frase
# Instrucao: Escreva um programa que peça ao usuário uma frase e devolva na tela a primeira palavra e a ultima dessa frase.
# - Entrada de dados (input)
# - Lista 
'''
frase = input("insira a frase")

palavra =frase.split()
primeira_frase=palavra[0]
ultima_palavra=palavra[-1]
meio_frase= palavra[1:-1]
print("Primeira frase:",primeira_frase)
print("Ultima frase", ultima_palavra)
print("Meio da frase", meio_frase)

'''
 
 # Exercício 5: Escreva um programa que peça ao usuário uma frase e devolva na tela o número de palavras dessa frase.
# - Entrada de dados (input)
# - Lista

# Exercício 6: Escreva um programa que peça ao usuário uma frase e devolva na tela a palavra mais longa dessa frase.
# - Entrada de dados (input)
# - Lista

# Exercício 7: Escreva um programa que peça ao usuário uma frase e devolva na tela as palavras dessa frase em ordem inversa.
# - Entrada de dados (input)
# - Lista

# Exercício 8: Escreva um programa que peça ao usuário uma frase e devolva na tela a frase sem palavras duplicadas.
# - Entrada de dados (input)
# - Lista
# - Conjuntos (Set)

# Exercício 9: Escreva um programa que peça ao usuário uma frase e uma letra. Encontre todas as palavras na frase que começam com essa letra e devolva na tela.
# - Entrada de dados (input)
# - Lista
# - Condicional (if)