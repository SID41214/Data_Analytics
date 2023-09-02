import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="sanjaydchamp",database="damastersbooklist")

dbCursor = db.cursor()

dbCursor.execute("Update bookdetail SET Price=500 WHERE Rating>4")

db.commit()
