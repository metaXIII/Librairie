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
        do_your_work(value)


def do_your_work(value):
    result = ""
    for i in range(int(len(value) / 8)):
        result += (bin_to_number(value[i * 8:((i + 1) * 8)]))
    print(result)


def bin_to_number(value):
    result = 0
    for i in range(len(value)):
        char = value[i]
        if char == "1":
            result = result + pow(2, 7 - i)
    return chr(result)


if __name__ == '__main__':
    transition_to_string("01101111 01101110  00100000 01110110 01100001  00100000 01100100 01100101 01110110 01100101 01101110 01101001 01110010  00100000 01110000 01100001 01110010 01100101 01101110 01110100  00100000")  # 8B8B # 8 -> 56 # B -> 66
    # transition_to_string("   111000 01000010 00111000 01000010")  # 8B8B # 8 -> 56 # B -> 66
