import psycopg2

con = psycopg2.connect(host='localhost', database='doctor247', user='postgres', password='123456789')
cur = con.cursor()
sql = ""
cur.execute(sql)
con.commit()
