""""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input("Digite um número inteiro: ")

try:
    numero = int(entrada)

    if numero % 2 == 0:
        print("Seu número é par")
    else:
        print("Seu número é ímpar")

    print('seu numero é inteiro')    

except ValueError:
    print("Isso não é um número inteiro.")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = int(input("Digite a hora (0-23): "))

    if 0 <= hora <= 11:
        print("Bom dia")
    elif 12 <= hora <= 17:
        print("Boa tarde")
    elif 18 <= hora <= 23:
        print("Boa noite")
    else:
        print("Hora inválida")

except ValueError:
    print("Você não digitou um número válido.") 

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    nome = input("Digite seu primeiro nome: ").strip()

    if not nome:
        raise ValueError("Entrada vazia")

    letras = len(nome)

    if letras <= 4:
        print("Seu nome é curto")
    elif 5 <= letras <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")

except ValueError:
    print("Você não digitou nada.")