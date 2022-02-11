'''
Listas
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''
#         0    1    2   3   4   5   6
array = ['a', 'b', 'c', 10, True, 10.5]
array[3] = 'Não c'

print(array[3])
#print(array[::-1])     REVELA LISTA DE TRAS PARA FRENTE

l1=[1,2,3]
l2=[8,9,10]
l3= l1 + l2
l4= list(range(1,20)) # CRIOU UM ARRAY COM RANGE DE 1-20 COM NUMERO MAX 19

print(l3)
#OU

l1.extend(l2)
print(l1)


l2.append('valor final')
print(l2)


l2.insert(0, 'valor inicial')
print(l2)


l2.pop() #  DELETA O ULTIMO ELEMENTO!
print(l2)


del(l2[0:2]) #     DELETOU A FAIXA DE ELEMENTO DESEJADA
print(l2)

print(l4)
print( max(l4))
print(min(l4))