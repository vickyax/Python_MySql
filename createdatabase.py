import mysql.connector
import config

mydb = mysql.connector.connect(
    host = config.Host,
    user = config.User,
    password = config.Password,
)
query = mydb.cursor()

query.execute("CREATE DATABASE pydb")

mydb.close()