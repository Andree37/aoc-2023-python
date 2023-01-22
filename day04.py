def solve():
    result = 0
    for line in get_input().splitlines():
        [elf0, elf1] = line.split(',')
        # get left right of elf0
        elf0left, elf0right = get_left_right(elf0)
        elf1left, elf1right = get_left_right(elf1)
        if (elf0left >= elf1left and elf0right <= elf1right) or (elf0left <= elf1left and elf0right >= elf1right):
            result += 1

    print("result: {}".format(result))


def get_left_right(elf):
    [left, right] = elf.split('-')
    return int(left), int(right)


def get_input() -> str:
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


solve()
