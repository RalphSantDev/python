# Exemplo de uso do continue e break em loops aninhados
for i in range(10):

    if i == 5:
        print("Número 5 encontrado, pulando para o próximo número.")
        continue

    if i == 8:
        print("Número 8 encontrado, encerrando o loop.")
        break

    for j in range(1, 3):
        print(f"i: {i}, j: {j}")
else:
    print("Loop concluído sem interrupção.")