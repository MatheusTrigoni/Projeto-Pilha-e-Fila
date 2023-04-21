from collections import deque
import time

def menu_principal():
    print("\nMENU PRINCIPAL\n1 - Operações\n2 - Expressão\n0 - Finalizar Programa")
    escolha = input()
    if escolha == '1':
        operações(filaTotal)
    elif escolha == '0':
        print("\nPrograma finalizado.\n")
        return
    else:
        print("Opção inválida, retornado ao menu principal...")
        time.sleep(1)
        menu_principal()

def operações(ft: deque):
    print("\nOPERAÇÕES\n1 - Adicionar Operação na Fila\n2 - Executar Próxima Operação da Fila")
    print("3 - Executar Todas as Operações da Fila\n0 - Voltar para o menu principal")
    escolha = input()
    if escolha == '1':
        print("\n1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)")
        escolha = input()
        # Essa verificação existe aqui para que não haja necessidade de verificar durante a execução das operações
        if escolha not in ('1', '2', '3', '4'):
            print("\nOperação inválida, retornando ao menu de operações...")
            time.sleep(1)
            operações(filaTotal)
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
        operações(filaTotal)
    elif escolha == '2':
        # Necessário para caso o usuário selecione para executar a próxima operação na fila quando a mesma estiver vazia
        try:
            if ft[0][0] == 1:
                adição(ft[0])
                ft.popleft()
                time.sleep(3)
                operações(filaTotal)
            elif ft[0][0] == 2:
                subtração(ft[0])
                ft.popleft()
                time.sleep(3)
                operações(filaTotal)
            elif ft[0][0] == 3:
                multiplicação(ft[0])
                ft.popleft()
                time.sleep(3)
                operações(filaTotal)
            else:
                divisão(ft[0])
                ft.popleft()
                time.sleep(2)
                operações(filaTotal)
        except IndexError:
            print("\nA fila de operações está vazia, retornando ao menu de operações...")
            time.sleep(2)
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