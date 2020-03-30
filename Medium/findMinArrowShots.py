from typing import List


def find_min_arrow_shots(points):
    if not points:
        return 0

    # sort list according to highest value
    points = sorted(points, key=lambda x: x[1])

    # init number of arrows and current pair
    c = 0
    n = 1
    for i in range(1, len(points)):

        # if the two groups does not intersect -> update the number of arrows
        # and the pair to compare with
        if points[c][1] < points[i][0]:
            n+=1
            c=i
    return n


if __name__ == '__main__':
    print(find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]))