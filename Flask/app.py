from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  passwd="passpass",
  database="mydatabase"
)

mycursor = mydb.cursor()


@app.route('/',methods = ['POST', 'GET'])
def index():
   return render_template('index.html')

@app.route('/delete_direct',methods = ['POST', 'GET'])
def delete_direct():
   return render_template('delete.html')

@app.route('/update_direct',methods = ['POST', 'GET'])
def update_direct():
   return render_template('update.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   result = request.form
   print(result)
   temp=[]
   temp.append(result['Name'])
   temp.append(result['Physics'])
   # print(temp)
   # print(type(temp))
   val =tuple(temp)
   # print(type(val))

   sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
   mycursor.execute(sql, val)

   mydb.commit()

   print(mycursor.rowcount, "record inserted.")


   mycursor.execute("SELECT * FROM customers")

   myresult = mycursor.fetchall()
   ans =[]
   for x in myresult:
      # print(type(x))
      # print(x[0],x[1])
      ans.append([x[0],x[1]])
      # print(x)

   print(ans)      
   return render_template("result.html",result = ans)

@app.route('/delete',methods = ['POST', 'GET'])
def delete():
   result = request.form
   print(result)
   temp=[]
   temp.append(result['Name'])
   temp.append(result['Physics'])
   # print(temp)
   # print(type(temp))
   val =tuple(temp)
   # print(type(val))

   sql = "DELETE FROM customers WHERE Name = %s AND Address= %s"
   mycursor.execute(sql, val)

   mydb.commit()

   print(mycursor.rowcount, "record inserted.")


   mycursor.execute("SELECT * FROM customers")

   myresult = mycursor.fetchall()
   ans =[]
   for x in myresult:
      # print(type(x))
      # print(x[0],x[1])
      ans.append([x[0],x[1]])
      # print(x)

   print(ans)      
   return render_template("result.html",result = ans)

@app.route('/update',methods = ['POST', 'GET'])
def update():
   result = request.form
   print(result)
   temp=[]
   temp.append(result['Replacen'])
   temp.append(result['Replacea'])
   temp.append(result['Name'])
   temp.append(result['Physics'])
   # print(temp)
   # print(type(temp))
   val =tuple(temp)
   # print(type(val))

   sql = "UPDATE customers SET name= %s , address = %s WHERE name=%s AND address = %s"
   mycursor.execute(sql, val)

   mydb.commit()

   print(mycursor.rowcount, "record inserted.")


   mycursor.execute("SELECT * FROM customers")

   myresult = mycursor.fetchall()
   ans =[]
   for x in myresult:
      # print(type(x))
      # print(x[0],x[1])
      ans.append([x[0],x[1]])
      # print(x)

   print(ans)      
   return render_template("result.html",result = ans)

if __name__ == '__main__':
	app.run( debug = True , port = 5000)
