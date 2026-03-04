nome = input("Nome: ")
idade = input("Idade: ")

if nome.strip() and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    
    
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não tem espaços")


    print('seu nome tem: ',len(nome),'letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')


else:
    print("Preencha nome e idade")