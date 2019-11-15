valor_1 = 30 
valor_2 = 30

if(valor_1 <= valor_2):
    print('Realmente', valor_1, 'eh menor ou eh igual a', valor_2)
else:
    print(valor_1, 'não eh menor ou igual a', valor_2)

idade = 90
print('Sua idade eh', idade)

if(idade >= 18 and idade <= 60):
    print('Você pode tomar Catuaba!')
elif(idade < 18):
    print('Você NÃO pode tomar Catuaba!')
elif(idade > 80):
    print('Seria melhor você NÂO tomar Catuaba! #FicaDica')
