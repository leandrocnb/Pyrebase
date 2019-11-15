#Declarando uma piplha
pilha = ['Aecio', 'Temer', 'Dilma']


#Adicionando em elemento no topo da pilha
pilha.append('Lula')
print('Primeira pilha', pilha)

#Ultimo elemento a chegar sai
elemento = pilha.pop()
print(elemento, 'saiu')

#Ultimo elemento a chegar sai
elemento = pilha.pop()
print('tiraram a', elemento)

print('sobrou agora', pilha)