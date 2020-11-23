def is_path_crossing(path: str) -> bool:
    d = {'N': [0, 1], 'S': [0, -1], "E": [1, 0], "W": [-1, 0]}
    loc = [0, 0]
    p = [loc]
    for sub_path in path:
        new_loc = [i + j for i, j in zip(loc, d[sub_path])]
        if new_loc in p:
            return True
        else:
            p.append(new_loc)
            loc = new_loc
    return False
