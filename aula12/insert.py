# encoding: utf-8
import mysql.connector
from FormProduto import FormProduto
from Produto import Produto

conn = mysql.connector.connect(host='localhost', database='ap2_loja', user='root', password='')
if conn.is_connected():
    # nome = input("Digite o nome do produto:")
    # preco = input("Digite o preço: ")
    # preco = preco.replace( "," , ".")
    form = FormProduto()
    produto = form.show()

    if produto != None:

        query = "INSERT INTO produtos (nome, preco) VALUES ( "
        query += " '" + produto.nome + "' , " + str( produto.preco ) + " ) "

        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        cursor.close()
        conn.close()
else: 
    print( "Não foi possível conectar ao banco") 









