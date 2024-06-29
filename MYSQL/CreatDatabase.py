import mysql.connector as mc
try:
    con=mc.connect(host="localhost",
                   user="root",
                   password="narayan"
                   )
    cur=con.cursor()
    qry="create database python"
    cur.execute(qry)
    print("Database created successfully!")

except mc.DatabaseError as de:
    print("Errotor in mysql :".de)

