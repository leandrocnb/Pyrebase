#Declarando uma lista vazia
lista = []

#Adicionar elementos
lista.append('Joelma')
lista.append('Chimbinha')
lista.append('Safadao')
lista.append('Annita')
print(lista)

#Inserir elemento em uma posição especifica
lista.insert(0, 'MC Troinha')
print(lista)

#Remover um elemento pelo valor
lista.remove('Annita')
print(lista)

#Pegando posição do elemento pelo valor
local = lista.index('Safadao')
print(local)

#Removendo em elemento pelo index
del(lista[local])
print(lista)

#Invertendo ordem da lista
lista.reverse()
print(lista)

#Ordenando uma lista
lista.sort()
print(lista)

