#!/usr/bin/env python3

import sys

import wordToBinaire


# XOR Rules
#   Input 1 Input 2
#   0       0       0
#   0       1       1
#   0       1       1
#   1       1       0


def get_encrypted_text(clebin, wordbin):
    if clebin == wordbin:
        element = "0"
    else:
        element = "1"
    return element


if __name__ == '__main__':
    if (len(sys.argv)) != 3:
        print("end of program, should only be two args")
        exit()
    key = sys.argv[1]
    to_convert = sys.argv[2]
    key = wordToBinaire.to_binarie(key).replace(" ", "")
    to_convert = wordToBinaire.to_binarie(to_convert).replace(" ", "")
    while len(key) != len(to_convert):
        if len(key) < len(to_convert):
            key = (key[::-1] + "0")[::-1]
        else:
            to_convert = (to_convert[::-1] + "0")[::-1]
    result = ""
    position = 0
    for char in to_convert:
        result += get_encrypted_text(char, key[position])
        position += 1
    print("key: " + key)
    print("mot: " + to_convert)
    print("chiffré: " + result)
