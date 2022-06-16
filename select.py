import sqlite3
con=sqlite3.connect('bootcamp.db')
a=con.execute("select*from attendance")
for i in a:
    print(i)