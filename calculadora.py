# Função para adição
def adicao(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para multiplicação
def multiplicacao(x, y):
    return x * y

# Função para divisão
def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Divisão por zero não é permitida."

# Menu da calculadora
def menu():
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

# Loop principal
while True:
    menu()

    # Solicitar a escolha da operação
    escolha = input("Digite a opção (1/2/3/4/5): ")

    # Verificar se a escolha é válida
    if escolha in ('1', '2', '3', '4'):
        # Solicitar os operandos
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números válidos.")
            continue

        # Realizar a operação escolhida
        if escolha == '1':
            print(num1, "+", num2, "=", adicao(num1, num2))
        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))
        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))
        elif escolha == '4':
            resultado = divisao(num1, num2)
            print(num1, "/", num2, "=", resultado)
        elif escolha == '5':
            print("Calculadora encerrada.")
        break
    
    else:
        print("Escolha inválida. Tente novamente.")
