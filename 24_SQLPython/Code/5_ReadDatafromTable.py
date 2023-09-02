import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="sanjaydchamp",database="damastersbooklist")

dbCursor = db.cursor()

dbCursor.execute("Select Book from bookdetail")

result = dbCursor.fetchall()

for i in result:
    print(i)
