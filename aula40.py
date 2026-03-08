##### calculadora com while #####
# Crie uma calculadora simples que permita ao usuário escolher entre adição, subtração, multiplicação e divisão. A calculadora deve continuar funcionando até que o usuário escolha sair.

while True:

    print("__________Calculadora Simples__________")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    try:
        opcao_int = int(opcao)
        if opcao_int < 0 or opcao_int > 4:
            raise ValueError("Opção inválida. Por favor, escolha entre 0 e 4.")

    except ValueError as e:
            print(f"Erro: {e}")
            continue

    if opcao == "0":
        print("Encerrando a calculadora. Até mais!")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    numeros_validos = True

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    
    except:
        numeros_validos = None
        print("Erro: Por favor, digite números válidos.")
        continue

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

    numeros_validos = True


    try: 
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except ValueError:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Erro: Por favor, digite números válidos.")
        continue

    operadores_permitidos = ["+", "-", "*", "/"]
    if operacao not in operadores_permitidos:
        print("Erro: Operação inválida. Por favor, escolha entre +, -, * ou /.")
        continue

    if operacao == "+":
        resultado =float(numero_1) +float(numero_2)
        print(f'o resultado da adicao é: {resultado}')
        print("Operação realizada com sucesso!")
    elif operacao == "-":
        resultado =float(numero_1) -float(numero_2)
        print(f'o resultado da subtração é: {resultado}')
        print("Operação realizada com sucesso!")
    elif operacao == "*":
        resultado =float(numero_1) *float(numero_2)
        print(f'o resultado da mulltiplicação é: {resultado}')
        print("Operação realizada com sucesso!")
    elif operacao == "/":
        if float(numero_2) != 0:
            resultado = float(numero_1) / float(numero_2)
            print(f'o resultado da divião é: {resultado}')
            print("operacao realizada com sucesso!")
        else:
            print("Erro: Divisão por zero não é permitida.")

    sair = input("Deseja sair? (s/n): ").lower().startswith("s")
    if sair is True:
        print("Encerrando o programa. Até mais!")
        break
        
'''