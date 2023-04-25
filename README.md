Projeto Pilha e Fila de Estrutura de Dados
------------------------------------------

## Ideia

Consiste no uso dos conceitos de Pilha e Fila em um programa que funciona como console, possuindo Menu Principal e Menu de Operações.

## Opções

### Menu Principal

1. Ir para o menu de Operações.
2. Finalizar o programa.

### Menu de Operações

1. Adicionar uma operação à fila.
2. Executar a próxima operação da fila.
3. Executar todas as operações da fila.
4. Retornar ao Menu Principal.

## Observação

Na linha 57 da main.py foi necessário o uso de um try-except statement, usá-lo foi a maneira mais simples de corrigir um bug encontrado
quando a fila estava vazia: em ambas escolhas 2 e 3, a função operações() aparentava ser chamada duas vezes seguidas (mesmo tendo apenas
uma chamada no script) e(ou), na primeira chamada, caía automaticamente no escopo da opção 2.