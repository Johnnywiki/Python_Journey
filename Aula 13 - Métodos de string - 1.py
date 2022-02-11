'''
 Métodos de string; check por erros
 '''

a = input("Forneça um numero")
b = input("Forneça um outro numero")
 
#isnumeric, isdigit, isdecimal
 
if a.isdigit():
     print("Tudo certo!")
else:
     print("ERRO! ALGO NÃO É UM NUMERO!")
