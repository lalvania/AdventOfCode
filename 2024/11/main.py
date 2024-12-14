# https://adventofcode.com/2024/day/11
from functools import cache


@cache
def blink_rules(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        mid = len(s) // 2
        return [int(s[:mid]), int(s[mid:])]
    else:
        return [stone * 2024]


@cache
def get_counts(stone: int, remaining_blinks: int) -> int:
    new_stones = blink_rules(stone)
    if remaining_blinks == 1:
        return len(new_stones)
    else:
        return sum(get_counts(s, remaining_blinks-1) for s in new_stones)


def iterate(filename, blinks=25) -> int:
    with open(filename, 'r') as f:
        line = [x.strip() for x in f.readlines()][0]
        stones = [int(stone) for stone in line.split(" ")]

    return sum([get_counts(s, blinks) for s in stones])


def part1(filename):
    return iterate(filename, 25)


def part2(filename) -> int:
    return iterate(filename, 75)


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))