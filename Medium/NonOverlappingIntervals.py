from typing import List


def earase_overlap_intervals(intervals: List[List[int]]) -> int:
    # sort intervals according to heights value
    intervals = sorted(intervals, key=lambda x: x[1])

    # init answer and compare to index
    current_index = 0
    ans = 0

    for indx in range(1, len(intervals)):
        # check if there is an overlap
        if intervals[current_index][1] > intervals[indx][0]:
            ans += 1
        # if there isn't update the index to compare to
        else:
            current_index = indx

    return ans


if __name__ == '__main__':
    print(earase_overlap_intervals([[1,100],[11,22],[1,11],[2,12]]))
