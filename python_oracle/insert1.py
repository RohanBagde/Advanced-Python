#insert1.py
#inserting data statically
import cx_Oracle
try:
	con=cx_Oracle.connect("rohan/rohan@localhost/XE")
	print("connection obtain from db")
	cur=con.cursor()
	rohan="insert into student values(10,'rbb',99.99,'rtmnu')"
	cur.execute(rohan)
	con.commit()
	print("student table inserted in oracle db")
except cx_Oracle.databaseError as de:
	print(de)
finally:
	if con!=None:
		print("db connection closed:")
		con.close()



