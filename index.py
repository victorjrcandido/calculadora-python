import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
    while True:
        input_operacao = input("1 : somar\n2 : subtrair\n3 : multiplicar\n4 : dividir\nSelecione o tipo de operacao: ")
        if input_operacao in ["1", "2", "3", "4"]:
            break
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")

    operador = None
    resultado = None
    input_num1 = int(input("Digite o primeiro número: "))
    input_num2 = int(input("Digite o segundo número: "))

    if input_operacao == "1":
        resultado = input_num1 + input_num2
        operador = "+"
    if input_operacao == "2":
        resultado = input_num1 - input_num2
        operador = "-"
    if input_operacao == "3":
        resultado = input_num1 * input_num2
        operador = "*"
    if input_operacao == "4":
        resultado = input_num1 / input_num2
        operador = "/"

    print(input_num1, operador, input_num2, "=", resultado)

    while True:
        input_continuar = input("Deseja fazer outra operação? S ou N: ")
        if input_continuar in ["S", "s", "N", "n"]:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    if input_continuar == "N" or input_continuar == "n":
        print("Obrigado por usar a calculadora!")
        exit()
    
    if input_continuar == "S" or input_continuar == "s":
        clear()