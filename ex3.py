import json

# Carregar os dados do arquivo JSON
with open('dados.json', 'r') as dados:
    faturamentos = json.load(dados)

menor_valor = None
dia_menor_valor = None
maior_valor = None
dia_maior_valor = None
soma_faturamentos = 0
dias_validos = 0
dias_acima_da_media = []

for i in faturamentos:
    valor = i['valor']
    if valor > 0:
        dias_validos += 1
        soma_faturamentos += valor

        if menor_valor is None or valor < menor_valor:
            menor_valor = valor
            dia_menor_valor = i['dia']

        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
            dia_maior_valor = i['dia']

# Calcular a média apenas com dias válidos
if dias_validos > 0:
    media = soma_faturamentos / dias_validos
else:
    media = 0


# Verificar quais dias têm faturamento acima da média
if (media > 0):
    for i in faturamentos:
        if i['valor'] > media:
            dias_acima_da_media.append(i['dia'])

if menor_valor is not None:
    print(f"Menor valor de faturamento ocorreu no dia {dia_menor_valor} com valor: {menor_valor}\n")
else:
    print("Não houve faturamento válido.\n")

if maior_valor is not None:
    print(f"Maior valor de faturamento ocorreu no dia {dia_maior_valor} com valor: {maior_valor}\n")
else:
    print("Não houve faturamento válido.\n")

if dias_acima_da_media:
    print(f"Número de dias no mês com faturamento acima da média mensal: {len(dias_acima_da_media)}\n")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}\n")
else:
    print("Não houve dias com faturamento acima da média.\n")
