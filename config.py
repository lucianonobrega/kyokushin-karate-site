#cria a conexão com o banco de dados
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="black_wolves_database"
)