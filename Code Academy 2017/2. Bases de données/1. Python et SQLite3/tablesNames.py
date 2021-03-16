#!/usr/bin/python python3

import sys
import sqlite3

database = sys.argv[1]
tableName = sys.argv[2]

print(database)
print(tableName)

conn = sqlite3.connect(database)
c = conn.cursor()
query = "select * from " + tableName + " where 1=0"
c.execute(query)
rs = c.fetchall()
field_names = [r[0] for r in c.description]

for f in field_names:
    print("*", f)