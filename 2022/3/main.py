import functools

lower = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z')+1)}
upper = {chr(i): i - ord('A') + 27 for i in range(ord('A'), ord('Z')+1)}
d = lower | upper


def part1(file_path: str) -> int:
    file = open(file_path, "r")
    x = 0
    for l in file.readlines():
        i = l.strip()
        left = i[:len(i) // 2]
        right = i[len(i) // 2:]
        sets = [left, right]
        common = ''.join(functools.reduce(set.intersection, sets[1:], set(sets[0])))
        x += d[common]
        # print(len(i), i, left, right, common)
    return x


def part2(file_path:str) -> int:
    file = open(file_path, "r")
    x = 0
    c = 0
    sets = []
    for l in file.readlines():
        i = l.strip()
        if c == 3:
            common = ''.join(functools.reduce(set.intersection, sets[1:], set(sets[0])))
            x += d[common]
            sets = []
            c = 0
        c += 1
        sets.append(i)
    common = ''.join(functools.reduce(set.intersection, sets[1:], set(sets[0])))
    x += d[common]
    return x


if __name__ == '__main__':
    # test
    print(part1("resources/test"))
    print(part2("resources/test"))

    # part 1
    print(part1("resources/input"))

    # part 2
    print(part2("resources/input"))
