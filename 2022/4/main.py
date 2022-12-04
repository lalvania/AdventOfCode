def check(s1, e1, s2, e2, c=0):
    """
    return True if:
    condition 1:
        s1---------e1
            s2---e2
    condition 2:
        s1------e1
            s2---------e2
    condition 3:
            s1------e1
        s2-------e2

    repeat checks again by swapping items 1 and 2

    :param s1: start of list 1
    :param e1: end of list 1
    :param s2: start of list 2
    :param e2: end of list2
    :param c: recursion count
    :return: Array of True or false. Part1 = index 0, and Part2 = index 1
    """
    p1, p2 = False, False

    if s1 <= s2 and e1 >= e2:
        p1, p2 = True, True
    elif s1 <= s2 <= e1 <= e2:
        p1, p2 = False, True
    elif e1 >= e2 >= s1 >= s2:
        p1, p2 = False, True

    if c == 1:
        return p1, p2
    else:
        r = check(s2, e2, s1, e1, 1)
        return p1 or r[0], p2 or r[1]


def part1(file_path: str) -> int:
    file = open(file_path, "r")
    x = 0
    for line in file.readlines():
        s1, e1, s2, e2 = map(int, line.strip().replace("-", ",").split(","))
        x += 1 if check(s1, e1, s2, e2)[0] else 0
    return x


def part2(file_path: str) -> int:
    file = open(file_path, "r")
    x = 0
    for line in file.readlines():
        s1, e1, s2, e2 = map(int, line.strip().replace("-", ",").split(","))
        x += 1 if check(s1, e1, s2, e2)[1] else 0
    return x


if __name__ == '__main__':
    # test
    print(part1("resources/test"))
    print(part2("resources/test"))

    # input
    print(part1("resources/input"))
    print(part2("resources/input"))
