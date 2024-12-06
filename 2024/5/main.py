# https://adventofcode.com/2024/day/5
from collections import defaultdict

from typing import Dict, List


def parse(filename: str):
    rules = defaultdict(list)
    updates = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if "|" in line:
                x, y = list(map(int, line.split("|")))
                rules[y].append(x)
            elif "," in line:
                updates.append([int(x.strip()) for x in line.split(",")])
    return rules, updates


def invalid_position(rules: Dict[int, list], update: List[int]) -> (int, set):
    for i, page in enumerate(update):
        # print("checking:", page, "for: ", rules[page], "in ", update[i+1:])
        if set(rules[page]) & set(update[i+1:]):
            return i, set(rules[page]) & set(update[i + 1:])
    return -1, set()


def median(update: List[int]) -> int:
    return update[len(update)//2]


def main(filename):
    rules, updates = parse(filename)
    part1 = 0
    part2 = 0
    for update in updates:
        bad_pos, s = invalid_position(rules, update)
        if bad_pos < 0:
            part1 += median(update)
        else:
            while bad_pos >= 0:
                bad_pos, s = invalid_position(rules, update)
                if s:
                    good_pos = update.index(list(s)[0])
                    update[bad_pos], update[good_pos] = update[good_pos], update[bad_pos]
            part2 += median(update)
    print(part1, part2)


if __name__ == '__main__':
    # test
    main("resources/test")

    # real
    main("resources/input")
