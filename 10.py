while True:
    try:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            print("Programa encerrado.")
            break
        print("Número informado:", numero)
    except ValueError:
        print("Erro: digite um número inteiro.")
