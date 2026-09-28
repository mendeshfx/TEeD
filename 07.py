identificador = input("Digite o identificador: ").strip()
if len(identificador) != 11:
    print("Erro: o identificador deve possuir 11 dígitos.")
elif not identificador.isdigit():
    print("Erro: o identificador deve conter apenas números.")
else:
    print("Identificador válido.")
