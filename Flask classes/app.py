from flask import Flask, render_template, request
import mysql.connector
from query_classes import customers

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
   p1 = customers()
   data=p1.sel()
   print(data)
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
  
   p2 = customers()
   p2.insert(result['Name'],result['Physics'])

   p1 = customers()
   data=p1.sel()
   print(data)     
   return render_template("result.html",result = data)

@app.route('/delete',methods = ['POST', 'GET'])
def delete():
   result = request.form
   p2 = customers()
   p2.delete(result['Empid'])

   p1 = customers()
   data=p1.sel()
   print(data)       
   return render_template("result.html",result = data)

@app.route('/update',methods = ['POST', 'GET'])
def update():
   result = request.form
   # print(result)
   p2 = customers()
   p2.update(result['Replacen'],result['Replacea'],result['Empid'])

   p1 = customers()
   data=p1.sel()
   print(data)      
   return render_template("result.html",result = data)

if __name__ == '__main__':
	app.run( debug = True , port = 5000)
