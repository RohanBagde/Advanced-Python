#modify.py
import cx_Oracle
try:
	con=cx_Oracle.connect("rohan/rohan@localhost/XE")
	print("connection obtain from db")
	cur=con.cursor()
	rohan="alter table student modify(sname varchar2(15))"
	cur.execute(rohan)
	print("student table altered in oracle db")
except cx_Oracle.databaseError as de:
	print(de)
finally:
	if con!=None:
		print("db connection closed:")
		con.close()