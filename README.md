# Introduction to Connecting to MySQL Local Server

This guide will help you connect to a MySQL local server using the `mysql-connector-python` package.

## Prerequisites

- Python installed on your system
- MySQL server installed and running locally

## Installation

First, you need to install the `mysql-connector-python` package. You can do this using pip:

```sh
pip install mysql-connector-python
```

## Connecting to MySQL

Here is a simple example of how to connect to a MySQL local server:

```python
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

```

Replace `your_username`, `your_password`, and `your_database` with your actual MySQL credentials and database name.

Table creation:

```
query = mydb.cursor()

sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

query.execute(sql)


```

Table Insertion:

```
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
query.execute(sql, val)

mydb.commit()

print(query.rowcount, "record inserted.")

```
mydb.commit() is required to make the changes, otherwise no changes are made to the table.
