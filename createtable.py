import mysql.connector
import config

mydb = mysql.connector.connect(
    host = config.Host,
    user = config.User,
    password = config.Password,
    database = config.Database
)

query = mydb.cursor()

sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

query.execute(sql)

mydb.close()