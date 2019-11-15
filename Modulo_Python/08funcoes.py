altura = float(input('Qual sua Altura: '))
peso = float(input('Qual seu peso: '))

def calcular_imc(valor_altura, valor_peso):
    valor_imc = valor_peso / (valor_altura*valor_altura)
    return valor_imc

print(calcular_imc(altura, peso))


