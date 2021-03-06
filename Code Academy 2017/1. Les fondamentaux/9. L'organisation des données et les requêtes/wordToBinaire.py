#!/usr/bin/env python

import sys


def bin_to_ord(char):
    char = int(char)
    result = ""
    max = 7
    while max >= 0:
        maxpow = pow(2, max)
        if maxpow > char:
            result += "0"
        else:
            result += "1"
            char -= maxpow
        max -= 1
    return result


def word_to_bin(char):
    return bin_to_ord(ord(char)) + " "


def do_your_work(value):
    result = ""
    for char in value:
        result += word_to_bin(char)
    return result


SPACE_ORD = " "

if __name__ == '__main__':
    result = ""
    while True:
        for arg in sys.argv[1:]:
            result += do_your_work(arg) + " " + do_your_work(SPACE_ORD)
        break
    print(result)
