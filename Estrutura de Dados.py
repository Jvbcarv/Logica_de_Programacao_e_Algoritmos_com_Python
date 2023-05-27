#Nome Jovana Vilas Bôas de Carvalho \
# RU 1268527

#algoritmo de busca: busca sequencial
def busca_sequencial(lista, elemento_procurado):
    contador = 0 #variável que armazenará quantas vezes o elemento procurado aparecerá na lista.
    for elemento in lista:
        if elemento == elemento_procurado: #se o elemento atual encontrado pela variável 'elemento' for igual\
            # ao 'elemento_procurado', é incrementado contador em 1.
            contador += 1
    return contador #retorna o valor do contador contendo o número de vezes que o elemento_procurado aparece na lista.

lista = [23, 4, 67, 54, 90, 21, 54, 5, 29, 54]
elemento = 54

quantidade = busca_sequencial(lista, elemento) #a variável 'quantidade' chama a função 'busca_sequencial'\
# O retorno da função, que é o número de ocorrências do elemento na lista, é armazenado na variável quantidade.
mensagem = "O elemento {} aparece {} vezes na lista.".format(elemento, quantidade)
print(mensagem)
