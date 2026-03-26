# Aula 53 - Lista de compras
import os

lista = []

while True:

    print('___LISTA DE COMPRAS___')
    opcao = input('Selecione uma opcao: \n[1] - Adicionar item \n[2] - Remover item \n[3] - Mostrar lista \n[4] - Sair\n')

    if opcao == '1':
        os.system('cls')
        item = input('Digite oque deseja inserir: ')
        lista.append(item)
        print(f'{item} adicionado a lista!')


    elif opcao == '2':
        indice_str = input('Digite o indice do item que deseja remover: ')

        try: 
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um numero inteiro!')
        except IndexError:
            print('Esse indice nao existe!')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


       
    elif opcao == '3':
        os.system('cls')

        if len(lista) == 0:
            print('Lista vazia!')

        for indice, item in enumerate(lista):
            print(f'{indice} - {item}')


    elif opcao == '4':
        print('Saindo...')
        break

    else:
        print('Opcao invalida!')

    
        

        



