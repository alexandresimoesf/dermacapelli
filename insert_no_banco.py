import psycopg2

con = psycopg2.connect(host='localhost', database='doctor247', user='postgres', password='123456789')
cur = con.cursor()
with open('agenda_sql_203.sql', 'r', encoding='utf-8') as sql_file:
    for n, linha_sql in enumerate(sql_file):
        try:
            sql = linha_sql
            cur.execute(sql)
        except Exception as e:
            con.rollback()
            print(n, e)

# con.commit()
con.close()