# https://adventofcode.com/2024/day/7
import concurrent.futures
import itertools


def split_lines(l) -> (int, list):
    solution = int(l.split(':')[0].strip())
    numbers = [int(i.strip()) for i in l.split(':')[1].split(' ') if len(i.strip()) > 0]
    return solution, numbers


def handle_ops(numbers, solution, ops):
    val = numbers[0]
    for j, op in enumerate(ops):
        if op == "+":
            val += numbers[j+1]
        elif op == "*":
            val *= numbers[j+1]
        elif op == "|":
            val = int(str(val) + str(numbers[j+1]))
        if val > solution:
            return -1
    if val == solution:
        return solution


def process_line(args):
    solution, numbers = split_lines(args[0])
    symbols = args[1]

    for ops in itertools.product(symbols, repeat=len(numbers)-1):
        x = handle_ops(numbers, solution, ops)
        if x == solution:
            return solution
    return -1

def part1(filename):
    symbols = "*+"
    with open(filename, 'r') as f:
        lines = [(x, symbols) for x in f.readlines()]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(process_line, lines)
            return sum([r for r in results if r > 0])


def part2(filename):
    symbols = "*+|"
    with open(filename, 'r') as f:
        lines = [(x.replace("||", "|"), symbols) for x in f.readlines()]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(process_line, lines)
            return sum([r for r in results if r > 0])


if __name__ == '__main__':
    # test 1
    print(part1("resources/test"))

    # part 1
    print(part1("resources/input"))

    # test 2
    print(part2("resources/test"))

    # part 2
    print(part2("resources/input"))
