'''
Operadores relacionais
==, >, >=, <, <=, !=
== igual que
> maior que
>= maior ou igual que
< menor que
<= menor ou igual que
!= Diferente
'''
print(2==2)
num1 = 2
num2 = 2
num3 = num1 == num2
print(num3)
print(2>1)
print(2>=2)
print(2<3)
print(2<=3)
print(2!=3)

idade = int(input("Qual sua idade? "))
idadeLimiteMax = 30
idadeLimiteMin= 18

if idade>=idadeLimiteMin and idade<=idadeLimiteMax:
    print(f'O usuario pode pegar um emprestimo!')
else:
    print(f'O usuario não pode pegar um emprestimo!')