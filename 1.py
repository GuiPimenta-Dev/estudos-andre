# Exercicio 1: Calculadora Simples
# Instrucao: Escreva um programa que exiba a soma, subtração, multiplicação e divisão deles.
# Tópicos para estudar:
# - Entrada de dados (input)
# - Conversão de tipos (int, float)
# - Operações aritméticas básicas (+, -, *, /)
# - Impressão de dados (print)
'''
numero_1 =int( input("insert number one: "))
numero_2 =int( input("insert number two: "))
soma  =numero_1+numero_2
divisão = numero_1/numero_2
subtração = numero_1-numero_2
multiplicação =numero_1*numero_2
print(soma)
print(subtração)
print(divisão)
print(multiplicação)
'''
# Exercicio 2: Média de três números
# Instrucao: Escreva um programa que peça ao usuário três números e calcule a média deles.
# Tópicos para estudar:
# - Entrada de dados (input)
# - Conversão de tipos (int, float)
# - Operações aritméticas básicas (+, /)
# - Impressão de dados (print)
'''
numero_4 =int(input("insert number one"))
numero_5 =int(input("insert number two"))
numero_6 =int(input("insert number tres"))

numerador =numero_4+numero_5+numero_6
denominador =3
media =numerador/denominador

print(media)
'''
# Exercicio 3: Conversão de Temperatura
# Instrucao: Escreva um programa que peça ao usuário a temperatura em graus Celsius e a converta para Fahrenheit.
# Fórmula: F = C * 9/5 + 32
# Tópicos para estudar:
# - Entrada de dados (input)
# - Conversão de tipos (int, float)
# - Operações aritméticas básicas (*, +, /)
# - Impressão de dados (print)
'''
C =int(input("insira o valor em celsius"))
conversao =C*(9/5)+32
print(conversao)
'''



# Exercicio 4: Área de um Círculo
# Instrucao: Escreva um programa que peça ao usuário o raio de um círculo e calcule a área dele.
# Fórmula: Área = π * raio^2 (π = 3.14159)
# Tópicos para estudar:
# - Entrada de dados (input)
# - Conversão de tipos (int, float)
# - Operações aritméticas básicas (*, **)
# - Impressão de dados (print)

'''
raio =int(input("insira o valor do raio do circulo"))
area =3.14159*raio**2
print(area)
'''

# Exercicio 5: Idade do Usuário
# Instrucao: Escreva um programa que peça ao usuário o nome e o ano de nascimento e calcule a idade dele.
# Resposta: "Olá, [nome]. Você tem [idade] anos."
# Tópicos para estudar:
# - Entrada de dados (input)
# - Conversão de tipos (int)
# - Operações aritméticas básicas (-)
# - Impressão de dados (print)
'''
nome =input("Insira o seu nome") 
nascimento =int(input("insira o ano de nascimento"))
import datetime
hoje =datetime.date.today()
idade = hoje.year - nascimento
print(f"Olá, {nome} Você tem, {idade}, anos")
'''

# Exercicio 6: Mostar dia atual, ontem e amanhã
# Instrucao: Escreva um programa que mostre o dia atual, o dia de ontem e o dia de amanhã.
# Resposta: "Ontem foi [dia]. Hoje é [dia]. Amanhã será [dia]."
# Tópicos para estudar:
# - Manipulação de datas (datetime)
# - Impressão de dados (print)
'''
from datetime import datetime, timedelta

anos_print = 2024

agora = datetime.now().replace(year=anos_print, hour=0, minute=0, second=0, microsecond=0)
hoje = agora
ontem = (datetime.now() - timedelta(days=1)).replace(year=anos_print, hour=0, minute=0, second=0, microsecond=0)
amanha = (datetime.now() + timedelta(days=1)).replace(year=anos_print, hour=0, minute=0, second=0, microsecond=0)

print(f"Ontem foi {ontem.strftime('%d-%m-%Y')}. Hoje é {agora.strftime('%d-%m-%Y')}. Amanhã será {amanha.strftime('%d-%m-%Y')}")
'''
# Exercicio 7: Contador de letras
# Instrucao: Escreva um programa que peça ao usuário uma frase e conte quantas letras há na frase e devolva a primeira e a última palavra.
# Resposta: "A frase tem [n] letras."
# Tópicos para estudar:
# - Entrada de dados (input)
# - Manipulação de strings 
# - Impressão de dados (print)
 
frase = input("insira a frase")
tamanho_frase = 0

for caractere in frase:
    if caractere.isalpha():  
        tamanho_frase += 1
        
print(f"A Frase tem {tamanho_frase} letras.")

# Exercicio 8: Conversor de string para maiúsculas, minúsculas e título
# Instrucao: Escreva um programa que peça ao usuário uma frase e converta todas as letras para maiúsculas, minusculas e titulo.
# Resposta: "Minuscula: [frase]. Maiuscula: [frase]. Titulo: [frase]."
# Tópicos para estudar:
# - Entrada de dados (input)
# - Manipulação de strings (lower, upper, title)
# - Impressão de dados (print)

# Código aqui
