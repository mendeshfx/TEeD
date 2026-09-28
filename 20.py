def cadastrar_aluno():
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        print("Erro: o nome não pode ficar vazio.")
        return
    try:
        idade = int(input("Idade: "))
        if idade <= 0:
            print("Erro: idade inválida.")
            return
        notas = []
        for i in range(3):
            nota = float(input(f"Digite a {i + 1}ª nota: "))
            if nota < 0 or nota > 10:
                print("Erro: a nota deve estar entre 0 e 10.")
                return
            notas.append(nota)
        media = sum(notas) / 3
        if media >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        print("\n--- RESULTADO ---")
        print("Nome:", nome)
        print("Idade:", idade)
        print("Média:", round(media, 2))
        print("Situação:", situacao)
    except ValueError:
        print("Erro: digite valores numéricos válidos.")
cadastrar_aluno()
