import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="sanjaydchamp",database="damastersbooklist")

dbCursor = db.cursor()

form = "Insert into bookdetail(Rating,Book,Price) values(%s,%s,%s)"

data = [(4,"Power of Subconscious Mind",99),(3,"Attitude is Everything",50),(5,"Rich dad poor dad",149), ]

dbCursor.executemany(form,data)

db.commit()

###In Workbench - To visualize data in table
#SELECT * FROM bookdetail ORDER BY Price;


