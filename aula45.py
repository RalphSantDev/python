# Jogo de Adivinhar a Palavra Secreta
'''
palavra_secreta = "ariane"  # Defina a palavra secreta aqui
letras_adivinhadas = set()
tentativas = 0

print("Bem-vindo ao jogo de adivinhar a palavra secreta!")
print(f"A palavra tem {len(palavra_secreta)} letras.")

# Mostrar palavra inicial
palavra_atual = ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])
print(palavra_atual)

while True:
    palpite = input("Digite uma letra ou 'desistir' para desistir: ").lower()
    
    if palpite == 'desistir':
        print(f"Você desistiu! A palavra secreta era '{palavra_secreta}'.")
        break
    
    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue
    
    if palpite in letras_adivinhadas:
        print("Você já tentou essa letra.")
        continue
    
    letras_adivinhadas.add(palpite)
    tentativas += 1
    
    if palpite in palavra_secreta:
        print(f'correto! A letra "{palpite}" está na palavra.')
    else:
        print(f'Incorreto! letra "{palpite}" não está na palavra.')
    
    palavra_atual = ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])
    print(palavra_atual)
    
    if '_' not in palavra_atual:
        print(f"Parabéns! Você adivinhou a palavra '{palavra_secreta}' em {tentativas} tentativas.")
        break
'''

palavra_secreta = "a"
letras_certas = ''
tentativas = 0


print("Bem-vindo ao jogo de adivinhar a palavra secreta!")
print(f"A palavra tem {len(palavra_secreta)} letras.")

while True:
    palpite = input('digite uma letra: ')
    tentativas += 1

    if len(palpite) > 1:
        print("Por favor, digite apenas uma letra.")
        continue

    if palpite in palavra_secreta:
      print(f'correto! A letra "{palpite}" está na palavra.')
      letras_certas += palpite

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'

    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('parabéns! Você adivinhou a palavra secreta em', tentativas, 'tentativas.')
        tentativas = 0
        letras_certas = ''
        break
        

