import sqlite3
conn=sqlite3.connect('Bootcamp.db') #step 2 and step 3

'''
    query -> desc participants ->MySQL
    query -> pragma table_info(table_name) -> sqlite3
'''
str=conn.execute("pragma table_info('participants1')")
print(str)
for i in str:
    print(i)
