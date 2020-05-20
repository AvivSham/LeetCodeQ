def judge_circle(moves: str) -> bool:
    if len(moves) % 2 == 1:
        return False

    spot = [0, 0]
    for step in moves:
        if step == "U":
            spot[1] += 1
        elif step == "D":
            spot[1] -= 1
        elif step == "R":
            spot[0] += 1
        else:
            spot[0] -= 1

    return True if spot == [0, 0] else False


def judge_circle_ver2(moves: str) -> bool:
    return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")


def judge_circle_ver3(moves: str) -> bool:
        direction = {'L': 1, 'R': -1, 'U': 1j, 'D': -1j}
        return sum(direction[move] for move in moves) == 0


if __name__ == '__main__':
    print(judge_circle("UUUDDD"))
