#!/usr/bin/env python


import sys

import binaireToWord
import chiffrement
import wordToBinaire


def do_your_work(cle_de_chiffrement, cypher_text):
    result = ""
    cle_de_chiffrement = cle_de_chiffrement.replace(" ", "")
    cypher_text = cypher_text.replace(" ", "")
    cypher_text = cypher_text[::-1]
    cle_de_chiffrement = cle_de_chiffrement[::-1]
    for i in range(0, 8):
        result += chiffrement.get_encrypted_text(cle_de_chiffrement[i], cypher_text[i])
    result = binaireToWord.do_your_work(result[::-1])
    return result


if __name__ == '__main__':
    if (len(sys.argv)) != 3:
        print("end of program, should only be two args")
        exit()
    result = ""
    key = wordToBinaire.to_binarie(sys.argv[1]).replace(" ", "")
    to_convert = sys.argv[2]
    text = {}
    i = 0
    while len(key) != len(to_convert):
        if len(key) < len(to_convert):
            key = (key[::-1] + "0")[::-1]
        else:
            to_convert = (to_convert[::-1] + "0")[::-1]
    print(key)
    print(to_convert)
    for char in to_convert:
        result += chiffrement.get_encrypted_text(char, key[i])
        i += 1
    print(result)
    print("déchiffré :", binaireToWord.do_your_work(result))

    # for i in range(2, len(sys.argv)):
    #     if len(sys.argv[i]) > 8:
    #         for j in range(0, int(len(sys.argv[i]) / 8)):
    #             cypher_text[i + j - 2 + max_len] = sys.argv[i][8 * j:8 * (j + 1)]
    #             j += 1
    #         max_len += 1
    #     else:
    #         cypher_text[i - 2 + max_len] = sys.argv[i]
    # for x in range(0, len(cypher_text)):
    #     result += do_your_work(cle_de_chiffrement_bin, cypher_text[x])
    # print("déchiffré : " + result)
