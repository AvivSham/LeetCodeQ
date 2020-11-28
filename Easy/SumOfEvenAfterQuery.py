from typing import List


def sum_even_after_queries(A: List[int], queries: List[List[int]]) -> List[int]:
    ans = sum([a for a in A if a % 2 == 0])
    res = []

    for val, idx in queries:
        if A[idx] % 2 == 0:  # case of A[idx] even
            if val % 2 == 0:  # val even as well
                ans += val  # add val to sum of even values
            else:  # case of A[idx] odd
                ans -= A[idx]  # remove A[idx]from sum since it is no longer even

        elif val % 2 == 1:  # case A[idx] is odd
            ans += val + A[idx]  # add val + A[idx] to sum of even values since it didn't
            # include A[idx] in the first place

        res.append(ans)  # add current sum
        A[idx] += val  # update A[idx]

    return res
