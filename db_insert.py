import sqlite3
conn=sqlite3.connect('Bootcamp.db') #step 2 and step 3

'''
query --> insert into table_name values(int,'','','')
'''
conn.execute("insert into participants1 values(2216101,'Yash Bollepally','CSAI')")
conn.execute("insert into participants1 values(2216102,'Chennamaneni Akshay Rao','CSE')")
conn.execute("insert into participants1 values(2216103,'Ram charan teja Maduri','CSAI')")
conn.execute("insert into participants1 values(2216104,'Kandula Surya Kumari','CSE')")

conn.commit()
conn.close()
