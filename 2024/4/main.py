# https://adventofcode.com/2024/day/4

def part1(filename: str) -> int:
    directions = [
        (-1,  1), (0,  1), (1,  1),
        (-1,  0),          (1,  0),
        (-1, -1), (0, -1), (1, -1),
    ]
    counter = 0

    with open(filename, 'r') as f:
        lines = f.readlines()
        max_i = len(lines)
        max_j = len(lines[0].strip())
        for i in range(max_i):
            for j in range(max_j):
                if lines[i][j] == 'X':
                    for x,y in directions:
                        m_pos = [i+x, j+y]
                        a_pos = [i+x*2, j+y*2]
                        s_pos = [i+x*3, j+y*3]
                        # print(i,j, (x,y), m_pos, a_pos, s_pos)
                        #bounds check:
                        if s_pos[0] < 0 or s_pos[0] >= max_i:
                            continue
                        if s_pos[1] < 0 or s_pos[1] >= max_j:
                            continue
                        m_check = lines[m_pos[0]][m_pos[1]] == "M"
                        a_check = lines[a_pos[0]][a_pos[1]] == "A"
                        s_check = lines[s_pos[0]][s_pos[1]] == "S"

                        if all([m_check, a_check, s_check]):
                            counter += 1
    return counter


def part2(filename: str) -> int:
    m_dirs = [(-1,  1), (-1, -1)]
    s_dirs = [(1,  1), (1, -1)]

    counter = 0

    with open(filename, 'r') as f:
        lines = f.readlines()
        max_i = len(lines)
        max_j = len(lines[0].strip())
        for i in range(max_i):
            for j in range(max_j):
                if lines[i][j] == 'A':
                    if i - 1 < 0 or i + 1 >= max_i:
                        continue
                    if j - 1 < 0 or j + 1 >= max_j:
                        continue
                    c = [
                        lines[i - 1][j - 1],
                        lines[i + 1][j - 1],
                        lines[i - 1][j + 1],
                        lines[i + 1][j + 1],
                    ]
                    print(i, j, c)
                    if c.count("M") == 2 and c.count("S") == 2 and c[0] != c[3]:
                        counter += 1
    return counter


if __name__ == '__main__':
    # test 1
    # print(part1("resources/test"))

    # part 1
    # print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))
