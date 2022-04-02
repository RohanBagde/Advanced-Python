#insertdy1.py
#program for inserting record from table with dynamically data
import cx_Oracle
try:
	con=cx_Oracle.connect("rohan/rohan@localhost/XE")
	print("connection obtain from db")
	cur=con.cursor()
	while(True):
		stno=int(input("enter student number:"))
		stname=input("enter student name:")
		marks=float(input("enter student marks:"))
		cname=input("enter college name:")
		querry="insert into student values(%d,'%s',%f,'%s')"
		cur.execute(querry %(stno,stname,marks,cname))
		con.commit()
		print("student record inserted  in oracle db")
		ch=input("do you want to insert values again (yes/no):")
		if(ch=="no"):
			break
except cx_Oracle.databaseError as de:
	print(de)



