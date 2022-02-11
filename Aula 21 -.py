'''
Split, Join, Enumerate
Split = Divide listas em strings
Join = Junta uma lista a uma string
Enumerate = Enumera elemtentos da listra iteraveis
'''
frase = 'Eu te amo, me lembrarei até quando esquecer'
teste1 = frase.split();
teste2 = frase.split(',')
print(teste1)
print(teste2)

frase2 = '-'.join(teste1)
print(frase2)

#if Johnny in World is True:
   # remember(me);
    #continue;

for index, index2 in enumerate(frase):
    print(index,index2);

