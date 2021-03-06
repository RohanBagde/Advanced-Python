#cursor.py
import cx_Oracle
try:
	con=cx_Oracle.connect("rohan/rohan@localhost/XE")
	print("connection obtain from db")
	cur=con.cursor()
	rohan="create table student(sno number(3),sname varchar2(10),marks number(5,2))"
	cur.execute(rohan)
	print("student table created in oracle db")
except cx_Oracle.databaseError as de:
	print(de)
finally:
	if con!=None:
		print("db connection closed:")
		con.close()