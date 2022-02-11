'''
len -> permite adquirir o numerod de caracteres; funciona apenas com strings (inicialmente)
'''


teste = input('Insira seu nome!')
nLetras = len(teste)

print(teste, nLetras, type(nLetras))

if nLetras<2:
    print("Isso não é um nome...")
else:
    print("Ah sim, então esse é seu nome!")
    
