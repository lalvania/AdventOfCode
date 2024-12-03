# https://adventofcode.com/2024/day/3

def part1(filename: str) -> int:
    import re
    pattern = "mul\(\d+,\d+\)"
    sums = 0
    with open(filename, 'r') as f:
        lines = "\n".join(f.readlines())
        for i in re.findall(pattern, lines):
            x, y = i.replace("mul(", "").replace(")", "").split(",")
            sums += int(x)*int(y)
    return sums

def part2(filename: str) -> int:
    import re
    pattern = "(mul\(\d+,\d+\)|do\(\)|don't\(\))"
    sums = 0
    isDisabled = False
    with open(filename, 'r') as f:
        lines = "\n".join(f.readlines())
        for i in re.findall(pattern, lines):
            if i == 'do()':
                isDisabled = False
                continue
            elif i == "don't()":
                isDisabled = True
                continue

            if isDisabled:
                continue

            x, y = i.replace("mul(", "").replace(")", "").split(",")
            sums += int(x)*int(y)
    return sums


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test2"))

    # part 2
    print(part2("resources/input"))
