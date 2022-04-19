# flask-sample-mysql
Sample Student App with MySQL DB

## Files

`testflask.py`: Simple hello world in flask to be sure libraries are installed correctly

`testmysql.py`: Simple python script to access a MySQL database

`main.py`: Simple flask app to display student data from a MySQL database

`create.sql`: Creates `sample` database, `student` table, and fills data

`secrets.py-def`: For `main.py` to work, it needs to get a hostname, username, and password from a `secrets.py` file. Make a copy of this file, fill it in, and rename it. This lets us avoid putting secret credentials like database passwords into a git repo.