import sqlite3
con=sqlite3.connect('bootcamp.db')
query= ''' 
       create table attendance(g_id int,name text,percentage int)
       '''
con.execute(query)