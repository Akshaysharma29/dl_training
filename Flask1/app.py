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
   mycursor.execute("SELECT * FROM customers")

   myresult = mycursor.fetchall()
   data =[]
   for x in myresult:
      # print(type(x))
      # print(x[0],x[1])
      data.append([x[0],x[1],x[2]])
      # print(x)

   # print(ans)
   return render_template('result.html',result=data)

@app.route('/delete_direct',methods = ['POST', 'GET'])
def delete_direct():
   result = request.form
   # print(result)
   return render_template('delete.html')

@app.route('/update_direct',methods = ['POST', 'GET'])
def update_direct():
   result = request.form
   # print(result)
   temp =[]
   temp.append(result['Empid'])
   temp.append(result['Name'])
   temp.append(result['Physics'])
   return render_template('update.html',ans=temp)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   result = request.form
   # print("hi")
   # print(result)
   temp=[]
   temp.append(result['Empid'])
   temp.append(result['Name'])
   temp.append(result['Physics'])
   # print(temp)
   # print(type(temp))
   val =tuple(temp)
   # print(type(val))

   sql = "INSERT INTO customers (Empid,name, address) VALUES (%s, %s, %s)"
   mycursor.execute(sql, val)

   mydb.commit()

   # print(mycursor.rowcount, "record inserted.")


   mycursor.execute("SELECT * FROM customers")

   myresult = mycursor.fetchall()
   ans =[]
   for x in myresult:
      # print(type(x))
      # print(x[0],x[1])
      ans.append([x[0],x[1],x[2]])
      # print(x)

   # print(ans)      
   return render_template("result.html",result = ans)

@app.route('/delete',methods = ['POST', 'GET'])
def delete():
   result = request.form
   # print(result)
   temp=[]
   temp.append(result['Empid'])
   # print(temp)
   # print(type(temp))
   val =tuple(temp)
   # print(type(val))

   sql = "DELETE FROM customers WHERE Empid=%s"
   mycursor.execute(sql, val)

   mydb.commit()

   # print(mycursor.rowcount, "record deleted.")


   mycursor.execute("SELECT * FROM customers")

   myresult = mycursor.fetchall()
   ans =[]
   for x in myresult:
      # print(type(x))
      # print(x[0],x[1])
      ans.append([x[0],x[1],x[2]])
      # print(x)

   # print(ans)      
   return render_template("result.html",result = ans)

@app.route('/update',methods = ['POST', 'GET'])
def update():
   result = request.form
   # print(result)
   temp=[]
   temp.append(result['Replacen'])
   temp.append(result['Replacea'])
   temp.append(result['Empid'])
   # temp.append(result['Name'])
   # temp.append(result['Physics'])
   # print(temp)
   # print(type(temp))
   val =tuple(temp)
   # print(type(val))

   sql = "UPDATE customers SET name= %s , address = %s WHERE Empid=%s"
   mycursor.execute(sql, val)

   mydb.commit()

   # print(mycursor.rowcount, "record update.")


   mycursor.execute("SELECT * FROM customers")

   myresult = mycursor.fetchall()
   ans =[]
   for x in myresult:
      # print(type(x))
      # print(x[0],x[1])
      ans.append([x[0],x[1],x[2]])
      # print(x)

   # print(ans)      
   return render_template("result.html",result = ans)

if __name__ == '__main__':
	app.run( debug = True , port = 5000)
