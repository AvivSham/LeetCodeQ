from typing import List


def lastStoneWeight(stones: List[int]) -> int:

    while len(stones) > 1:

        y = stones.pop(stones.index(max(stones)))
        x = stones.pop(stones.index(max(stones)))

        if y - x != 0:
            stones.append(y - x)

    if len(stones) == 1:
        return stones[0]
    else:
        return 0


if __name__ == '__main__':
    print(lastStoneWeight([1, 1]))
