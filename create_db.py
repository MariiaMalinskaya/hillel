import sqlite3

con = sqlite3.connect('new.db')
cur = con.cursor()
sql_query =  '''
CREATE TABLE If NOT EXISTS phones
(contactName text, phoneValue text )
'''

cur.execute(sql_query)
con.commit()
con.close()