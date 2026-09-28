entrada = input("Digite o preço do produto: ").strip()
try:
    preco = float(entrada)
    if preco < 0:
        print("Erro: o preço não pode ser negativo.")
    else:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
        else:
            total = preco * quantidade
            print("Valor total: R$", round(total, 2))
except ValueError:
    print("Erro: digite um valor numérico válido.")
