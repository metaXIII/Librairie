#!/usr/bin/env python3

import dechiffrement
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
    cle_de_chiffrement = "A"
    cle_de_chiffrement_bin = wordToBinaire.do_your_work(cle_de_chiffrement)
    test = "B"
    word_bin = wordToBinaire.do_your_work(test)
    result = ""
    cypher_text = ""
    i = 0

    while True:
        cypher_text += get_encrypted_text(cle_de_chiffrement_bin[i], word_bin[i])
        i += 1
        if i > 7:
            break
    print(cle_de_chiffrement_bin)
    print(word_bin)
    print(cypher_text)
    print(dechiffrement.do_your_work(cypher_text))
