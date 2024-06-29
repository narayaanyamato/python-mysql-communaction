import mysql.connector as mc
try:
    con=mc.connect(host="localhost",
                   user="root",
                   password="narayan",
                   database="python")
    cur=con.cursor()
    sec=input("Enter name to get details :")
    qry="select * from students where sname='%s'"
    cur.execute(qry %sec)
    res = cur.description
    col = []
    for cols in res:
        col.append(cols[0])
    else:
        for v in col:
            print(v,end="  ")

    print("---"*50)
    recdata=cur.fetchone()
    print("student id:", recdata[0])
    print("student name:",recdata[1])
    print("student sroll:", recdata[2])
    print("student cname:", recdata[3])


except mc.DatabaseError as de:
    print("error in mysql :",de)