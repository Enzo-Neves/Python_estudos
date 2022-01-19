#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = input ('Insira o nome completo:')

print(nome.upper(), nome.lower())
Semespaço = nome.replace(" ", "")
print(len(Semespaço))
nome1 = nome.split() 
print (len(nome1[0]))