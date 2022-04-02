#delete.py
#program for deleting record from table with static data
import cx_Oracle
try:
	con=cx_Oracle.connect("rohan/rohan@localhost/XE")
	print("connection obtain from db")
	cur=con.cursor()
	rohan="delete from student where sno=10"
	cur.execute(rohan)
	con.commit()
	print("student table delete in oracle db")
except cx_Oracle.databaseError as de:
	print(de)
finally:
	if con!=None:
		print("db connection closed:")
		con.close()



