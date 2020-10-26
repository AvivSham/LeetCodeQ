
def mincostmovechips(chips):
    odd_nums, even_nums = 0, 0
    for i in range(len(chips)):
        if i % 2 == 0:
            even_nums += 1
        else:
            odd_nums += 1
    return min(even_nums, odd_nums)


if __name__ == '__main__':
    print(mincostmovechips(range(1,31)))