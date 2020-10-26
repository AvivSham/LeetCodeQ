from typing import List


def sub_domain_visits(cpdomains: List[str]) -> List[str]:

    diction = {}

    for s in cpdomains:
        count, dom = s.split()
        count = int(count)
        dom = dom.split(".")

        for i in range(len(dom)):
            k = ".".join(dom[i:])
            diction[k] = diction.get(k, 0) + count

    return [str(i[1]) + " " + i[0] for i in diction.items()]


if __name__ == '__main__':
    print(sub_domain_visits(["9001 discuss.leetcode.com"]))
