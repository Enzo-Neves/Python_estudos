km = float(input('Quantos KM você rodou?'))
dia = float(input('Quantos dias você ficou com o carro?'))
p = (dia*60) + (km*0.15)
print('O total a pagar é de R${:.2f}'.format(p))