def calcular_compra(valor):
    if valor < 0:
        return "Valor inválido."
    if valor <= 100:
        return valor
    else:
        return valor * 0.90
print(calcular_compra(50))
print(calcular_compra(100))
print(calcular_compra(100.01))
print(calcular_compra(200))
print(calcular_compra(0))
print(calcular_compra(-10))
