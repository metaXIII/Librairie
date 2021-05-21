#!/usr/bin/env python

import redis
import sys

r = redis.StrictRedis("localhost", port=6379, db=0)
if len(sys.argv) != 4:
    print("Wrong number of argument")
    print("insert.py phone name surname")
    sys.exit

telephone = sys.argv[1]
name = sys.argv[2]
surname = sys.argv[3]

myTel = r.rpush(telephone, telephone)
myName = r.rpush(telephone, name)
mySur = r.rpush(telephone, surname)