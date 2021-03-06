#!/usr/bin/env python3

import sys


def transition_to_string(value):
    value = value.replace(" ", "")
    if len(value) < 4:
        print("Vous n'avez pas envoyé un ensemble binaire")
        return
    if len(value) % 4 != 0 or len(value) % 8 != 0:
        len_of_bin = len(value) % 8
        if len_of_bin != 0:
            how_many_bin_to_add = 8 - len_of_bin
            to_add = ""
            for i in range(how_many_bin_to_add):
                to_add += "0"
            transition_to_string(to_add + value)
    else:
        return do_your_work(value)


def do_your_work(value):
    result = ""
    for i in range(int(len(value) / 8)):
        result += (bin_to_number(value[i * 8:((i + 1) * 8)]))
    return result


def bin_to_number(value):
    result = 0
    for i in range(len(value)):
        char = value[i]
        if char == "1":
            result = result + pow(2, 7 - i)
    return chr(result)


if __name__ == '__main__':
    result = ""
    while True:
        for arg in sys.argv[1:]:
            result += transition_to_string(arg)
        break
    print(result)
