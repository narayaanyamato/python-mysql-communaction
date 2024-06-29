import mysql.connector as mc
try:
    con=mc.connect(host="localhost",
                   user="root",
                   password="narayan",
                   database="python")
    cur=con.cursor()
    while(True):
        print("select bellow to update :")
        print("1)Update Name\t\t 2)update college \t\t 3)update rollno")
        n=int(input("Enter your choice:"))
        if(n==1):
            sid=int(input("Enter id:"))
            sname=input("Enter student name:")
            qry="update students set sname='%s' where id=%d"
            cur.execute(qry %(sname,sid))
            print("rec name update")
            con.commit()
        elif(n==2):
            sid = int(input("Enter id:"))
            cname = input("Enter college name:")
            qry = "update students set cname='%s' where id=%d"
            cur.execute(qry %(cname,sid))
            print("rec college update")
            con.commit()
        elif(n==3):
            sid = int(input("Enter id:"))
            cname = int(input("Enter Rollno:"))
            qry = "update students set sroll=%d where id=%d"
            cur.execute(qry % (cname,sid))
            print("rec college update")
            con.commit()

        e=input("Enter yes/no to update :")
        if(e=="no"):
            break
except mc.DatabaseError as de:
    print("error in mysql :",de)