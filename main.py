import secrets # fill your DB info here - use secrets.
import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask('app')
mydb = mysql.connector.connect(
    host=secrets.config["host"],
    user=secrets.config["user"],
    password=secrets.config["password"],
    database="sample"
  )

@app.route('/')
def index():
  # Connect to database
  cursor = mydb.cursor(dictionary=True)
  # Get all the students and render to template
  cursor.execute("SELECT * FROM students;")

  students = cursor.fetchall()
  # or use cursor.fetchone() to get a single row
  return render_template("index.html", students=students)

@app.route('/addStudent')
def addStudent():
  cursor = mydb.cursor(dictionary=True)
  # Insert new student into the students table 
  # Will give error if student exists!
  student_name = "Zinnia Wood"
  student_id = "G00000000"
  student_email = "something@gmail.com"
  cursor.execute("INSERT INTO students (name, id, email) VALUES (%s,%s,%s)", (student_name, student_id, student_email) )
  mydb.commit()
  return redirect('/')

@app.route('/delStudent/<student_id>')
def delStudent(student_id):
  cursor = mydb.cursor(dictionary=True)
  # Delete student based on route parameter
  cursor.execute("DELETE FROM students WHERE id=(%s)", (student_id, ) )
  mydb.commit()
  return redirect('/')

app.run(host='0.0.0.0', port=8080)