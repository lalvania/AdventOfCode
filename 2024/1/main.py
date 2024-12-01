# https://adventofcode.com/2022/day/1
from collections import defaultdict


def part1(file_path: str) -> int:
    l = []
    r = []
    diff = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            x, y = line.split("   ")
            l.append(int(x))
            r.append(int(y))

    l.sort()
    r.sort()

    for i, j in zip(l, r):
        diff.append(abs(i - j))
    return sum(diff)

def part2(file_path: str) -> int:
    l = []
    r = defaultdict(int)
    sim = 0
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            x, y = line.split("   ")
            l.append(int(x))
            r[int(y)] += 1

    for i in l:
        if i in r:
            sim += i * r[i]
    return sim

if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))
