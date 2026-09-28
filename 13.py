temperaturas = [25, -3, 18, 30, 30, -5]
maior = temperaturas[0]
menor = temperaturas[0]
for temperatura in temperaturas[1:]:
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
