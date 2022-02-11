'''
DESEMPACOTAMENTO
*   PERMITE CRIAR OUTRA LISTA COM OS VALORES DENTRO DE UM OBJETO
'''

lista = ['Eu', 'Você', 'Nós',0,1,2,3]
n1,n2,n3, *n4= lista
print(n2)
print(*n4)