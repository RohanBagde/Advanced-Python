#createdb.py
#this program creates database in mysql 
#step1
import mysql.connector
try:
#step2
	kp=mysql.connector.connect(host="localhost",user="root",passwd="rohan")

#step3
	cur=kp.cursor()
#step4
	db="create database roman"
	cur.execute(db)
	print("data base create successfuLLy")
except mysql.connector.databasesError as db:
	print(db)

