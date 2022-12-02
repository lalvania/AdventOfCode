o_rock = "A"
o_paper = "B"
o_sissor = "C"

part2 = {
    "A X": 3,  # lose (0), opponent plays rock, you play scissor (3)
    "A Y": 4,  # draw (3), opponent plays rock, you play rock (1)
    "A Z": 8,  # win  (6), opponent plays rock, you play paper (2)
    "B X": 1,  # lose (0), opponent plays paper, you play rock (1)
    "B Y": 5,  # draw (3), opponent plays paper, you play paper (2)
    "B Z": 9,  # win  (6), opponent plays paper, you play scissor (3)
    "C X": 2,  # lose (0), opponent plays scissor, you play paper (2)
    "C Y": 6,  # draw (3), opponent plays scissor, you play scissor (3)
    "C Z": 7,  # win  (6), opponent plays scissor, you play rock (1)
}

part1 = {
    "A X": 7,  # win  (6), opponent plays scissor, you play rock  (1)
    "A Y": 4,  # draw (3), opponent plays rock, you play rock  (1)
    "A Z": 1,  # lose (0), opponent plays paper, you play rock  (1)
    "B X": 8,  # win  (6), opponent plays rock, you play paper  (2)
    "B Y": 5,  # draw (3), opponent plays paper, you play paper  (2)
    "B Z": 2,  # lose (0), opponent plays scissor, you play paper  (2)
    "C X": 9,  # win  (6), opponent plays paper, you play scissor (3)
    "C Y": 6,  # draw (3), opponent plays scissor, you play scissor (3)
    "C Z": 3,  # lose (0), opponent plays rock, you play scissor (3)
}


def run(file_path: str, d: dict) -> int:
    file = open(file_path, "r")
    x = 0
    for l in file.readlines():
        i = l.strip()
        x += d[i]
    return x


if __name__ == '__main__':
    # test
    print(run("resources/test", part1))
    print(run("resources/test", part2))

    # part 1
    print(run("resources/input", part1))
    print(run("resources/input", part2))
