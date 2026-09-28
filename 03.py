alunos = ["Ana", "João", "Maria", "Pedro"]
try:
    indice = int(input("Digite o índice do aluno: "))
    if indice < 0:
        print("Erro: o índice não pode ser negativo.")
    elif indice >= len(alunos):
        print("Erro: índice inexistente.")
    else:
        print("Aluno:", alunos[indice])
except ValueError:
    print("Erro: digite um número inteiro.")
