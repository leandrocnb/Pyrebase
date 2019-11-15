#Laço para executar 10 vezes
for elemento in range(10):
    print(elemento)

#Podemos ir de 0 a 10 pulando de 2 em 2
for elemento in range(0, 10, 2):
    print(elemento)

#Declarando uma lista com algun elementos
lista = ['Eu', 'sei', 'fazer', 'isso', 'agora']

#Laço para percorrer um lista 
for elemento in lista:
    print(elemento)

conta = 0 
#Laço que roda até condição ser satisfeita
while(conta <= 10):
    conta += 1
    print(conta)

#Laço que executa condição quando for True e altera
condicao = True
while(condicao):
    print('Bloco while() e condicao==True')
    condicao = False
else:
    print('Bloco ELSE e condicao == False')

#Laço invocando o comando Break
condicao = True
while(condicao):
    print('Bloco while e condicao == True')
    condicao = False
    break
else:
    print('BLOCO ELSE e condicao == False')