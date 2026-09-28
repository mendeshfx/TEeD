senha_correta = "123456"
max_tentativas = 3
for tentativa in range(1, max_tentativas + 1):
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado.")
        break
    else:
        restantes = max_tentativas - tentativa
        if restantes > 0:
            print("Senha incorreta.")
            print("Tentativas restantes:", restantes)
        else:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")
