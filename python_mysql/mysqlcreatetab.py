#createtab.py
#step1
import mysql.connector
try:
#step2
	kp=mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="roman")

#step3
	cur=kp.cursor()
#step4
	db="create table student(sno int primary key,name varchar(20) not null,marks float not null)"
	cur.execute(db)
	print("student table create successfuLLy")
except mysql.connector.databasesError as db:
	print(db)

