import mysql.connector as mc
try:
    con=mc.connect(host="localhost",
                   user="root",
                   password="narayan",
                   database="python")
    cur=con.cursor()
    qry="select * from students"
    cur.execute(qry)
    res = cur.description
    col = []
    for cols in res:
        col.append(cols[0])
    else:
        for v in col:
            print(v,end="\t")

    print("---"*50)
    recdata=cur.fetchall()
    for i in recdata:
        print(i)

except mc.DatabaseError as de:
    print("error in mysql :",de)