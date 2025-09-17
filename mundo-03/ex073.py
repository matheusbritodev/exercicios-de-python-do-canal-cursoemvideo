"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

tabela = (
    (1, 'Flamengo'),(2, 'Botafogo'),(3, 'Palmeiras'),(4, 'Athletico-PR'),(5, 'Bahia'),(6, 'Internacional'),(7, 'Cruzeiro'),(8, 'Atlético-MG'),(9, 'Vasco'),(10, 'São Paulo'),(11, 'Juventude'),(12, 'Bragantino'),(13, 'Fortaleza'),(14, 'Corinthians'),(15, 'Chapecoense'),(16, 'Vitória'),(17, 'Fluminense'),(18, 'Grêmio'),(19, 'Cuiabá'),(20, 'Atlético-GO')
)

print(f"\n{"-=" * 18}\nLista de times do brasileirão:")
for posicao, time in tabela:
    print(f"{posicao} - {time}")
    if time == "Chapecoense":
        chape = posicao, time

print(f"{"-=" * 18}\nOs 5 primeiros:")
for posicao, time in tabela:
    if 5 >= posicao >=1:
        print(f"{posicao} - {time}")

print(f"{"-=" * 18}\nOs 4 ultimos:")
for posicao, time in tabela:
    if 20 >= posicao >= 17:
            print(f"{posicao} - {time}")

ordem = sorted(tabela, key=lambda time: time[1])
print(f"{"-=" * 18}\nTimes em ordem alfabética:")
for posicao, time in ordem:
    print(time)
print(f"{"-=" * 18}\nA Chapecoense está na {chape[0]}ª posição\n")
