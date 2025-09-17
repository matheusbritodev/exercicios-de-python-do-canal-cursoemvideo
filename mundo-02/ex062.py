"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
"""print(f"{"-=" * 20}")
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
quebra = " "
contagem_termos = 0
loop = 10
ultimo_termo = 0
while quebra not in "0":
    while loop > 0:
        print(f"{termo} ", end="")
        if termo > ultimo_termo:
            ultimo_termo = termo
        termo += razao
        print(" --> " if loop > 1 else "--> PAUSA", end="")
        loop -= 1
        contagem_termos += 1
    novo_termo = int(input("\nQuantos termos você quer mostrar a mais? "))
    if novo_termo != 0:
        lopp_sec = novo_termo
        while lopp_sec > 0:
            print(f"{ultimo_termo + razao} ", end="")
            if novo_termo > ultimo_termo:
                ultimo_termo = novo_termo
            ultimo_termo += razao
            print(" --> " if lopp_sec > 1 else "--> PAUSA", end="")
            lopp_sec -= 1
            contagem_termos += 1
    quebra = str(novo_termo) 
print(f"{"-=" * 20}\nProgressão finalizada com {contagem_termos} termos mostrados")"""

print(f"{"-=" * 20}")
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1
mais = 10
total = 0
ultimo_termo = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"{"-=" * 20}\nProgressão finalizada com {cont} termos mostrados")