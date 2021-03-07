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
    result = ""
    cle_de_chiffrement_bin = wordToBinaire.do_your_work(sys.argv[1]).replace(" ", "")
    cypher_text = {}
    max_len = 0
    for i in range(2, len(sys.argv)):
        if len(sys.argv[i]) > 8:
            for j in range(0, int(len(sys.argv[i]) / 8)):
                cypher_text[i + j - 2 + max_len] = sys.argv[i][8 * j:8 * (j + 1)]
                j += 1
            max_len += 1
        else:
            cypher_text[i - 2 + max_len] = sys.argv[i]
    for x in range(0, len(cypher_text)):
        result += do_your_work(cle_de_chiffrement_bin, cypher_text[x])
    print("déchiffré : " + result)
