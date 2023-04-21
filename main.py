from collections import deque
from os import system
from time import sleep

def menu_principal():
    system("cls")
    print("\nMENU PRINCIPAL\n1 - Operações\n2 - Expressão\n0 - Finalizar Programa")
    # Acredito ser o equilíbrio entre ter as informações mantidas sem perder tudo do nada e não deixar o terminal extremamente poluído
    print("\nOBS: Quando uma ou mais operações forem realizadas no menu de OPERAÇÕES, elas serão apagadas da fila e do terminal (funcional e visualmente).")
    escolha = input()
    if escolha == '1':
        operações(filaTotal)
    elif escolha == '0':
        system("cls")
        print("\nPrograma finalizado.\nVolte sempre, obrigado!\n")
        return
    else:
        print("Opção inválida, retornado ao MENU PRINCIPAL...")
        sleep(2)
        menu_principal()

def operações(ft: deque):
    system("cls") 
    print("\nOPERAÇÕES\n1 - Adicionar Operação na Fila\n2 - Executar Próxima Operação da Fila")
    print("3 - Executar Todas as Operações da Fila\n0 - Voltar para o MENU PRINCIPAL")
    escolha = input()
    if escolha == '1':
        system("cls")
        print("\n1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)")
        escolha = input()
        # Essa verificação existe aqui para que não haja necessidade de verificar durante a execução das operações
        if escolha not in ('1', '2', '3', '4'):
            print("\nOperação inválida, retornando ao menu de OPERAÇÕES...")
            sleep(2)
            operações(filaTotal)
        system("cls")
        print('\nDigite quantos valores quiser e "fim" para encerrar a inserção de valores:')
        fila = deque([int(escolha)])
        while True:
            valor = input()
            if valor == "fim":
                break
            else:
                try:
                    fila.append(float(valor))
                except ValueError:
                    print('O valor inserido não se trata de um valor numérico (lembre-se, para encerrar a inserção, digite "fim").')
        ft.append(fila)
        system("cls")
        operações(filaTotal)
    elif escolha == '2':
        # Necessário para caso o usuário selecione para executar a próxima operação na fila quando a mesma estiver vazia
        try:
            if ft[0][0] == 1:
                system("cls")
                adição(ft[0])
            elif ft[0][0] == 2:
                system("cls")
                subtração(ft[0])
            elif ft[0][0] == 3:
                system("cls")
                multiplicação(ft[0])
            else:
                system("cls")
                divisão(ft[0])
            ft.popleft()
            input("\nEsses dados não são armazenadas em lugar algum, dê uma boa olhada neles antes que desapareçam. Prossiga digitando qualquer tecla: ")
            operações(filaTotal)
        except IndexError:
            system("cls")
            print("\nA fila de operações está vazia, retornando ao menu de OPERAÇÕES...")
            sleep(2)
            operações(filaTotal)
    elif escolha == '0':
        menu_principal()

def adição(filaOp: deque):
    print("\nAdição\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    for i in filaOp:
        print(i, end=" | ")
    print("\nResultado:", sum(filaOp))
    
def subtração(filaOp: deque):
    print("\nSubtração\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    sub = filaOp.popleft() # Tirando o primeiro número da operação e o atribuindo a sub para meios de cálculo
    print(sub, end=" | ") # Printando esse único valor fora do loop (já que ele "não faz mais parte da lista")
    for i in filaOp:
        print(i, end=" | ")
        sub -= i
    print("\nResultado:", sub)

def multiplicação(filaOp: deque):
    print("\nMultiplicação\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    multi = 1
    for i in filaOp:
        print(i, end=" | ")
        multi *= i
    print("\nResultado:", multi)

def divisão(filaOp: deque):
    print("\nDivisão\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    div = filaOp.popleft() # Tirando o primeiro número da operação e o atribuindo a div para meios de cálculo
    print(div, end=" | ") # Printando esse único valor fora do loop (já que ele "não faz mais parte da lista")
    for i in filaOp:
        print(i, end=" | ")
        div /= i
    print("\nResultado:", div)

filaTotal = deque()
menu_principal()