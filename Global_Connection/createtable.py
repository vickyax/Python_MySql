from dbconnect import connectdb

db = connectdb()
query = db.cursor()

sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

query.execute(sql)


print(query.rowcount)

db.close()