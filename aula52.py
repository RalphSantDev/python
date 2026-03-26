# Aula 52 - Enumerate
lista = ["joao", 'Maria', 'helena', 'luiz', 'ana']

for item in enumerate(lista):
    indice, nome = item
    print(f'{indice} - {nome}')

# Ou de forma mais simples:
for indice, nome in enumerate(lista):
    print(f'{indice} - {nome}')