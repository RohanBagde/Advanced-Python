#creatab.py
import cx_Oracle
try:
	rohan=cx_oracle("rohan/rohan@localhost/orcl")
	print("connection obtain from oracle db")
	print("-----------------------------------------")
	cur=con.cursor()
	kvrqry="create table student(sno number(3),sname varchar2(10),marks number(5,2)"
	cur.execute(kvrqry)
	print("std table created in oracle db");
except cx_Oracle.DatabaseError as de:
	print(de)
finally:
	if con!=None:
		print("db connection closed")
		con.close()
