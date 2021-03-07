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
    cle_de_chiffrement = sys.argv[1]
    cle_de_chiffrement_bin = wordToBinaire.do_your_work(cle_de_chiffrement)
    to_crypted = ""
    crypted = ""

    for arg in sys.argv[2:]:
        to_crypted += arg + " "
    word_bin = wordToBinaire.do_your_work(to_crypted)
    result = ""
    cypher_text = ""
    i = 0

    word_bin_without_space = word_bin.replace(" ", "")
    max = int(len(word_bin_without_space) / 8)
    dict = {}
    cypher_text = {}
    for i in range(0, max):
        dict[i] = word_bin_without_space[i * 8:(i + 1) * 8] + wordToBinaire.do_your_work(" ")
    result = ""
    for i in range(0, max):
        for j in range(0, 8):
            result += get_encrypted_text(cle_de_chiffrement_bin[j], dict[i][j])
    crypted += result
    print("key :" + cle_de_chiffrement_bin)
    print("mot :" + word_bin)
    print("chiffré :" + crypted)
