import sqlite3
con=sqlite3.connect('bootcamp.db')
con.execute("insert into attendance values(123,'siri',100)")
con.execute("insert into attendance values(124,'ram',90)")
con.execute("insert into attendance values(125,'pranay',100)")
con.execute("insert into attendance values(126,'devika',95)")
con.execute("insert into attendance values(127,'sharanya',80)")
con.commit()
con.close()