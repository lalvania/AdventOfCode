from collections import namedtuple

Action = namedtuple("Action", ["count", "start", "end"])


def read(file_path: str) -> (list, list[Action]):
    file = open(file_path, "r")
    piles_strings = []
    reading_piles = True
    actions = []
    piles = []
    for line in file.readlines():
        if line.startswith("move"):
            reading_piles = False

        if reading_piles:
            piles_strings.append(line)
        else:
            x, y, z = map(int, line
                          .replace("move ", " ")
                          .replace(" from ", " ")
                          .replace(" to ", " ")
                          .strip()
                          .split(" "))
            actions.append(Action(x, y, z))

    for l in reversed(piles_strings[:-2]):
        row = [l[i:i+4].strip().replace('[', '').replace(']', '') for i in range(0, len(l), 4)]
        for i, r in enumerate(row):
            while len(piles) < i+1:
                piles.append([])
            if r:
                piles[i].append(r)
    return piles, actions


def print_grid(piles: list):
    for i in piles:
        print(i)


def part1(file_path: str) -> str:
    piles, actions = read(file_path=file_path)
    print_grid(piles)
    for a in actions:
        print(a)
        for i in range(a.count):
            piles[a.end-1].append(piles[a.start-1].pop())
        print_grid(piles)

    return "".join([i[-1] for i in piles])


def part2(file_path: str) -> str:
    piles, actions = read(file_path=file_path)
    print_grid(piles)
    for a in actions:
        print(a)
        temp = piles[a.start-1][-a.count:]
        print("temp:", temp)
        piles[a.start-1] = piles[a.start-1][0:-a.count]
        piles[a.end-1].extend(temp)
        print_grid(piles)

    return "".join([i[-1] for i in piles])




if __name__ == '__main__':
    # test
    #print(part1("resources/test"))
    print(part2("resources/test"))

    # input
    # print(part1("resources/input"))
    print(part2("resources/input"))
