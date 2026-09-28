nota = float(input("Digite a nota: "))
if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota >= 7:
    print("Excelente")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")
