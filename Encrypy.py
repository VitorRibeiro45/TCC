import shutil
import os
import sys
from art import *
import pymysql as MySQLdb
import pymysql.cursors
import random
import subprocess


# base crypto

def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("cry" + filename, "wb")
    file.write(data)
    file.close()


def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, "wb")
    file.write(data)
    file.close()


# Connect banco de dados
conexao = MySQLdb.connect(host='localhost',
                          user='root',
                          password='',
                          database='TESTE1',
                          cursorclass=pymysql.cursors.DictCursor)

banco = conexao.cursor()

banco.execute("select usuario, senha from clientes;")

usuario = ''
senha = ''

for linha in banco.fetchall():
    for coluna in linha:
        if (coluna == 'usuario'):
            usuario = linha[coluna]
        else:
            senha = linha[coluna]

conexao.close()

tprint("ENCRYPY")
print("Cuidado, senha inválida resulta na remoção do arquivo")

random.seed()
valor = usuario + senha
insert_senha = 0
insert_user = 0
tentativas = 2
while insert_senha != valor:
    insert_user = (input("Digite o usuario: "))
    insert_senha = (input("Digite a senha: "))
    tentativas = tentativas + 1
    if insert_senha == senha and insert_user == usuario:
        print("Sucess")
        break
    else:
        print("Deletando")
        dir = os.getcwd()
        os.remove(dir+'\%s' % sys.argv[0])
        sys.exit()

choice = ""
while choice != "3":
    print("\nSELECIONE A OPÇÃO")
    print("1. CRIPTOGRAFAR")
    print("2. DECRIPTOGRAFAR")
    print("3. QUIT")
    choice = input()
    if choice == "1" or choice == "2":
        key = int(input("INSIRA A CHAVE!\n"))
        filename = input("INSIRA O NOME DO ARQUIVO COM A EXTENSÃO:\n")
    if choice == "1":
        Encrypt(filename, key)
        os.remove(filename)
    if choice == "2":
        Decrypt(filename, key)
