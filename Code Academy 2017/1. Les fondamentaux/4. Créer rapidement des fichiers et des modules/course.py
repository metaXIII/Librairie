#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

# f = open(os.environ["HOME"] + "/list.txt", "r")

def doYourWork():
    f = open("list.txt", "rb")
    print(f.readline())
    # print("\"début\"")
    # for line in f:
    #     print(line.strip("\n"))
    # print("\"fin\"")
    f.close()

if __name__ == "__main__":
    doYourWork()
