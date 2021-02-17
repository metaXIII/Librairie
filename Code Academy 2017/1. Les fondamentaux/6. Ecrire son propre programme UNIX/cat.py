#!/usr/bin/env python3
import fileinput
import sys

argv = sys.argv


def do_your_work():
    for line in fileinput.input():
        print(line, end="")


if __name__ == '__main__':
    do_your_work()
