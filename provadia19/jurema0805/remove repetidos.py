# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# remove todas os carateres repetidos
# ----------------------------------------------------------
lista=input()
#remove os repetidos com metodo set()
unicos=list(set(lista))
#converte lista em string
str1=''.join(unicos)
print(str1)