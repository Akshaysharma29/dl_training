import mysql.connector

class customers:
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="akshay",
      passwd="passpass",
      database="mydatabase"
    )

    self.mycursor = self.mydb.cursor()

  def sel(self):
    
    self.mycursor.execute("SELECT * FROM customers")

    myresult = self.mycursor.fetchall()
    
    data =[]

    for x in myresult:
        # print(type(x))
        data.append([x[0],x[1],x[2]])
    
    return(data)
  
  def insert(self,Name,Physics):

    self.Name=Name
    self.Physics=Physics
    
    temp=[]
    temp.append(self.Name)
    temp.append(self.Physics)

    val =tuple(temp)

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    self.mycursor.execute(sql, val)

    self.mydb.commit()
    
  def delete(self,Empid):

    self.Empid=Empid
    
    temp=[]
    temp.append(self.Empid)

    val =tuple(temp)

    sql = "DELETE FROM customers WHERE Empid=%s"
    self.mycursor.execute(sql, val)

    self.mydb.commit()

  def update(self,Replacen,Replacea,Empid):

    self.Replacen=Replacen
    self.Replacea=Replacea
    self.Empid=Empid
    
    temp=[]
    temp.append(self.Replacen)
    temp.append(self.Replacea)
    temp.append(self.Empid)

    val =tuple(temp)

    sql = "UPDATE customers SET name= %s , address = %s WHERE Empid=%s"
    self.mycursor.execute(sql, val)

    self.mydb.commit()

# p1 = customers()
# z=p1.sel()
# print(z)