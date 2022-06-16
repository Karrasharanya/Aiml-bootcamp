import sqlite3
con=sqlite3.connect('bootcamp.db')
query='''
    update attendance set name='sai' where g_id=124
     '''
print(con.total_changes)
con.execute(query)
con.commit()
con.close()