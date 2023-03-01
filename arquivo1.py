import json

# abre o arquivo com o faturamento diário
with open("faturamento.json", "r") as f:
    faturamento = json.load(f)

# inicializa as variáveis para cálculo do menor valor, do maior valor e da média
menor_valor = float("inf")
maior_valor = float("-inf")
total_faturado = 0
dias_com_faturamento_superior_a_media = 0

# calcula o menor valor, o maior valor e a média
for valor in faturamento.values():
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    total_faturado += valor

media = total_faturado / len(faturamento)

# calcula o número de dias com faturamento superior à média
for valor in faturamento.values():
    if valor > media:
        dias_com_faturamento_superior_a_media += 1

# imprime os resultados
print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_com_faturamento_superior_a_media}")