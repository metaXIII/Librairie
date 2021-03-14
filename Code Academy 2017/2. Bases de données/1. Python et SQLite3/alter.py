#!/usr/bin/python python3

import sqlite3
conn = sqlite3.connect("LXF.sqlite")

conn.execute("drop table if exists lxfissues;")
conn.execute("drop table if exists issues;")

conn.execute("create table lxfissues(id int primary key not null, number int not null, year int not null, comments char(50));")
conn.execute("create table issues(id integer primary key autoincrement, number int not null, year int not null, comments char(50));")
conn.execute("alter table lxfissues add column editor char(100);")

conn.close
