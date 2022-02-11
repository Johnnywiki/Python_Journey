'''
Tipos de dados básicos são...
str - caracteres conectados | 'Hello world!'
int - inteiros | '10', '20', '-100', '-22222'...
float - reais | '10.1', '22.22222'...
bool - verdadeiro ou falso | 'true' OU 'false' | '10 == 10'
'''

'''
type -> Revela o tipo de dado presente na função.
'''

print('Johnny',type('Johnny'))
print(10,type(10))
print('True',type(True))
print('10==10',type(10==10))
print('22.2',type(22.2))

#TRANSMOGRAFIA DE STRING PRA INTEIRO!!!
print('10', type('10'), type(int('10')))
