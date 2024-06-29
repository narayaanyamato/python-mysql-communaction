import mysql.connector as mc
try:
    con=mc.connect(host="localhost",
                   user="root",
                   password="narayan",
                   database="python")
    cur=con.cursor()
    qry="create table students(id int not null,sname varchar(25),sroll varchar(15),cname varchar(20))"
    cur.execute(qry)
    print("table created")

except mc.DatabaseError as de:
    print("error in mysql :",de)