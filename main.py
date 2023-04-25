from collections import deque
from queue import LifoQueue
from time import sleep
from os import system

def menu_principal():
    system("cls")
    print("MENU PRINCIPAL\n1 - Operações\n2 - Expressão\n0 - Finalizar Programa")
    escolha = input()
    if escolha == '1':
        operações(filaTotal)
    elif escolha == '0':
        system("cls")
        print("Programa finalizado.\nVolte sempre!\n")
        return
    else:
        system("cls")
        print("Opção inválida, retornado ao menu principal...")
        sleep(1)
        menu_principal()

def operações(ft: deque):
    system("cls")
    print("OPERAÇÕES\n1 - Adicionar Operação à Fila\n2 - Executar Próxima Operação da Fila")
    print("3 - Executar Todas as Operações da Fila\n0 - Voltar para o menu principal")
    escolha = input()
    if escolha == '1':
        system("cls")
        print("1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)")
        escolha = input()
        # Essa verificação existe aqui para que não haja necessidade de verificar durante a execução das operações
        if escolha not in ('1', '2', '3', '4'):
            system("cls")
            print("Operação inválida, retornando ao menu de operações...")
            sleep(1)
            operações(filaTotal)
        else:
            system("cls")
            print('Digite quantos valores quiser e "fim" para encerrar a inserção de valores:')
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
            operações(filaTotal)
    elif escolha == '2':
        system("cls")
        manipulação_fila(ft)
        # Contexto do bug referenciado na README abaixo
        try:
            ft.popleft()
            input("Esses dados não são armazenadas em lugar algum, dê uma boa olhada neles antes que desapareçam. Aperte ENTER ")
            operações(filaTotal)
        except IndexError:
            pass
    elif escolha == '3':
        system("cls")
        if len(ft) > 0:
            i = 0
            while i < len(ft):
                manipulação_fila(ft, i) # Passando a fila total e o index da "subfila" como parâmetros
                i += 1
            ft.clear()
            input("Esses dados não são armazenadas em lugar algum, dê uma boa olhada neles antes que desapareçam. Aperte ENTER ")
            operações(filaTotal)
        else:
            system("cls")
            print("A fila de operações está vazia, retornando ao menu de OPERAÇÕES...")
            sleep(2)
            operações(filaTotal)
    elif escolha == '0':
        menu_principal()
    else:
        system("cls")
        print("Opção inválida, retornando ao menu de OPERAÇÕES...")
        sleep(2)
        operações(filaTotal)

def manipulação_fila(filaInteira: deque, index=0):
    try: # Necessário para caso a fila estiver vazia
        if filaInteira[index][0] == 1:
            adição(filaInteira[index])
        elif filaInteira[index][0] == 2:
            subtração(filaInteira[index])
        elif filaInteira[index][0] == 3:
            multiplicação(filaInteira[index])
        else:
            divisão(filaInteira[index])
    except IndexError:
        print("A fila de operações está vazia, retornando ao menu de OPERAÇÕES...")
        sleep(2)
        operações(filaTotal)

def adição(filaOp: deque):
    print("Adição\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    for i in filaOp:
        print(i, end=" | ")
    print("\nResultado:", sum(filaOp), "\n")
    
def subtração(filaOp: deque):
    print("Subtração\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    sub = filaOp.popleft() # Tirando o primeiro número da operação e o atribuindo a sub para meios de cálculo
    print(sub, end=" | ") # Printando esse único valor fora do loop (já que ele "não faz mais parte da lista")
    for i in filaOp:
        print(i, end=" | ")
        sub -= i
    print("\nResultado:", sub, "\n")

def multiplicação(filaOp: deque):
    print("Multiplicação\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    multi = 1
    for i in filaOp:
        print(i, end=" | ")
        multi *= i
    print("\nResultado:", multi, "\n")

def divisão(filaOp: deque):
    print("Divisão\nValores:", end=' ')
    filaOp.popleft() # Tirando o inteiro que representa a operação
    div = filaOp.popleft() # Tirando o primeiro número da operação e o atribuindo a div para meios de cálculo
    print(div, end=" | ") # Printando esse único valor fora do loop (já que ele "não faz mais parte da lista")
    for i in filaOp:
        print(i, end=" | ")
        div /= i
    print("\nResultado:", div, "\n")

filaTotal = deque()
menu_principal()