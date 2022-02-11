while True:
    print('----------------------')
    num1=input('Primeiro numero ')
    num2=input('Segundo numero ')
    metodo=input('Operação a ser realizada ')

    if not num1.isnumeric() or not num2.isnumeric():
        print("Erhm, algo não é um valor númerico comum, revise porfavor...")
        continue
 
    num1=int(num1)
    num2=int(num2)

    if metodo == '+':
        print(num1+num2)
    elif metodo == '-':
        print(num1-num2)
    elif metodo == '/':
        print(num1/num2)
    elif metodo == '*':
        print(num1*num2)
