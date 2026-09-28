def validar_cadastro(idade, curso, ano):
    if idade < 0:
        return "Idade inválida."
    if curso.strip() == "":
        return "Curso não pode ficar vazio."
    if ano < 1 or ano > 3:
        return "Ano inválido."
    return "Cadastro válido."
print(validar_cadastro(17, "Informática", 3))
print(validar_cadastro(16, "Administração", 2))
print(validar_cadastro(18, "Informática", 1))
print(validar_cadastro(-5, "Informática", 3))
print(validar_cadastro(17, "", 3))
print(validar_cadastro(17, "Informática", 5))
