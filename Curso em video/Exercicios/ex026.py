a = str(input ('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(a.count('a')))
print('A letra A aparece na {} posição' .format(a.find('a') + 1))
print('A última letra A aparece na posição {}'.format(a.rfind('a') + 1))
