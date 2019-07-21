import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  passwd="passpass",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers ( Empid INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), address VARCHAR(255));")