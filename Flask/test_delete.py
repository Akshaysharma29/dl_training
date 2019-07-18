import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  passwd="passpass",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE Name = %s AND Address= %s"
adr = ("Akshay","Delhi" )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")