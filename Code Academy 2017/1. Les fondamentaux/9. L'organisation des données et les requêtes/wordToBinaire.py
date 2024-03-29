#!/usr/bin/env python3

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


def to_binarie(value):
    result = ""
    for char in value:
        result += word_to_bin(char)
    return result


if __name__ == '__main__':
    exit()
