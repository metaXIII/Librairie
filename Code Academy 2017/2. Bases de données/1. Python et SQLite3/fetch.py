#!/usr/bin/python python3

import sqlite3
conn = sqlite3.connect("LXF.sqlite")
c = conn.execute("select * from issues;")

for row in c:
	print(row)
conn.close
