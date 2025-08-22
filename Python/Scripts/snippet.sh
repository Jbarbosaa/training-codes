#1. Aplicando for

#Bash
for i in {1..5}; do
    echo "Contagem :$i"
done

#Python
for i in range (1,6):
    print (f"Contagem: {i}")

**
#2. Váriáveis
BASH: NOME="Julio" ; echo $NOME
PYTHON: nome="Julio" ; print (nome)

**
#3. Leitura de arquivos

BASH : 
while read linha; done
    echo "$linha"
done > arquivo.txt

Python :
with open ("Arquivo.txt") as f:
    for linha in f:
        prit (linha.strip())

*
#4. Argumentos no script

#Bash
#Declarar variável !#/bin/bash
echo "Primeiro arg: $1"

#Python
import sys
print (f"Primeiro arg: {sys.argv{1}}" )

#Desafio listar arquivos de um diretório

#Bash
ls -l > list.txt

#Python
import os

with open ("list.txt", "w") as f:
    for arquivo in os.listdir ("."):
        f.write(arquivo + "\n")