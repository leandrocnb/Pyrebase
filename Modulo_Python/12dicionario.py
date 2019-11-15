dic_pernambucano = {'Sport':41, 'Santa Cruz':29, 'Nautico':21}

#Adicionando um elemento ao dicionario (Chave: valor)
dic_pernambucano['Salgueiro'] = 0
print(dic_pernambucano)

#Busca um valor com base na chave
quant_titulos = dic_pernambucano.get('Sport')
print('O Sport tem', quant_titulos, 'titulos')

#Remover um elemento com base na chave
del dic_pernambucano['Salgueiro']
print(dic_pernambucano)

#REmove a chave e retorna seu valor
valor = dic_pernambucano.pop('Nautico')
print('O valor retornado da chave Nautico')
print(dic_pernambucano)

#Verificar se uma chave existe no dicionario
print('Santa Cruz' in dic_pernambucano)

#Pegar todas as chaves do dicionario
print(dic_pernambucano.keys())

#Pegar todos os valores do dicionario
print(dic_pernambucano.values())