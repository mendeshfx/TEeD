try:
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        dados = arquivo.read()
        print(dados)
except FileNotFoundError:
    print("Erro: o arquivo 'alunos.txt' não foi encontrado.")
