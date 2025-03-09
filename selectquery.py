import mysql.connector

import config

mydb = mysql.connector.connect(
    host = config.Host,
    user = config.User,
    password = config.Password,
    database = config.Database
)
query = mydb.cursor()

query.execute("SELECT * FROM customers")

print(query.fetchall())

mydb.close()
