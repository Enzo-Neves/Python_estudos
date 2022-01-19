velocidadedocarro = float(input('qual a velocidade do carro?'))
if velocidadedocarro <= 80.00:
    print('tenha um bom dia, dirija com cuidado')
else:
    valordamulta = (velocidadedocarro - 80) * 7.00
    print('Voce esta acima do limite de velocidade, total da multa a pagar é {:.2f}'.format(valordamulta))
