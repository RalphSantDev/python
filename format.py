a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
print(formato)


''' outro jeito de format

nome = 'raphael'
sobrenome = 'santana'
idade = 19
ano_nascimento = 2025 - idade
maior_de_idade = idade >= 18 
altura = 1.80

print(f'nome: {nome}')
print(f'sobrenome:{sobrenome}')
print(f'idade:{idade}')
print(f'ano de nascimento:{ano_nascimento}')
print(f'é maior de idade?:{maior_de_idade}')
print(f'altura:{altura:.2f}m')


'''