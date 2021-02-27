#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# file = open("exist.txt", "w")

# for feed in feeds:
#     file.write("{0}\n".format(feed))
import json

feeds = ["http://newsrss.bbc.co.uk/rss/newsonline_uk_edutuib/front_page/rss.xml", "http://www.tuxradar.com/rss"]
with open("exist.txt", "a") as file:
    json.dump(feeds, file)
with open("exist.txt", "r") as file:
    feeds = json.load(file)
    print(feeds)
