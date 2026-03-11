palavra_secreta = "developer"
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
        print(f'Parabéns! Você adivinhou a palavra "{palavra_secreta}" em {tentativas} tentativas.')
        print(f'A palavra secreta era "{palavra_secreta}".')
        tentativas = 0
        letras_certas = ''
    break
        

