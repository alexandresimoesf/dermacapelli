import psycopg2

con = psycopg2.connect(host='localhost', database='doctor247', user='postgres', password='123456789')
cur = con.cursor()
with open('agenda_sql_203.sql', 'r', encoding='utf-8') as sql_file:
    for linha_sql in sql_file:
        try:
            sql = linha_sql
            cur.execute(sql)
        except Exception as e:
            print(e)

# con.commit()
con.close()