print('Bem-vindo(a) a loja Ponto da Moda!')
#Dados de entrada:
preco = float(input('Entre com o valor unitário do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))
subtotal = preco * quantidade
#Aplicação de desconto utilizando if, elif e else:
if subtotal <= 4:
    valorfinal = subtotal
elif subtotal >= 5 and subtotal <= 19:
    valorfinal = subtotal - subtotal * 0.03
elif subtotal >= 20 and subtotal <= 99:
    valorfinal = subtotal - subtotal * 0.06
else:
    valorfinal = subtotal - subtotal * 0.10
    # Resultados
print('O valor sem desconto foi de R$ {:.2f}.'.format(subtotal))
print('O valor com desconto foi de R$ {:.2f}.'.format(valorfinal))
