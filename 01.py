entrada = input("Digite sua idade: ").strip()
if entrada == "":
    print("Erro: a idade não foi informada.")
else:
    try:
        idade = int(entrada)
        if idade <= 0:
            print("Erro: idade inválida.")
        else:
            print("Idade válida:", idade)
            print("O estudante pode participar da atividade.")
    except ValueError:
        print("Erro: digite uma idade usando apenas números.")
