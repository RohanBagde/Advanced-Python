#mysqlconnect.py
import mysql.connector
con=mysql.connector.connect(
                           host="localhost", 
                           user="root", 
						   passwd="rohan")
print("mysql connected")
