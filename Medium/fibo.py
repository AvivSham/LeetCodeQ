# Dynamic Programming solution for Fibonacci numbers

#######################
#                     #
# Recursive solution  #
#                     #
#######################


def fib(num):
    if num < 2:
        return num
    cache = [-1 for _ in range(num + 1)]
    cache[0] = 0
    cache[1] = 1
    return fib_(num, cache)


def fib_(num, cache):
    if cache[num] >= 0:
        return cache[num]

    cache[num] = fib_(num - 1, cache) + fib_(num - 2, cache)
    return cache[num]


#######################
#                     #
# Iterative solution  #
#                     #
#######################

def fib_iter(num):
    if num == 0:
        return 0
    fibi = [-1 for _ in range(num + 1)]
    fibi[0] = 0
    fibi[1] = 1
    for i in range(2, len(fibi), 1):
        fibi[i] = fibi[i - 2] + fibi[i - 1]
    return fibi[-1]


if __name__ == '__main__':
    print(fib_iter(0))
