#!/usr/bin/env python2
# -*- coding: utf-8 -*-

f = open("list.txt", "r")

# tm = open("./lib/timeMachine.txt", mode="r", encoding="utf-8")

def doYourWork():
    for line in f:
        print(line)

if __name__ == "__main__":
    print(doYourWork)

