# https://adventofcode.com/2024/day/2

def isSafe(report: list) -> bool:
    def zipper():
        return zip(report[:-1], report[1:])
    diffs = all(i in [1, 2, 3] for i in [abs(i - j) for i, j in zipper()])
    isInc = all(i < j for i, j in zipper())
    isDec = all(i > j for i, j in zipper())

    # print(report, diffs, isInc, isDec)
    return (isInc or isDec) and diffs


def part1(filename: str) -> int:
    with open(filename, 'r') as f:
        lines = f.readlines()
        sum = 0
        for report in lines:
            sum += 1 if isSafe([int(x) for x in report.strip().split(" ")]) else 0
        return sum


def part2(filename: str) -> int:
    with open(filename, 'r') as f:
        lines = f.readlines()
        sum = 0
        for report in lines:
            r = [int(x) for x in report.strip().split(" ")]
            if isSafe(r):
                sum += 1
            else:
                for i in range(len(r)):
                    r2 = r[:i] + r[i+1:]
                    if isSafe(r2):
                        # print(r, r2)
                        sum += 1
                        break
        return sum


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))
