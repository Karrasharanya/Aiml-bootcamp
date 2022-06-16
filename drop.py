import sqlite3
con=sqlite3.connect('bootcamp.db')
con.execute('drop table attendance')