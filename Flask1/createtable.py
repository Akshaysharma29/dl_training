# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="akshay",
#   passwd="passpass"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  passwd="passpass",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers ( Empid INT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255));")