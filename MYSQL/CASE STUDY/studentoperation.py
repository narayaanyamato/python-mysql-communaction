import mysql.connector as mc
def Add():
    try:
        con = mc.connect(host="localhost",
                         user="root",
                         password="narayan",
                         database="python")
        cur = con.cursor()
        while (True):
            sid = int(input("Enter student id"))
            sname = input("Enter Student name :")
            sroll = int(input("Enter student roll:"))
            cname = input("Enter college name:")
            qry = "insert into students values(%d,'%s',%d,'%s')"
            cur.execute(qry % (sid, sname, sroll, cname))
            print("data saved in table")
            con.commit()
            n = input("add new rec :(yes/no)").lower()
            if (n == "no"):
                break
    except mc.DatabaseError as de:
        print("Error in mysql :", de)

def remove():
    try:
        con = mc.connect(host="localhost",
                         user="root",
                         password="narayan",
                         database="python")
        cur = con.cursor()
        d = int(input("Enter student id :"))
        qry = "delete from students where id=%d"
        cur.execute(qry % d)
        con.commit()
        print("Data removed")

    except mc.DatabaseError as de:
        print("error in mysql :", de)


def update():
    try:
        con = mc.connect(host="localhost",
                         user="root",
                         password="narayan",
                         database="python")
        cur = con.cursor()
        while (True):
            print("select bellow to update :")
            print("1)Update Name\t\t 2)update college \t\t 3)update rollno")
            n = int(input("Enter your choice:"))
            if (n == 1):
                sid = int(input("Enter id:"))
                sname = input("Enter student name:")
                qry = "update students set sname='%s' where id=%d"
                cur.execute(qry % (sname, sid))
                print("rec name update")
                con.commit()
            elif (n == 2):
                sid = int(input("Enter id:"))
                cname = input("Enter college name:")
                qry = "update students set cname='%s' where id=%d"
                cur.execute(qry % (cname, sid))
                print("rec college update")
                con.commit()
            elif (n == 3):
                sid = int(input("Enter id:"))
                cname = int(input("Enter Rollno:"))
                qry = "update students set sroll=%d where id=%d"
                cur.execute(qry % (cname, sid))
                print("rec college update")
                con.commit()

            e = input("Enter yes/no to update :")
            if (e == "no"):
                break
    except mc.DatabaseError as de:
        print("error in mysql :", de)


def view():
    try:
        con = mc.connect(host="localhost",
                     user="root",
                     password="narayan",
                     database="python")
        cur = con.cursor()
        qry = "select * from students"
        cur.execute(qry)
        res = cur.description
        col = []
        for cols in res:
            col.append(cols[0])
        else:
            for v in col:
                print(v, end="\t")

        print("---" * 50)
        recdata = cur.fetchall()
        for i in recdata:
            print(i)

    except mc.DatabaseError as de:
        print("error in mysql :", de)

def search():
    try:
        con = mc.connect(host="localhost",
                         user="root",
                         password="narayan",
                         database="python")
        cur = con.cursor()
        sec = input("Enter name to get details :")
        qry = "select * from students where sname='%s'"
        cur.execute(qry % sec)
        res = cur.description
        col = []
        for cols in res:
            col.append(cols[0])
        else:
            for v in col:
                print(v, end="  ")

        print("---" * 50)
        recdata = cur.fetchone()
        print("student id:", recdata[0])
        print("student name:", recdata[1])
        print("student sroll:", recdata[2])
        print("student cname:", recdata[3])


    except mc.DatabaseError as de:
        print("error in mysql :", de)