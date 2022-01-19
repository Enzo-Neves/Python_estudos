#ordem de precedencia
#1 ()
#2 **
#3 * / // %
#4 +-
#//Pratica 
#raiz quadrada eleva a 1/2
#nome = input('Qual seu nome?')
#print('Prazer em te conhecer {:=^12}!'.format(nome))
n1 = int(input('Um valor:'))
n2 = int(input('segundo valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print('a soma vale: {}, o produto vale: {} e a divisao vale: {:.2f} '.format(s, m ,d), end='')
print('Divisao inteira: {} e potencia: {}'.format(d1, e))