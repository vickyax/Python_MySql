from dbconnect import connectdb

db = connectdb()
query = db.cursor()

sql = "SELECT * FROM customers"

query.execute(sql)

print(query.fetchall())

db.close()