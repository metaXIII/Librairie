#!/usr/bin/python python3

import sqlite3
conn = sqlite3.connect("LXF.sqlite")

conn.execute("insert into issues(number, year, comments) values(202, 2015, 'Best issue ever !');")
conn.execute("insert into issues(number, year, comments) values(203, 2015, 'Best Linux Format issue ever !');")

conn.commit()

conn.execute("insert into lxfissues(id, number, year, comments) values(0, 202, 2015, 'Best issue ever !');")
conn.execute("insert into lxfissues(id, number, year, comments) values(1, 203, 2015, 'Best Linux Format issue ever !');")

conn.commit()

conn.close
