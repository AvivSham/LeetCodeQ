def rotate_string(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False

    if A == B:
        return True

    A = list(A)
    B = list(B)

    for _ in range(len(A)):
        if A == B:
            return True

        A.append(A.pop(0))

    return False


def rotate_string_v2(A: str, B:str) -> bool:
    return (B in 2*A) and (len(A) == len(B))


if __name__ == '__main__':
    print(rotate_string_v2("", ""))
