


import math
an = float(input('digite o angulo que voce deseja:'))
seno = math.sin(math.radians(an))
coseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('o angulo de {} tem o seno de: {:.2f}, o coseno de: {:.2f}, e a tangente de: {:.2f}'.format(an,seno,coseno,tangente))