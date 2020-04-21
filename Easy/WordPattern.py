def wordPattern(pattern: str, str: str) -> bool:
    str = str.split(" ")

    if len(pattern) != len(str):
        return False

    map = {pattern[0]: str[0]}

    for p, word in zip(pattern[1:], str[1:]):

        if (p not in map.keys()) and (word not in map.values()):
            map[p] = word

        elif (p in map.keys()) and (map[p] != word):
            return False

        elif (p not in map.keys()) and (word in map.values()):
            return False

    return True


if __name__ == '__main__':
    print(wordPattern("baaa","dog dog dog dog"))