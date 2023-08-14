import mysql.connector
dataBase=mysql.connector.connect(
host='localhost',
user='root',
passwd='password'
)

#prepare a cursor object
cursorObject=dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE Capstone_database")


print("All Done!! ")