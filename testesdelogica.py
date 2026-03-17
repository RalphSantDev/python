'''
# 1
# Peça um número ao usuário e mostre se ele é par ou ímpar.
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print (f'o numero {numero} é par')
else:
    print(f'o numero {numero} è impar')

# 2
# Peça dois números ao usuário e mostre qual é o maior.
num_1 = input('Digite um numero: ')
num_2 = input('Digite outro numero: ')

num_1_int = int(num_1)
num_2_int = int(num_2)

if num_1_int > num_2_int:
    print (f'O primeiro numero: {num_1_int} é maior qeu o segundo: {num_2_int}')
elif num_2_int > num_1_int:
    print(f'O segundo numero: {num_2_int} é maior que o primeiro: {num_1_int}')
else:
    print('os numeros sao iguais!')



# 3
# Peça a idade de uma pessoa e diga se ela pode votar ou não.
idade = int(input('Digite sua idade: '))
if idade >= 16:
    print('você pode votar!')
else:
    print('você não pode votar!')


# 4
# Peça um número ao usuário e informe se ele é:
# positivo
# negativo
# ou zero


numero = int(input('digite um numero: '))
if numero > 0:
    print(f'o numero {numero} é positivo')
elif numero < 0:
    print(f'o numero {numero} é negativo')
else:
    print('o numero é zero!')



# 5
# Mostre os números de 1 até 10 usando while.
i = 0
while i < 10:
    i += 1
    print(i)



# 6
# Peça 5 números ao usuário e mostre a soma total deles.
soma = 0
contador = 0
while contador < 5:
    numero = int(input('digite um numero: '))
    soma += numero
    contador += 1
print(f'a soma total dos numeros digitados é: {soma}')
''' 

# 7
# Peça números ao usuário até que ele digite 0.
# No final mostre quantos números foram digitados.
vezes_digitadas = 0
while True: 
    digite_numero = int(input('digite um numero: '))
    
    #sair  
    if digite_numero == 0:
        print (f'voce digitou {vezes_digitadas} numeros!')
        break
    vezes_digitadas += 1
    

# 8
# Peça um número ao usuário e mostre a tabuada dele de 1 até 10.
numero = int(input('digite um numero: '))
print(f'A tabuada de {numero} é: ')

for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')


# 9
# Peça uma palavra ao usuário e mostre quantas letras ela possui.
palavra = input('digite uma palavra: ')
print(f'a palavra "{palavra}" possui {len(palavra)} letras.')

# 10
# Peça uma palavra ao usuário e mostre a palavra ao contrário.
palavra = input('digite uma palavra: ')
print(f'a palavra "{palavra}" ao contrário é: {palavra[::-1]}')

# 11
# Peça uma palavra e uma letra ao usuário e mostre
# quantas vezes essa letra aparece na palavra.


# 12
# Peça 5 números ao usuário e mostre qual é o maior número digitado.


# 13
# Peça 3 notas de um aluno e calcule a média.
# Se a média for maior ou igual a 7 mostrar "Aprovado".
# Se for menor que 7 mostrar "Reprovado".


# 14
# Crie um jogo onde o computador escolhe um número entre 1 e 10
# e o usuário tenta adivinhar.
# O programa deve informar se o número digitado é maior,
# menor ou se o usuário acertou.


# 15
# Peça uma palavra ao usuário e conte quantas vogais existem nela.


# 16
# Crie um sistema de login simples.
# Defina no código:
# usuario = "admin"
# senha = "1234"
# Peça para o usuário digitar o login e a senha.
# Se estiver correto mostrar "Acesso permitido".
# Se estiver errado mostrar "Login inválido".
