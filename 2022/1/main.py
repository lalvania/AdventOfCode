# https://adventofcode.com/2022/day/1

def run(file_path: str, top: int = 1) -> int:
    file = open(file_path, "r")

    sum_cal = 0
    cals = []

    for l in file.readlines():
        if l == "\n":
            cals.append(sum_cal)
            sum_cal = 0
        else:
            sum_cal += int(l.strip())
    cals.append(sum_cal)
    cals.sort()
    return sum(cals[-top:])


if __name__ == '__main__':
    # test
    print(run("resource/test"))
    print(run("resource/test"), 3)

    # part 1
    print(run("resources/input"))

    # part 2
    print(run("resources/input", 3))
