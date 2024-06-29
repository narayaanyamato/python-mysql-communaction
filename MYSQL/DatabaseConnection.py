import mysql.connector as mc
try:
    con=mc.connect(host="localhost",user="root",password="narayan",database="test")
    print("database connection successfull")

    print("table created")
except mc.DatabaseError as de:
    print("error in :",de)