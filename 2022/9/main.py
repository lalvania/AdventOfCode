import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.distance(other) == 0

    def __hash__(self):
        return hash(self.__repr__())


def print_grid_HT(head: Point, tail: Point, row = 6, col = 6):
    g = [["." for x in range(col)] for y in range(row)]
    g[0][0] = "s"
    g[tail.y][tail.x] = "T"
    g[head.y][head.x] = "H"
    for y in reversed(range(row)):
        print("".join(g[y]))
    print("")


def print_grid_knots(knots: dict, row = 6, col = 6):
    g = [["." for x in range(col)] for y in range(row)]

    g[0][0] = "s"
    for i, points in knots.items():
        p = knots[i][-1]
        c = g[p.y][p.x]
        if c in ["s", "."]:
            g[p.y][p.x] = str(i)
        else:
            g[p.y][p.x] = str(min(i, int(g[p.y][p.x])))
    head = knots[0][-1]
    g[head.y][head.x] = "H"
    for y in reversed(range(row)):
        print("".join(g[y]))
    print("")


def print_grid(l: list[Point], row = 6, col = 6):
    g = [["." for x in range(col)] for y in range(row)]
    for i in l:
        g[i.y][i.x] = '#'
    g[0][0] = "s"
    for y in reversed(range(row)):
        print("".join(g[y]))
    print("")


def move_head(head: Point, direction) -> Point:
    if direction == "R":
        return Point(head.x+1, head.y)
    elif direction == "L":
        return Point(head.x-1, head.y)
    elif direction == "U":
        return Point(head.x, head.y+1)
    elif direction == "D":
        return Point(head.x, head.y-1)

def move_tail(head: Point, tail: Point) -> Point:
    dx = head.x - tail.x
    dy = head.y - tail.y
    dist = math.hypot(dx, dy)
    if dist < 2:
        return Point(tail.x, tail.y)
    else:
        add_x = 1 if dx > 0 else 0 if dx == 0 else -1
        add_y = 1 if dy > 0 else 0 if dy == 0 else -1
        return Point(tail.x + add_x, tail.y + add_y)

def part1(file_path: str) -> int:
    head_pos = [Point(0, 0)]
    tail_pos = [Point(0, 0)]

    with open(file_path, "r") as f:
        for l in f.readlines():
            speed = l.strip().split(" ")[1]
            direction = l.strip().split(" ")[0]
            for i in range(int(speed)):
                head = move_head(head_pos[-1], direction)
                head_pos.append(head)
                tail = move_tail(head, tail_pos[-1])
                tail_pos.append(tail)
                # print(direction, i+1, dist)
                # print_grid_HT(head, tail_pos[-1]))
            # print(direction, speed)
            # print(head_pos)
            # print(tail_pos)
    # print(tail_pos)
    print(set(tail_pos))
    # print_grid(tail_pos)

    return len(set(tail_pos))

def part2(file_path: str, knot_length, grid_dims: list = [6, 6]) -> int:
    knots = {0: [Point(0, 0)]}

    with open(file_path, "r") as f:
        for l in f.readlines():
            speed = l.strip().split(" ")[1]
            direction = l.strip().split(" ")[0]
            for i in range(int(speed)):
                head = move_head(knots[0][-1], direction)
                knots[0].append(head)
                for xs in range(1, knot_length):
                    if xs not in knots:
                        knots[xs] = [Point(0, 0)]
                    curr_head = knots[xs-1][-1]
                    curr_tail = knots[xs][-1]
                    knots[xs].append(move_tail(curr_head, curr_tail))

            if grid_dims:
                print("==", direction, speed, "==")
                print_grid_knots(knots, grid_dims[0], grid_dims[1])
                # print(direction, speed)
                # print(head_pos)
                # print(tail_pos)

    print(set(knots[knot_length-1]))
    return len(set(knots[knot_length-1]))


if __name__ == '__main__':
    # test
    # print(part1("resources/test")) # 13
    # print(part2("resources/test", 2)) # 13
    # print(part2("resources/test", 9)) # 1

    # test2
    print(part2("resources/test2", 10, [30, 30])) # 36

    # input
    # print(part1("resources/input"))
    print(part2("resources/input", 10, None))
