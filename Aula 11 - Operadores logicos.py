'''
and, or, not
in, not in
'''
a=1
b=2
c=3

#Verdadeiro E Falso = Falso
a and b

#Verdadeiro OU Verdadeiro
a or b

if b>a:
    print(f'{b} é maior que {a}')
else:
    print(f'{b} não é maior que {a}')

if not b>a: #INVERTEU
    print(f'{b} é maior que {a}')
else:
    print(f'{b} não é maior que {a}')

if 'o' in 'Johnny':
    print('existe o em johnny')

if 'o' not in 'Johnny':
    print('não existe o em johnny') #NOTE QUE NÃO IMPRIME!