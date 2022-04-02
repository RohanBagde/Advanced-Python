#inserttab.py
#inserting data dynamically
import sys
import mysql.connector
while (True):
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="rohan",
                                database="roman")
    cur=con.cursor()
    sno=int(input("enter student ID number: "))
    name=input("enter student name: ")
    marks=float(input("enter student salory: "))
    cur.execute("insert into student values(%d,'%s',%f)" %(sno,name,marks))
    con.commit()
    print("{}student data inserted into table dynamically is succesfully".format(cur.rowcount))
    ch=input("\nDo u want to insert another record(yes/no):")
    if(ch=="no"):
        print("Thanks for using this Program:")
        sys.exit()
