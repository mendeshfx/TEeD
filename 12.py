nomes = ["Ana", "João", "Maria", "Ana", "Pedro", "João"]
vistos = set()
duplicados = set()
for nome in nomes:
    if nome in vistos:
        duplicados.add(nome)
    else:
        vistos.add(nome)
if duplicados:
    print("Nomes repetidos:", list(duplicados))
else:
    print("Não existem nomes repetidos.")
