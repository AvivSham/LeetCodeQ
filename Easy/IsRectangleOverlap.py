from typing import List


def is_rectangle_overlap(rec1: List[int], rec2: List[int]) -> bool:
    return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[1] >= rec2[3] or rec2[1] >= rec1[3])


if __name__ == '__main__':
    print(is_rectangle_overlap([0, 0, 2, 2], [1, 1, 3, 3]))
