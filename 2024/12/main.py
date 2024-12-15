# https://adventofcode.com/2024/day/12
from collections import defaultdict
from itertools import product


orthogonal = [
    (x,y)
    for x,y in product([-1, 0, 1], repeat=2)
    if not (x == 0 and y == 0) and x*y == 0
]


def find_region(coords: set) -> list[set]:
    regions = []
    visited = set()

    def dfs(root) -> set:
        stack = [root]
        group = set()
        while stack:
            current = stack.pop()
            x0, y0 = current
            if current not in visited:
                visited.add(current)
                group.add(current)

                for x, y in [(x0+dx, y0+dy) for dx, dy in orthogonal]:
                    if (x, y) in coords and (x, y) not in visited:
                        stack.append((x, y))
        return group

    for coord in coords:
        if coord not in visited:
            regions.append(dfs(coord))

    return regions


def find_costs(filename, price_func) -> int:
    plots = defaultdict(set)
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        for y, line in enumerate(lines):
            for x, plant in enumerate(line):
                plots[plant].add((x, y))
    cost = 0
    for plant in plots:
        for region in find_region(plots[plant]):
            cost += price_func(region)

    return cost


def part1(filename):
    def price(coords: set) -> int:
        area = len(coords)
        perimeter = area * 4
        for x, y in coords:
            for dx, dy in orthogonal:
                if (x + dx, y + dy) in coords:
                    perimeter -= 1
        return area * perimeter

    return find_costs(filename, price)


def part2(filename):
    def price(coords: set) -> int:
        area = len(coords)
        perimeter = 0 # counting corners

        for x, y in coords:
            N = (x + 0, y - 1) in coords
            S = (x + 0, y + 1) in coords
            E = (x + 1, y + 0) in coords
            W = (x - 1, y + 0) in coords
            NW = (x - 1, y - 1) in coords
            NE = (x + 1, y - 1) in coords
            SW = (x - 1, y + 1) in coords
            SE = (x + 1, y + 1) in coords

            if sum([N, S, W, E]) == 0:
                # this is a box
                perimeter += 4
            elif sum([N, S, W, E]) == 1:
                # if it has 3 edges: 2 corners
                perimeter += 2
            elif sum([N, S, W, E]) == 2 and sum([N, S]) == 1 and sum([E, W]) == 1:
                # adjancent edges: 1 corner
                perimeter += 1

            # L shapes also generate 1 point
            # X X
            # X
            if S and E and not SE:
                perimeter += 1
            # X X
            #   X
            if S and W and not SW:
                perimeter += 1
            #   X
            # X X
            if N and W and not NW:
                perimeter += 1
            # X
            # X X
            if N and E and not NE:
                perimeter += 1

        return area * perimeter

    return find_costs(filename, price)


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))