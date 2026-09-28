nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
quantidade = int(input("Digite a quantidade de notas: "))
if quantidade == 0:
    print("Erro: não é possível dividir por zero.")
else:
    media = (nota1 + nota2) / quantidade
    print("Média:", media)
