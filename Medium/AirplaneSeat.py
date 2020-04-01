def nthPersonGetsNthSeat(n):
    """
    The answer: lets break down this problem into (3) options:
    1) person 1 seats in 1st seat
    2) person 1 seats in nth seat
    3) person 1 chooses seat between 2 to n-1

    1) if person 1 seats in 1st seat then problem solved since each one of the other persons will take their own seat
    including the nth passenger

    2) if the first person selects to seat in the nth seat there is no way that the nth passenger can sit in it's own
    seat

    3) for this case let us take an specific example: the first passenger selects the 20th seat, then all the passengers
    till the 20th one sit in their own seats. when the 20th person needs to select a seat either he select 1/n seat and
    the problem solved or it continues to exits. on the bottom line one of the passengers will have to chose between the
    first and last seat which resulting 0.5 probability for number of seats greater than 1.

    """
    if n == 1:
        return 1.0
    else:
        return 0.5


if __name__ == '__main__':
    print(nthPersonGetsNthSeat(2))