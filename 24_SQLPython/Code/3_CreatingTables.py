import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="sanjaydchamp",database="damastersbooklist")

dbCursor = db.cursor()
dbCursor.execute("Create table bookdetail(Rating INT(20),Book VARCHAR(40),Price DECIMAL(16,2))");
dbCursor.execute("Show tables")

for i in dbCursor:
    print(i)


