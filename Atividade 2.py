# Meu identificador:
print('Bem-Vindo(a) a Pizzaria Imperial!')
# Cardápio/tabela de preços:
print('-----------------------Cardápio-----------------------------')
print('| Código |  Descrição  | Pizza Média - M | Pizza Grande - G |')
print('|   21   |  Napolitana |    R$ 20,00     |     R$ 26,00     |')
print('|   22   |  Margherita |    R$ 20,00     |     R$ 26,00     |')
print('|   23   |  Calabresa  |    R$ 25,00     |     R$ 32,50     |')
print('|   24   |  Toscana    |    R$ 30,00     |     R$ 39,00     |')
print('|   25   |  Portuguesa |    R$ 30,00     |     R$ 39,00     |')
print('------------------------------------------------------------\n')

# Loop principal:
acumulador = 0

while True:
    tamanho = input('Qual o tamanho de pizza que deseja (M ou G)?: ')
    # Opção de tamanho M e código da pizza (if, elif e else):
    if (tamanho == 'M'):
        codigo = int(input('Entre com o código do sabor desejado: '))
        if (codigo == 21):
            print('Você pediu uma Pizza Napolitana')
            acumulador = acumulador + 20
        elif (codigo == 22):
            print('Você pediu uma Pizza Margherita')
            acumulador = acumulador + 20
        elif (codigo == 23):
            print('Você pediu uma Pizza Calabresa')
            acumulador = acumulador + 25
        elif (codigo == 24):
            print('Você pediu uma Pizza Toscana')
            acumulador = acumulador + 30
        elif (codigo == 25):
            print('Você pediu uma Pizza Portuguesa')
            acumulador = acumulador + 30
        else:
            print('Opção Inválida') #caso a pessoa digite uma opção diferente aparecerá a mensagem de opção inválida
            continue #continue para voltar para o início do while

    # Opção de tamanho G e código da pizza (if, elif e else):
    elif (tamanho == 'G'):
        codigo = int(input('Entre com o código do sabor desejado: '))
        if (codigo == 21):
            print('Você pediu uma Pizza Napolitana')
            acumulador = acumulador + 26
        elif (codigo == 22):
            print('Você pediu uma Pizza Margherita')
            acumulador = acumulador + 26
        elif (codigo == 23):
            print('Você pediu uma Pizza Calabresa')
            acumulador = acumulador + 32.50
        elif (codigo == 24):
            print('Você pediu uma Pizza Toscana')
            acumulador = acumulador + 39
        elif (codigo == 25):
            print('Você pediu uma Pizza Portuguesa')
            acumulador = acumulador + 39
        else:
            print('Opção Inválida') #caso a pessoa digite uma opção diferente aparecerá a mensagem de opção inválida
            continue #continue para voltar para o início do while
    else:
        print('Opção Inválida')
        continue #continue para voltar para o início do while

    print('O valor a ser pago está em: R$ {:.2f}.'.format(acumulador))
    # Repetir loop principal se caso o cliente quiser mais alguma coisa:
    resposta = input('Deseja pedir mais alguma coisa? 1 - Sim e 0 - Não: ')
    if resposta == '1':
        continue
    else:
        print("O valor final será de R$ {:.2f}.".format(acumulador))
        break #break para sair do while
