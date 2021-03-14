#!/usr/bin/python python3

import sqlite3
conn = sqlite3.connect("LXF.sqlite")
conn.execute("update issues set year = 2016 where year = 2015")
conn.commit()

print("Total of rows updated: ", conn.total_changes)


conn.close
