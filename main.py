def adicao(x, y):
    return x + y;

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y !=0:
        return x / y
    else:
        return "Divisão por zero não é permitido"
    
def menu():
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    menu() 

    Escolha = input("Digite a opção (1/2/3/4/5)")

    if Escolha in('1', '2', '3', '4'):

        num1= float(input("Digite o primeiro número: "))
        num2= float(input("Digite o segundo número: "))

        if Escolha == '1':
            print(num1,"+", num2, "=", adicao(num1, num2))
        elif Escolha == "2":
            print(num1, "-", num2, "=", subtracao(num1, num2))
        elif Escolha == "3":
            print(num1, "*", num2, "=", multiplicacao(num1, num2))
        elif Escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))

    elif Escolha == '5':
        print("Calculadora encerrada.")
        break
    else:
        print("Escolha inválida. Tente novamente.")


