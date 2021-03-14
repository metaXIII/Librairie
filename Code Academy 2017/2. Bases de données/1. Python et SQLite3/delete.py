#!/usr/bin/python python3

import sqlite3
conn = sqlite3.connect("LXF.sqlite")

conn.execute("delete from issues where id = 2;")
conn.commit()

print("total of rows deleted : ", conn.total_changes)
conn.close
