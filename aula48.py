"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
#pop() - remove o ultimo item da lista e armazena em uma variavel
lista = [10, 20, 30, 40]
lista.append('Luiz') # adiciona um item ao final da lista
nome = lista.pop()
print(lista)
print(f'valor retirado e armazenado é: {nome}')


# insert() - adiciona um item no índice escolhido
lista.insert(0, 'Maria') # adiciona o item 'Maria' no índice 0
print(lista)    

del lista[0] # apaga o item do índice 0
print(lista)

# extend() - estende a lista
lista1 = [1, 2, 3]  
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)

# clear() - limpa a lista
lista.clear()
print(lista)