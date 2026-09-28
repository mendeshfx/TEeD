entrada = input("Digite a nota de 0 a 10: ").strip()
try:
    nota = float(entrada)
    if nota < 0 or nota > 10:
        print("Erro: a nota deve estar entre 0 e 10.")
    elif nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
except ValueError:
    print("Erro: digite uma nota numérica.")
