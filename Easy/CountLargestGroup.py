
def count_largest_group(n: int) -> int:
    hash_ = {}
    for i in range(1, n + 1):
        num = i
        count = 0
        while num >= 10:
            count += num % 10
            num //= 10
        count += num

        if count in hash_:
            hash_[count] += 1
        else:
            hash_[count] = 1

    max_val = max(hash_.values())
    ans = 0
    for e in hash_.values():
        if e == max_val:
            ans += 1
    return ans


if __name__ == '__main__':
    print(count_largest_group(15))