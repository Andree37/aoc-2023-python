from math import floor


def solve():
    for line in get_input().splitlines():
        found_c = ''
        half_index = floor(len(line) / 2)
        compartment_0, compartment_1 = line[0: half_index], line[half_index:len(line)]  # 1 off?
        for c in compartment_0:
            if c in compartment_1:
                found_c = c

        print("c: {}".format(found_c))


def get_input() -> str:
    return """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


solve()
