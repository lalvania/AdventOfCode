# https://adventofcode.com/2024/day/6
import concurrent.futures

dir_map = {
    '^': {"x":  0, "y": -1, "new_dir": ">"},
    'v': {"x":  0, "y":  1, "new_dir": "<"},
    '<': {"x": -1, "y":  0, "new_dir": "^"},
    '>': {"x":  1, "y":  0, "new_dir": "v"},
}


def is_in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def get_start(lines) -> tuple[int, int]:
    for i, line in enumerate(lines):
        if '^' in line:
            return line.index('^'), i


def part1VisitedSet(lines):
    visited = set()
    height = len(lines)
    width = len(lines[0].strip())

    pos = get_start(lines)
    direction = '^'

    while is_in_bounds(pos[0], pos[1], width, height):
        if pos not in visited:
            visited.add(pos)
        new_pos = (pos[0] + dir_map[direction]["x"], pos[1] + dir_map[direction]["y"])
        # print(pos, new_pos, direction, lines[new_pos[1]][new_pos[0]])
        if not is_in_bounds(new_pos[0], new_pos[1], width, height):
            return visited
        elif lines[new_pos[1]][new_pos[0]] == "#":
            direction = dir_map[direction]["new_dir"]
        else:
            pos = new_pos

    return visited


def part1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return len(part1VisitedSet(lines))


def part2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0].strip())

    _pos = get_start(lines)
    _direction = '^'

    def is_loop(obstacle: tuple[int, int]) -> bool:
        visited = set()
        pos = _pos
        direction = _direction
        while is_in_bounds(pos[0], pos[1], width, height):
            if (pos, direction) in visited:
                return True
            else:
                visited.add((pos, direction))

            new_pos = (pos[0] + dir_map[direction]["x"], pos[1] + dir_map[direction]["y"])
            # print(pos, new_pos, direction, lines[new_pos[1]][new_pos[0]])
            if not is_in_bounds(new_pos[0], new_pos[1], width, height):
                # walk off the map
                return False
            elif lines[new_pos[1]][new_pos[0]] == "#" or (new_pos[0] == obstacle[0] and new_pos[1] == obstacle[1]):
                direction = dir_map[direction]["new_dir"]
            else:
                pos = new_pos
        return False

    # brute force with threading:
    # coordinates = [(x, y) for x in range(width) for y in range(height)]
    coordinates = part1VisitedSet(lines)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(is_loop, coordinates)
        return sum(1 for result in results if result)


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))
