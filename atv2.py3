# Função principal da calculadora
def calculadora():
    # Solicita ao usuário que insira dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza as operações
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    # Exibe os resultados das operações
    print(f"A soma de {num1} e {num2} é {soma};")
    print(f"A subtração de {num1} por {num2} é {subtracao};")
    print(f"A multiplicação de {num1} e {num2} é {multiplicacao};")

    # Verifica se o segundo número é zero antes de realizar a divisão
    if num2 != 0:
        divisao = num1 / num2
        print(f"A divisão de {num1} por {num2} é {divisao};")
    else:
        print("Não é possível dividir por zero.")

# Chama a função da calculadora
calculadora()