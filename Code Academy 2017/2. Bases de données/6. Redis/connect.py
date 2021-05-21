#!/usr/bin/env python

import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)
myVal = r.set("One", "Two")
if myVal == True:
    print ("Set operation was successfull")
else:
    print("Opération failed")

myVal = r.get("One")
print("The value of One is " + str(myVal))