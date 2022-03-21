import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask('app')

@app.route('/')
def index():
  # Connect to database
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  # Get all the students and render to template
  cursor.execute("SELECT * FROM students;")
  students = cursor.fetchall()
  # or use cursor.fetchone() to get a single row
  connection.close()
  return render_template("index.html", students=students)

@app.route('/addStudent')
def addStudent():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  # Insert new student into the students table 
  # Will give error if student exists!
  student_name = "Zinnia Wood"
  student_id = "G00000000"
  student_email = "something@gmail.com"
  cursor.execute("INSERT INTO students (name, id, email) VALUES (?,?,?)", (student_name, student_id, student_email) )
  connection.commit()
  connection.close()
  return redirect('/')

@app.route('/delStudent/<student_id>')
def delStudent(student_id):
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  # Delete student based on route parameter
  cursor.execute("DELETE FROM students WHERE id=(?)", (student_id, ) )
  connection.commit()
  connection.close()
  return redirect('/')

app.run(host='0.0.0.0', port=8080)