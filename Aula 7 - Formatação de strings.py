'''
Iniciar com letra APENAS!!, pode conter numeros, separar com _, letras minusculas
'''

nome = 'Johnny'
idade = 18
altura = 1.81
altura2 = 1.81284765839
peso = 58

compararA = idade > altura
imc = peso/altura**2
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Minha idade é superior a minha altura em cm?:', compararA)

'''
desafio!!
'''

print(nome, 'tem', idade, 'com', str(altura)+'cm,', 'sendo assim tendo um IMC de:',imc)
print(f'{nome} tem {idade} com {altura}cm, sendo assim tendo um IMC de: {imc}            ALTERNATIVA DE ESCRITA' )
print(f'Altura com limitação por 2f!! : {altura2:.2f}')