import mysql.connector
import config

def connectdb():
    global DB
    if "DB" not in globals():
        DB = mysql.connector.connect(
            host = config.Host,
            user = config.User,
            password = config.Password,
            database = config.Database
        )
    return DB


