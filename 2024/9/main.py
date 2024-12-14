# https://adventofcode.com/2024/day/9


def part1(filename) -> int:
    with open(filename, 'r') as f:
        line = [x.strip() for x in f.readlines()][0]
    diskmap = []
    for i, c in enumerate(line):
        if i % 2 == 0:
            # written block
            id = i // 2
            diskmap.extend([id] * int(c))
        else:
            # free block
            diskmap.extend([-1] * int(c))
    i = 0
    j = len(diskmap) - 1
    while i < j:
        if diskmap[i] != -1:
            i += 1
        else:
            diskmap[i] = diskmap[j]
            diskmap[j] = -1
            j -= 1

    return sum([i * x for i, x in enumerate(diskmap[:j+1])])


def part2(filename) -> int:
    with open(filename, 'r') as f:
        line = [x.strip() for x in f.readlines()][0]

    used = []
    free = []
    pos = 0

    for i, c in enumerate(line):
        if i % 2 == 0:
            # written block
            used.append( (pos, int(c)))
            pos += int(c)
        else:
            # free block
            free.append((pos, int(c)))
            pos += int(c)

    for i, (block_start, block_length) in list(enumerate(used))[::-1]:
        for j, (free_start, free_length) in enumerate(free):
            if block_start >= free_start and block_length <= free_length:
                used[i] = (free_start, block_length)  # update positions thus destroying old position
                free[j] = (free_start + block_length, free_length - block_length)
                break

    # math formula for partial sum
    # len * (first + last) // 2
    # len * (first + first + len) // 2
    ans = 0
    for i, (block_start, block_length) in list(enumerate(used)):
        ans += i * block_length * (2 * block_start + block_length - 1) // 2
    return ans


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))