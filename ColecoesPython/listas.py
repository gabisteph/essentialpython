"""
Listas

Listas em python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem dinâmicos
e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    Será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em python:

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionar elementos;
- Qualquer tipo de dado: não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em python são representadas por colchetes: []
# Exemplos de listas
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))


lista5 = list('Geek University')


# podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'encontrei o número {num} ')
else:
    print(f'não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)


# Podemos contar o número de ocorrência de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elemento em listas

Para adicionar elementos em listas, utilizamos a função append
OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
lista1. append(12, 34, 56) # Erro

print(lista1)
lista1.append(42)
print(lista1)

# mas é possível o seguinte exemplo
lista1.append([8, 3, 11])  # Coloca a lista como elemento único (sublista)
print(lista1)
if [8, 3, 11] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Colocar cada elemento da lista como valor
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)
# Podemos facilmente juntar duas listas
# lista6 = lista1 + lista2
lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista utilizando reverse

Forma 1

# lista1.reverse()
# lista2.reverse()
#
# print(lista1)
# print(lista2)

Forma 2
print(lista1[::-1])
print(lista2[::-1])


# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Tamanho da lista
print(len(lista3))

# Remover o último elemento de uma lista
# OBS: O pop remove e retorna o último elemento que ele removeu
print(lista5)
lista5.pop()
print(lista5)

# Remover o elemento pelo índice
# Os elementos á direita deste índice serão deslocados a esquerda
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos da lista
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para uma lista

# Exemplo 1
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,python:,essencial'
print(curso)
curso = curso.split(',')
print(curso)

# convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)
# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)
# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dadosDD
lista6 = [1, 2.45, True, 'Geek', 'd', [1, 2, 3], 234532453244]

# Utilizando For
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# Utilizando While
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num4]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

# __________0________1__________2________3__
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo
# Onde o final de um elemento está ligado ao início da lista

print(cores[-1])  # Branco
print(cores[-2])  # Azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
print(cores[-5])  # Erro, pois não existe índice -5
cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)
# lista aceitam repetição

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print((numeros.index(9)))

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
# print(numero.index(19)) retorna erro
# OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca em um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1))  # Buscando a partir do índice 1
print(numeros.index(5, 2))  # Buscando a partir do índice 2
print(numeros.index(5, 3))  # Buscando a partir do índice 3


# Podemos fazer busca em um range, inicio e fim
print(numeros.index(8, 3, 8))  # Buscar o índice do valor 8, entre 3 e 6

# Revisão de slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:4])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com parâmetro passo:

print(lista[1::2]) # Começa do 1 e pega até o final, de dois em 2

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # Máximo valor
print(min(lista))  # Mínimo valor
print(len(lista))  # tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# shallow copy

lista = [1, 2, 3]
print(lista)

nova = lista  # Cópia

nova.append(4)

print(lista)
print(nova)

"""
