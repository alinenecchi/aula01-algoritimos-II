import mysql.connector

conn = mysql.connector.connect(host='localhost', database='ap2_loja', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    result = cursor.fetchall()

    for produto in result:
        texto = str(produto[0]) + ": " + produto[1] + "-" + str(produto[2])
        print(texto)
    id = input("Digite o id do produto que deseja excluir: ")
    cursor.execute("DELETE FROM produtos WHERE id= " + str(id))
    conn.commit()
    
    cursor.execute("SELECT * FROM produtos")
    result = cursor.fetchall()
    for produto in result:
        texto = str(produto[0]) + ": " + produto[1] + "-" + str(produto[2])
        print(texto)
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")