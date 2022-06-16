import sqlite3
con=sqlite3.connect('bootcamp.db')
str=con.execute("pragma table_info('attendance')")
print(str)
for i in str:
    print(i)