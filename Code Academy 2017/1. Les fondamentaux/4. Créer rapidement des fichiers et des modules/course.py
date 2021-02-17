#!/usr/bin/env python2
# -*- coding: utf-8 -*-

f = open("list.txt", "r")

# tm = open("./lib/timeMachine.txt", mode="r", encoding="utf-8")

def doYourWork():
    print("\"début\"")
    for line in f:
        print(line.strip("\n"))
    print("\"fin\"")

if __name__ == "__main__":
    doYourWork()
