import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  passwd="passpass",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(type(x))
    print(x[0],x[1])
    print(x)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)