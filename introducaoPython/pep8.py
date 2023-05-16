"""
PEP8 - Proposta de melhoras para a linguagem python

The zen of python

import this

A ideia de PEP8 é que possamos escrever códigos python de forma Pythônica.

[1] - Utilize Camel Case para nomes de Classes:

Ex: class Calculadora:
        pass

    class CalculadoraCientifica:
        pass
[2] Utilize nome em minúsculo, separados por underline para funções ou variáveis:

Ex:  def soma():
        pass
    def soma_dois():
        pass

[3] - utilize 4 espaços para identação! (não use TAB)

[4] - 2 linhas em branco: separar funções  e definições, métodos dentro de uma class devem ser separados com uma única linha em branco

[5] - imports devem ser feitos em linhas separadas
EX: import Errado: import sys, os
    import certo: import sys
                  import os
obs: há problemas em ex: from types import StringType, ListType
Caso tenha muitos importes recomenda-se: from type import { blablab,
                                                            blablaj,
                                                            }
import devem estar sempre no toṕo do arquivo logo depois de quaisquer comentários ou docstrings e antes de constantes ou variáveis globais.

[6] Espaços em expressões e instruçoes:

     não faça:  função( algo: 1 }
[7] termine sempre uma instrução com uma nova linha
   # insira sua instrução aqui
   linha em branco

"""