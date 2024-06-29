import mysql.connector as mc
try:
    con=mc.connect(host="localhost",
                   user="root",
                   password="narayan",
                   database="python")
    cur=con.cursor()
    while(True):
        sid=int(input("Enter student id"))
        sname=input("Enter Student name :")
        sroll=int(input("Enter student roll:"))
        cname=input("Enter college name:")
        qry="insert into students values(%d,'%s',%d,'%s')"
        cur.execute(qry %(sid,sname,sroll,cname))
        print("data saved in table")
        con.commit()
        n=input("add new rec :(yes/no)").lower()
        if(n=="no"):
            break
except mc.DatabaseError as de:
    print("Error in mysql :",de)
