#!/usr/bin/python python3

import sys
import sqlite3
import tkinter
from tkinter import *
import tkinter.scrolledtext as ST


def callBack():
    tableName = variable.get()
    text.delete('1.0', END)
    myText = "Table name: " + tableName
    text.insert("insert", myText + "\n")
    text.insert("insert", "** FIELD NAMES **\n")
    query = "select * from " + tableName + " where 1 = 0"
    c.execute(query)
    rs = c.fetchall()
    field_names = [r[0] for r in c.description]
    for f in field_names:
        text.insert("insert", "\t" + f + "\n")

database = sys.argv[1] if len(sys.argv) > 1 else "LXF.sqlite"

conn = sqlite3.connect(database)
c = conn.cursor()

root = Tk()
canvas = Canvas(root, width=810, height=600)
canvas.pack()

text = ST.ScrolledText(canvas, width=35, height=20, borderwidth=0)
text.pack()

# Dummy
listOfTables = {}
listOfTables['sqlite_master'] = 0

c.execute("select name from sqlite_master where type='table';")
for record in c:
    listOfTables[record[0]] = 0

variable = StringVar(root)
variable.set("sqlite_master") #default value
w = OptionMenu(root, variable, *listOfTables)
w.pack()
Button(root, text="Quit", command=root.quit).pack(side=BOTTOM, anchor=SE)
Button(root, text="OK", command=callBack).pack(side=TOP, anchor=SE)

mainloop()
conn.close()