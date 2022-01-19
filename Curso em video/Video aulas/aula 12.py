#else if
#if condição:
#bloco1
#elif:
#bloco 2
#else:
#bloco 3
#=-=-=-=-=-=-=-=--==--==-=-=-==--==-
nome = str(input('qual é o seu nome?'))
if nome == 'enzo':
    print('que nome bonito')
elif nome == 'diogo' or 'lohra' or 'carlos':
    print('eai amigo do enzo prazer em te conhecer \033[4;30;44m{}\033[m.'.format(nome))
elif nome in 'matteo hiago cristhian leo':
    print('Salveeee')
else:
    print('prazer em te conhecer {}'.format(nome))
print('Tenha um bom dia \033[4;30;44m{}\033[m'.format(nome))


