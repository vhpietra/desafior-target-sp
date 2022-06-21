import json

file = open("Q3/dados.json")
dados = json.load(file)

max = 0
min = 9999999999999999
soma = 0
quantidade = 0
valores_acima = 0

for item in dados:
    if item['valor'] != 0:
        if item['valor'] < min:
            min = item['valor']
        if item['valor'] > max:
            max = item['valor']
        quantidade += 1
        soma += item['valor']

media = soma / quantidade

for item in dados:
    if item['valor'] > media:
        valores_acima += 1



print("Menor valor de faturamento diario no mês: " + str(min))
print("Maior valor de faturamento diario no mês: " + str(max))
print("Número de dias com faturamento superior à média mensal: " + str(valores_acima))
