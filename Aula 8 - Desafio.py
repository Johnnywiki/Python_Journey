'''
Criar variaveis pra nome, idade, altura, e peso.
Criar variavel pro ano atual
Obter ano de nascimento da pessoa ( BASEADO NA IDADE E NO ANO ATUAL )
Obter o IMC da pessoa com 2 CASAS DECIMAIS
Exibir um texto com todos os valores na tela usando F-STRINGS
'''
nome = ('Johnny')
idade = 18
altura = 1.81
peso = 58.543
anoAtual = 2022
anoDeNascimento = (anoAtual-(idade+1))
imc = peso/altura**2

print(f'{nome} tem {idade} anos com {altura}cm e pesando entre {peso}, fazendo o assim ter o imc de {imc:.2f}. Ele atualmente vive em {anoAtual} e nasceu em {anoDeNascimento}')
