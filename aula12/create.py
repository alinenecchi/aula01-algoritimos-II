import mysql.connector

# conecção com banco de dados
conn = mysql.connector.connect(host='localhost', database='ap2_loja', user='root', password='')

# testando a conexão com Banco de Dados
if conn.is_connected():
    info = conn.get_server_info()
    print("Conectado ao MySQL", info)
    print("------------------")
    print("Tabelas existentes")

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    for linha in cursor:
        print(linha)
    print("----------------------")
    # criando tabela
    query = "CREATE TABLE IF NOT EXISTS produtos ( "
    query += " id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, "
    query += " nome VARCHAR(100) NOT NULL, "
    query += " preco DOUBLE ) "
    cursor.execute(query)

    print("Tabelas existentes")
    cursor.execute("SHOW TABLES")
    for linha in cursor:
        print(linha)
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco")