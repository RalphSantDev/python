##### calculadora com while #####
# Crie uma calculadora simples que permita ao usuário escolher entre adição, subtração, multiplicação e divisão. A calculadora deve continuar funcionando até que o usuário escolha sair.
'''
while True:

    print("Calculadora")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando a calculadora. Até mais!")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Realizando adição...")
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado:.2f}")
        print("Operação realizada com sucesso!")
    elif opcao == "2":
        print("Realizando subtração...")
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado:.2f}")
        print("Operação realizada com sucesso!")

    elif opcao == "3":
        print("Realizando multiplicação...")
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado:.2f}")
        print("Operação realizada com sucesso!")

    elif opcao == "4":
        print("Realizando divisão...")
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado:.2f}")
            print("Operação realizada com sucesso!")
        else:
            print("Erro: Divisão por zero não é permitida.")
'''

# calculadora sem menu, apenas com os inputs
while True:
    
    numero_1 = (input("Digite o primeiro número: "))
    numero_2 = (input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = int(numero_1) + int(numero_2)
        print(f'o resultado da adicao é: {resultado}')
        print("Operação realizada com sucesso!")
    elif operacao == "-":
        resultado = int(numero_1) - int(numero_2)
        print(f'o resultado da subtração é: {resultado}')
        print("Operação realizada com sucesso!")
    elif operacao == "*":
        resultado = int(numero_1) * int(numero_2)
        print(f'o resultado da mulltiplicação é: {resultado}')
        print("Operação realizada com sucesso!")
    elif operacao == "/":
        if int(numero_2) != 0:
            resultado = int(numero_1) / int(numero_2)
            print(f'o resultado da divião é: {resultado}')
            print("operacao realizada com sucesso!")
        else:
            print("Erro: Divisão por zero não é permitida.")

    sair = input("Deseja sair? (s/n): ").lower().startswith("s")
    if sair is True:
        print("Encerrando o programa. Até mais!")
        break