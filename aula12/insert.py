import mysql.connector

conn = mysql.connector.connect(host='localhost', database='ap2_loja', user='root', password='')

if conn.is_connected():
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    preco = preco.replace(",", ".")

    query = "INSERT INTO produtos (nome, preco) VALUES ( "
    query += " '" + nome + "' , " + preco + ")"

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")