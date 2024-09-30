# Operadores in e not in
# Strings são interáveis
# 0 1 2 3 4 5
# R a f a e l
# -6-5-4-3-2-1

#nome = 'Rafael'
#print(nome[-4])
#print(nome[3])
# print('ael' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('ael' not in nome)
# print('zero' not in nome)

Texto = input('Digite seu texto: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in Texto:
    print(f'{encontrar} esta em {Texto}')

else:
    print(f'{encontrar} não está em {Texto}')