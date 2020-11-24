def find_complement(num: int) -> int:
    bin_num = bin(num)
    r = ''
    for i in range(2, len(bin_num)):
        if bin_num[i] == '0':
            r += '1'
        else:
            r += '0'
    return int(r, 2)
