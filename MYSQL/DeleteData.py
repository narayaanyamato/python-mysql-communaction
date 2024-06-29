import mysql.connector as mc
try:
    con=mc.connect(host="localhost",
                   user="root",
                   password="narayan",
                   database="python")
    cur=con.cursor()
    d=int(input("Enter student id :"))
    qry="delete from students where id=%d"
    cur.execute(qry %d)
    con.commit()
    print("Data removed")

except mc.DatabaseError as de:
    print("error in mysql :",de)