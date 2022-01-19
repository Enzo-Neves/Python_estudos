km = float(input('Qual a distância da viagem?'))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(km))
if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45
print('O preço da passagem será de R${:.2f} '.format(passagem))
