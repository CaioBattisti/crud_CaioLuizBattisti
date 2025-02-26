import mysql.connector
from config import MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE)
def create_user(nome, telefone,email,usuario,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert usuario(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome,telefone,email,usuario,senha))
    conn.commit()
    cursor.close()
    conn.close()