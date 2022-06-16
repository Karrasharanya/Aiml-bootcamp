
import sqlite3
conn=sqlite3.connect('Bootcamp.db') #step 2 and step 3

'''
query --> update table_name set column_name=updated_value where <<condition>>
'''

query = '''update participants1 set name='Yashwanth' where g_id=2216101
        '''

conn.execute(query)

print(conn.total_changes)
conn.commit()
conn.close()