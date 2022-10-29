#!/usr/bin/env python3
# coding: utf-8

import sys
import datetime

begin_time = datetime.datetime.now()
print("Hello world !")

i = 0
while (i < 1000000):
    print(i)
    i += 1

print(datetime.datetime.now() - begin_time)
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
