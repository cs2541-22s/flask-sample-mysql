import mysql.connector

mydb = mysql.connector.connect(
    host="instructor-1.ck8ualavedvt.us-east-1.rds.amazonaws.com",
    user="admin",
    password="SECRET",
    database="sample"
  )

c = mydb.cursor(dictionary=True)

c.execute("Select * from students")

results = c.fetchall()
print(results)

c.close()