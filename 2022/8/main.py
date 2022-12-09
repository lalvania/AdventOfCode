import math
from dataclasses import dataclass


@dataclass
class o:
    height: int = 0
    visible: bool = False


# Reset
Color_Off = '\033[0m'  # Text Reset

# Regular Colors
Red = '\033[0;31m'  # Red
Green = '\033[0;32m'  # Green


def print_grid(grid: list[list[o]], with_visibility: bool = False):
    print(f"{Color_Off}printing grid")
    for row in grid:
        r = []
        for tree in row:
            if with_visibility:
                r.append(f"{Red}x" if not tree.visible else f"{Green}{str(tree.height)}")
            else:
                r.append(str(tree.height))
        print("".join(r))
    print(f"{Color_Off}")


def read(file_path: str) -> list[list[o]]:
    grid = []
    with open(file_path, "r") as f:
        for l in f.readlines():
            content = [o(height=int(x)) for x in l.strip()]
            grid.append([x for x in content])
    return grid


def part1(file_path: str) -> int:
    grid = read(file_path=file_path)
    t_grid = list(zip(*grid))

    max_x = len(grid[0])
    max_y = len(grid)
    count = 0

    for y in range(max_y):
        for x in range(max_x):
            tree = grid[y][x]
            # scan_west
            if all([i.height < tree.height for i in grid[y][0:x]]):
                tree.visible = True
            # scan_east
            elif all([i.height < tree.height for i in grid[y][x + 1:]]):
                tree.visible = True
            # scan_north

            elif all([i.height < tree.height for i in t_grid[x][0:y]]):
                tree.visible = True
            # scan_south
            elif all([i.height < tree.height for i in t_grid[x][y + 1:]]):
                tree.visible = True
            count += 1 if tree.visible else 0
    # print_grid(grid, with_visibility=True)
    return count


def part2(file_path: str) -> int:
    grid = read(file_path=file_path)
    t_grid = list(zip(*grid))

    max_x = len(grid[0])
    max_y = len(grid)
    max_height = 0

    def scan_heights(tree_height: int, view: list[int]):
        c = 0
        for height in view:
            c += 1
            if height >= tree_height:
                break
        return c

    for y in range(1, max_y-1):
        for x in range(1, max_x-1):
            tree = grid[y][x]
            west = list(reversed([i.height for i in grid[y][0:x]]))
            east = [i.height for i in grid[y][x + 1:]]
            north = list(reversed([i.height for i in t_grid[x][0:y]]))
            south = [i.height for i in t_grid[x][y + 1:]]
            views = [west, east, south, north]
            scans = [scan_heights(tree.height, x) for x in views]
            height = math.prod(scans)
            # print(x, y, tree, list(zip(views, scans)), height)
            if height > max_height:

                max_height = height

    # print_grid(grid, with_visibility=True)
    return max_height


if __name__ == '__main__':
    # test
    print(part1("resources/test"))
    print(part2("resources/test"))

    # input
    print(part1("resources/input"))
    print(part2("resources/input"))
