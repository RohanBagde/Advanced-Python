#insertvaltab.py
#step1
import mysql.connector
try:
#step2
	kp=mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="roman")

#step3
	cur=kp.cursor()
#step4
	db="insert into student values(40,'goldberg',70.15)"
	cur.execute(db)
#step5
	kp.commit() 
	print("{}student table create successfuLLy".format(cur.rowcount))
except mysql.connector.databasesError as db:
	print(db)

