import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '2206'
    
)



# prepare cursor object
cursorObject = dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE!")