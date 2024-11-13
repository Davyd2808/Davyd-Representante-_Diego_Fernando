n = int(input("Insira a quantidade de dias: "))  # Quantidade de dias

meta_dia = 150
dias_cumpriram_meta = 0
soma_consumo = 0
maior_consumo = None
menor_consumo = None

for dia in range(1, n + 1):
    consumo = int(input(f"Insira o consumo do dia {dia}: "))

    if consumo < 0:
        print("Por favor, insira um valor positivo.")
        continue

    if consumo >= meta_dia:
        dias_cumpriram_meta += 1

    soma_consumo += consumo

    if maior_consumo is None or consumo > maior_consumo:
        maior_consumo = consumo
    if menor_consumo is None or consumo < menor_consumo:
        menor_consumo = consumo


media_consumo = soma_consumo / n

if dias_cumpriram_meta == n:
    print("Parabéns! Todos os dias cumpriram a meta de consumo sustentável.")
elif dias_cumpriram_meta == 0:
    print("Infelizmente, nenhum dia cumpriu a meta de consumo sustentável." )
else:
    dias_nao_cumpriram_meta = n - dias_cumpriram_meta
    print(f"{dias_cumpriram_meta} dias cumpriram a meta e {dias_nao_cumpriram_meta} dias não cumpriram a meta.  ")

print(f"A média de consumo foi de {media_consumo} kWh. O maior consumo foi de {maior_consumo} kWh e o menor consumo foi de {menor_consumo} KWh.")

