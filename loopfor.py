"""
Loop for

loop -> é uma estrutura de repetição
for -> uma dessas estruturas

C ou Java

for (int i=0; i < limitador; i++){
    //execução do loop
}

Python

for item i interavel:
    //execução do loop

Utilizamos loop para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:

- string
    nome = 'Geek university'
-lista
    lista = [1,2,3,4,5]
- Range
    numeros = range (1,10)


#Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

#Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)

Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' ') ...)

for indice, letra in enumarate(nome):
    print(nome[indice])


for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
OBS: Quando não precisamos de um valor descartamos com um underline

nome = 'Geek University'
lista = [1, 3, 4, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])
for n in range(1,qtd+1):
    print(f'Imprimindo {n}')

qtd = int(input("quantas vezes esse loop deve rodar ? "))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')


nome = 'Gabrielle Stephanie'
for letra in nome:
    print(letra, end='')

emoji = '\U0001F60D'

for num in range(1, 11):
    print(f'{emoji * num}')



"""

