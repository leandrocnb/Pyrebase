nome_aluno = 'Chimbinha'
nota_3 = 3
nota_4 = 2

media = (nota_3 + nota_4) / 2

#Verifica se aluno teve media maior igual a 7
if(media >= 7 and media <= 10):
    print(nome_aluno, 'foi aprovado com a media', media)
#Verifica se o aluno teve media entre 3 e 7
elif(media >= 3 and media < 7):
    print(nome_aluno, 'esta na recuperação com media ', media)
#Verifica se o aluno teve media menor que 3 e maior ou igual a 0
elif(media < 3 and media >= 0):
    print(nome_aluno, 'foi reprovado com media ',media)
else:
    print('valores inválidos')

nome_candidato = 'MC Troinha'
nota_Enem = 8
is_portador_diploma = False

if(is_portador_diploma == True or (nota_Enem >= 7 and nota_Enem  <= 10)):
    print(nome_candidato, 'Aprovado na seleção pela nota ou por possuir diplioma!')
else:
    print(nome_candidato, 'Reprovado pois não possui diploma e nem tem nota maior que 7')