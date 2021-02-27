import binascii

def transition_to_string(value):
    if len(value) < 4:
        print("Vous n'avez pas envoyé un ensemble binaire")
        return
    if len(value) % 4 != 0 and len(value) % 8 != 0:
        len_of_bin = len(value) % 8
        if len_of_bin != 0:
            how_many_bin_to_add = 8 - len_of_bin
            to_add = ""
            for i in range(how_many_bin_to_add):
                to_add += "0"
            transition_to_string(to_add + value)
    else:
        do_your_work(value)


def do_your_work(value):
    print(value)
    print(bin_to_number(value))
    print(chr(bin_to_number(value)))
    return


def bin_to_number(value):
    return value[0:7]


if __name__ == '__main__':
    transition_to_string("111000 01000010")
