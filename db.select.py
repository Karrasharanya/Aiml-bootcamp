import sqlite3
conn=sqlite3.connect('Bootcamp.db') #step 2 and step 3

res=conn.execute("select *from participants1")
for i in res:
    print(i)