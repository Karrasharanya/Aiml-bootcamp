'''
1. importing the module
2. Create a databse
3. Connecting the databse
4. create a table in the database -write query
5. executing the query
'''

import sqlite3
conn=sqlite3.connect('Bootcamp.db') #step 2 and step 3

'''
query -> create table table_name(column_names datatype constraints(primary key, not null, unique),.......)
'''
query = '''
        create table participants1(g_id int primary key,name text not null,branch text not null)
        '''
conn.execute(query)

