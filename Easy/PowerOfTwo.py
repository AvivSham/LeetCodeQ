import math


def isPowerOfTwo(n: int) -> bool:
    """
    :type n: int
    :rtype: bool - returns true if n is power of 2,  false otherwise
    """
    return True if math.log2(n) % 1 == 0 else False


def isPowerOfTwo_ver2(n: int) -> bool:
    """
    :type n: int
    :rtype: bool - returns true if n is power of 2,  false otherwise
    """
    return n > 0 and bin(n).count("1") == 1
