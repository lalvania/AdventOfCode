# https://adventofcode.com/2024/day/10
from collections import deque, defaultdict
from itertools import product

# orthogonal directions only
directions = [
    (x,y)
    for x,y in product([-1, 0, 1], repeat=2)
    if not (x == 0 and y == 0) and x*y == 0
]


def is_in_bounds(x, y, x_bounds, y_bounds) -> bool:
    return 0 <= x < x_bounds and 0 <= y < y_bounds


def part1(filename) -> int:
    trailheads = set()

    with open(filename, 'r') as f:
        grid = [x.strip() for x in f.readlines()]
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == '0':
                    trailheads.add((x, y))
        x_bounds = len(grid[0])
        y_bounds = len(grid)

    count = 0
    for trailhead in trailheads:
        levels = defaultdict(set)
        levels[0].add(trailhead)
        for level in range(1, 9+1):
            for x, y in levels[level-1]:
                for dx, dy in directions:
                    if is_in_bounds(x+dx, y+dy, x_bounds, y_bounds) and grid[y+dy][x+dx] == str(level):
                        levels[level].add((x+dx, y+dy))
            # print(trailhead, level, levels[level])
        count += len(levels[9])

    return count





def part2(filename) -> int:
    trailheads = set()

    with open(filename, 'r') as f:
        grid = [x.strip() for x in f.readlines()]
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == '0':
                    trailheads.add((x, y))
        x_bounds = len(grid[0])
        y_bounds = len(grid)

    count = 0
    for trailhead in trailheads:
        visited = set()
        queue = deque([trailhead])
        local_count = 0
        while queue:
            # print(queue)
            x,y = queue.pop()
            if (x,y) not in visited:
                # visited.add((x,y))
                level = grid[y][x]
                next_level = str(int(level) + 1)
                # print("Scouting level:", level)
                if level == '9':
                    local_count += 1
                else:
                    # explore all nodes
                    for dx,dy in directions:
                        if is_in_bounds(x+dx, y+dy, x_bounds, y_bounds) and grid[y+dy][x+dx] == next_level:
                            # print("pushing", (x,y), (x+dx,y+dy))
                            queue.append((x+dx,y+dy))
        # print(trailhead, local_count)
        count += local_count

    return count


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))