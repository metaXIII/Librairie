#!/usr/bin/env python3
# -*- coding: utf-8 -*-


tm = open("./lib/timeMachine.txt", mode="r", encoding="utf-8")
dict = {}
for line in tm:
	line = line.strip()
	line = line.translate(str.maketrans("", "",'!"#«»$%&–—\'()*+,-./:;<=>?@[\\]^_`{|}~'))
	line = line.lower()
	line = line.split(' ')
	for word in line:
		if word in dict:
			count = dict[word]
			count += 1
			dict[word] = count
		else:
			dict[word] = 1

for word, count in dict.items():
	print(word + " : " + str(count))