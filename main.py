from queue import Queue
from queue import LifoQueue
from time import sleep
from os import system

def menu_principal():
    system("cls")
    print("MENU PRINCIPAL\n1 - Operações\n2 - Expressão\n0 - Finalizar Programa")
    print("\nOBS: Quando uma ou mais operações forem realizadas no menu de OPERAÇÕES, elas serão apagadas da fila e do terminal (funcional e visualmente).")
    escolha = input()
    if escolha == '1':
        operações(filaTotal)
    elif escolha == '0':
        system("cls")
        print("Programa finalizado.\nVolte sempre!\n")
        return
    else:
        system("cls")
        print("Opção inválida, retornado ao MENU PRINCIPAL...")
        sleep(1)
        menu_principal()

def operações(ft: Queue):
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
            print("Operação inválida, retornando ao menu de OPERAÇÕES...")
            sleep(1)
            operações(filaTotal)
        else:
            system("cls")
            print('Digite quantos valores quiser e "fim" para encerrar a inserção de valores:')
            fila = Queue()
            fila.put(int(escolha))
            while True:
                valor = input()
                if valor == "fim":
                    break
                else:
                    try:
                        fila.put(float(valor))
                    except ValueError:
                        print('O valor inserido não se trata de um valor numérico (lembre-se, para encerrar a inserção, digite "fim").')
            if fila.qsize() > 2: # A fila precisa ter pelo menos 2 valores para que uma operação se realize (o primeiro sendo a representação da operação em si)
                ft.put(fila)
            operações(filaTotal)
    elif escolha == '2':
        system("cls")
        if not ft.empty():
            manipulação_fila(ft.get())
            input("Esses dados não são armazenadas em lugar algum, dê uma boa olhada neles antes que desapareçam. Aperte ENTER ")
            operações(filaTotal)
        else:
            print("A fila está vazia, retornando ao menu de OPERAÇÕES...")
            sleep(2)
            operações(filaTotal)
    elif escolha == '3':
        system("cls")
        if not ft.empty():
            while ft.qsize() > 0:
                manipulação_fila(ft.get())
                sleep(0.5)
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

def manipulação_fila(primeiraFila: Queue):
    op = primeiraFila.get() # Atribuindo o primeiro número da fila (que representa a operação) à variável op
    if op == 1:
        adição(primeiraFila)
    elif op == 2:
        subtração(primeiraFila)
    elif op == 3:
        multiplicação(primeiraFila)
    else:
        divisão(primeiraFila)

def adição(filaOp: Queue):
    print("Adição\nValores:", end=' ')
    soma = 0
    while not filaOp.empty():
        i = filaOp.get()
        print(i, end=" | " if 0 < filaOp.qsize() else '') # Apenas para fins estéticos
        soma += i
    print("\nResultado:", soma, "\n")
    
def subtração(filaOp: Queue):
    print("Subtração\nValores:", end=' ')
    sub = i = filaOp.get() # Tirando o primeiro número da operação e o atribuindo a sub e i para meios de cálculo
    print(i, end=" | ") # Printando esse único valor fora do loop pois será posteriormente manipulado
    while not filaOp.empty():
        i = filaOp.get()
        print(i, end=" | " if 0 < filaOp.qsize() else '') # Apenas para fins estéticos
        sub -= i
    print("\nResultado:", sub, "\n")

def multiplicação(filaOp: Queue):
    print("Multiplicação\nValores:", end=' ')
    multi = 1
    while not filaOp.empty():
        i = filaOp.get()
        print(i, end=" | " if 0 < filaOp.qsize() else '') # Apenas para fins estéticos
        multi *= i
    print("\nResultado:", multi, "\n")

def divisão(filaOp: Queue):
    print("Divisão\nValores:", end=' ')
    div = i = filaOp.get() # Tirando o primeiro número da operação e o atribuindo a div e i para meios de cálculo
    print(i, end=" | ") # Printando esse único valor fora do loop pois será posteriormente manipulado
    while not filaOp.empty():
        i = filaOp.get()
        print(i, end=" | " if 0 < filaOp.qsize() else '') # Apenas para fins estéticos
        try:
            div /= i
        except ZeroDivisionError:
            pass # Apenas ignorando o valor 0 digitado
    print("\nResultado:", div, "\n")

filaTotal = Queue()
menu_principal()