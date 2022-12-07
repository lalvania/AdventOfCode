def sub(stream: str, length) -> int:
    left = 0
    for right, c in enumerate(stream):
        s = stream[left:right]
        if len(set(s)) == length:
            return right
        if right - left >= length:
            left += 1
    return 0


def part(file_path: str, length: int) -> list[int]:
    file = open(file_path, "r")
    out = []
    for l in file.readlines():
        print(l)
        out.append(sub(l.strip(), length))
    return out


if __name__ == '__main__':
    # test
    # print(part("resources/test"), 4)
    # print(part("resources/test", 14))

    # input
    # print(part("resources/input", 4))
    print(part("resources/input", 14))
