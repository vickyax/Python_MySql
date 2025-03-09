import mysql.connector
import config

mydb = mysql.connector.connect(
    host = config.Host,
    user = config.User,
    password = config.Password,
    database = config.Database
)
query = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
query.execute(sql,val)
mydb.commit()

print(query.rowcount,"records")

mydb.close()
