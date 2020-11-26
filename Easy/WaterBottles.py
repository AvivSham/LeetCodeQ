def numWaterBottles(numBottles: int, numExchange: int) -> int:
    if numBottles < numExchange:
        return numBottles
    totalBottle = numBottles
    remainingBottles = numBottles
    while remainingBottles >= numExchange:
        toExchange = remainingBottles // numExchange
        totalBottle += toExchange
        remainingBottles = remainingBottles - toExchange * numExchange + toExchange
    return totalBottle


if __name__ == '__main__':
    print(numWaterBottles(22, 6))