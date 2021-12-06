import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password="a123456",
                     database='dmenu',
                     charset='utf8')

cur = db.cursor()

# select * from note_note
try:
    sql = "update note_note set saleout=True where title =A1;"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()

cur.close()
db.close()
