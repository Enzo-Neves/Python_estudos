from random import randint
numeroUsuario = int(input('Em que número eu pensei?'))
numerodopc = randint(0, 5)
if numeroUsuario == numerodopc:
    print('voce venceu')
else:
    print('voce perdeu')
