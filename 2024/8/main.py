# https://adventofcode.com/2024/day/8
import concurrent.futures
import itertools
from collections import defaultdict


def print_grid(s: set, x_max, y_max):
    for y in range(y_max):
        l = ""
        for x in range(x_max):
            if (x, y) in s:
                l += "#"
                s.remove((x, y))
            else:
                l += "."
        print(l, l.count("#"))
    print(s)


def read_grid(filename) -> (dict, int, int):
    d = defaultdict(set)
    with open(filename, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != '.':
                    d[char].add((x, y))
    return d, len(lines[0]), len(lines)


def is_in_bounds(x, y, x_max, y_max) -> bool:
    return 0 <= x < x_max and 0 <= y < y_max


def part1(filename) -> int:
    grid, x_max, y_max = read_grid(filename)

    def new_coord(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        vx = 1 if x1 < x2 else -1
        x = x2 + (vx * dx)

        dy = abs(y2 - y1)
        vy = 1 if y1 < y2 else -1
        y = y2 + (vy * dy)

        return x, y

    def process_char(char):
        antinodes = []
        for combos in itertools.permutations(grid[char], 2):
            x1, y1 = combos[0]
            x2, y2 = combos[1]
            antinodes.append(new_coord(x1,y1,x2,y2))
        return antinodes

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(process_char, grid.keys())
        ans = set()
        for result in results:
            for coord in result:
                ans.add(coord)
        return sum([1 for x, y in ans if is_in_bounds(x, y, x_max, y_max)])


def part2(filename) -> int:
    grid, x_max, y_max = read_grid(filename)

    def new_coord(x1, y1, x2, y2) -> set[tuple[int, int]]:
        coords = set()
        dx = abs(x2 - x1)
        vx = 1 if x1 < x2 else -1

        dy = abs(y2 - y1)
        vy = 1 if y1 < y2 else -1

        while is_in_bounds(x2, y2, x_max, y_max):
            coords.add((x2, y2))
            x2 += (vx * dx)
            y2 += (vy * dy)
        return coords

    def process_char(char):
        antinodes = []
        for combos in itertools.permutations(grid[char], 2):
            x1, y1 = combos[0]
            x2, y2 = combos[1]
            antinodes.extend(new_coord(x1,y1,x2,y2))
        return antinodes

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(process_char, grid.keys())
        ans = set()
        for result in results:
            for coord in result:
                ans.add(coord)
        # print(len(ans))
        # print_grid(ans, x_max, y_max)
        return sum([1 for x, y in ans if is_in_bounds(x, y, x_max, y_max)])


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))
