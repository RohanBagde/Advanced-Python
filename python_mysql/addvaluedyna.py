#addvaluedyna.py
#this program insert values in table
#step1
import mysql.connector
import sys
while(True):
#step2
	kp=mysql.connector.connect(host="localhost",user="root",passwd="rohan", database="roman")

	cur=kp.cursor()
	sno=int(input("enter student no:"))
	sname=input("enter student name:")
	smark=float(input("enter the marks"))
	cur.execute("insert into student values(%d,'%s',%f)"%(sno,sname,smark))
	kp.commit()
    print("{} student data inserted dynamycally is succesfully".format(cur.rowcount))
	ch=input("\ndo you want to enter value again(yes/no):")
    if(ch=="no"):
		print("thank you")
		sys.exit()



