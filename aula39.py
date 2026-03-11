'''
nome = input("Digite seu nome: ")

indice = 0
novo_nome = ""

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{letra}*'
    indice += 1

print("Nome modificado:", novo_nome)
'''

# iterando sobre uma string com while
string = 'Olá mundo'

i = 0

while i < len(string):
    letra = string[i]
    print(letra)
    i += 1