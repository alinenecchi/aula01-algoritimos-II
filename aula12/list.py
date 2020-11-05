import mysql.connector

conn = mysql.connector.connect(host='localhost', database='ap2_loja', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    result = cursor.fetchall()

    for produto in result:
        print("Nome: ", produto[0], "- ", produto[1], "-", produto[2])
        print("---------------------------------------------------")
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")