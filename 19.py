def analisar_usuario(idade, renda, cadastro):
    if idade < 18:
        return "Usuário menor de idade."
    elif renda < 2000:
        return "Usuário maior de idade com renda baixa."
    elif cadastro:
        return "Usuário maior de idade, renda adequada e cadastro ativo."
    else:
        return "Usuário maior de idade, mas cadastro inativo."
print(analisar_usuario(17, 3000, True))
print(analisar_usuario(20, 1500, True))
print(analisar_usuario(25, 3000, True))
print(analisar_usuario(25, 3000, False))
