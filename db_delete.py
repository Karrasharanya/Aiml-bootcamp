import sqlite3

conn = sqlite3.connect("Bootcamp.db")

'''
query = delete from table_name where <<condition>>
'''
conn.execute("delete from participants where branch='CSE'")
print(conn.total_changes)

conn.commit()
conn.close()

'''
drop the table from database
conn = sqlite3.connect("Bootcamp.db")
conn.execute("drop table participants1")
'''