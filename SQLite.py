import sqlite3

conn = sqlite3.connect('test.db')
#conn.execute('''create table test_table
#            (
#            id integer primary key not NULL,
#            data text not NULL
#            );''')
#conn.commit()
#conn.execute("insert into test_table values(1, 'first'), (2, 'second');")
#conn.commit()
cursor = conn.cursor()
cursor.execute('''select * from test_table;''')
r = cursor.fetchall()
for x in r:
    print(x)
conn.close()