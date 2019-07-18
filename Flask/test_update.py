import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  passwd="passpass",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET name= %s , address = %s WHERE name=%s AND address = %s"
val = ("Task","Valle 345", "Akshay","Delhi")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")