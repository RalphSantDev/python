# Aula 51 - Desempacotamento de listas e tuplas

dados = [
    "joao",
    "bernardo",
    "sao paulo",
    "solteiro",
    "25"   
]

nome,sobrenome, *_, idade = dados 
print(nome)
print(sobrenome)
print(idade)