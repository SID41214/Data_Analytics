import mysql.connector 
db = mysql.connector.connect(host="localhost",user="root",password="sanjaydchamp")
if db:
  print("Connection successful")
else:
  print("Connection Failed")
