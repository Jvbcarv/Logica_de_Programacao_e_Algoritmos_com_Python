#---------Começo da Função volumeFeijoada-------------------
def volumeFeijoada():
    while True:
        try:
            print('Menu Volume Feijoada')
            volume = float(input('Entre com a quantidade que deseja (ml): '))
            if (300 <= volume <= 5000):
                valor = volume * 0.08
                return valor
            else:
                print('Não aceitamos porções menores que 300 ml ou maiores que 5.000 ml. Tente novamente.')
                continue
        except ValueError:
            print('Digite um valor numérico. Tente novamente.')
            continue

#----------Fim da Função volumeFeijoada-------------------

#----------Começo da Função opcaoFeijoada-----------------
def opcaoFeijoada():
    while True:
        print('Menu Opção Feijoada')
        opcao = input('Entre com a opção de Feijoada: \nb - Básica (Feijão + paiol + costelinha) \np - Premium (Feijão + paiol +costelinha + partes de porco) \ns - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\n>>')
        if (opcao == 'b'):
            multiplicador = 1
        elif (opcao == 'p'):
            multiplicador = 1.25
        elif (opcao == 's'):
            multiplicador = 1.50
        else:
            print('Você não digitou uma opção válida. Tente novamente.')
            continue
        break
    return multiplicador
#----------Fim da Função opcaoFeijoada------------------

#----------Começo da Função acompanhamentoFeijoada-----------------
def acompanhamentoFeijoada():
    while True:
        print('Menu Acompanhamento Feijoada')
        adicional = 0
        acompanhamento = int(input('Deseja mais algum acompanhamento? \n0- Não desejo mais acompanhamentos (encerrar pedido) \n1- 200g de arroz  \n2- 150g de farofa especia \n3- 100g de couve cozida \n4- 1 laranja descascada\n>>'))
        if (acompanhamento == 0):
            return 0
        elif (acompanhamento == 1):
            return 5
        elif (acompanhamento == 2):
            return 6
        elif (acompanhamento == 3):
            return 7
        elif (acompanhamento == 4):
            return 3
        else:
            print('Você não digitou uma opção válida. Tente novamente.')
            continue
        break
        # ----------Fim da Função acompanhamentoFeijoada-----------------

# ------------------Começo da Main:------------------------------
print('Bem-vindo(a) à Feijoada da Casa Mineira!')

# Cálculo do valor total:
volume = volumeFeijoada()
opcao = opcaoFeijoada()
adicional = acompanhamentoFeijoada()
total = (volume * opcao) + adicional
print('O valor a ser pago é (R$): {:.2f} (volume = {:.2f} * opção = {:.2f}) + acompanhamento = {:.2f})'
              .format(total, volume, opcao, adicional))

# ------------------Fim da Main------------------------------
