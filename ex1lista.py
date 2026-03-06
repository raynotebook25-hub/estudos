# lista de numeros de 1 a 5 

numeros = [1, 2, 3, 4, 5]

print(numeros)

#lista de vogais 

vogais = ["a", "e", "i", "o", "u"]

print(vogais)

# Voce pode coverter outros tipos de dados iteraveis (strings, tuplas, conjuntos) em lista usando a função 'list()'
# minha_string = hello
#lista_da_string = list(minha_string)

#           ACESSANDO VALORES DE UMA LISTA 

#PELO INDICE
# se quiser exibir apenas um dos valores guardados na lista basta especificar a posição (indice)
# da lista onde o valor desejado se encontra
# SEMPRE começa pelo numero ZERO 

# ex: valores = [10, 3, 5] o indice do "10" para identificar é  0, do "3" é 1, do "5" é 2.

#notas = ["Rayssa", 21, True, 1.63, False]

#print(notas[3])

# pode se usar numeros negativos para acessar os elementos de uma lista. 
# o -1 representa o ultimo elemento, o -2 o penultimo, e assim vai.

#print(notas[-1]) # printa o false

#              MANIPULAÇÃO DE LISTAS 

# Adição de itens : .append()  --> adiciona um elemnto ao final da lista 
# Adição de itens : .insert()  --> adiciona um ele mento na posição informada 
# Remoção de itens : .removed() --> Remover um elemento de uma lista atraves do seu valor
# Remoçao de itens : .pop()  --> Remover um elemento de uma lista atraves do seu indice

#valores = [1, 2, 3, 4, 5, 6, 7, 8]

#valores.append(9)
#print(valores) # adiciona o 9 ao final da lista quando printar 

#valores.insert(3, 3.5) # insere o 3.5 na posição 3 quando printar 

#pessoas = ["ray", "ju", "benicio", "gabi", "ruan"]

#pessoas.pop(2) # remove "benicio" da lista quando printar 

#pessoas.remove("benicio") #remove benicio da lista quando printar

#   USANDO FOR NA LISTA

lista_compras = [
    "2 pacote de arroz",
    "6 pacote de milho",
    "4kg de carne muida",
    "1 couve",
    "2 pacote de feijão",
    "5 unidades de laranja",
    "1 coca cola",
]

print("LISTA DE COMPRAS", end='\n\n') #\n siginifica pular uma linha 
for item in lista_compras:
    print("[ ]", item)