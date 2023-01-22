def solve():
    result = [0]
    current_elf = 0
    for line in get_input().splitlines():
        if line == "":
            current_elf += 1
            result.append(0)
        else:
            result[current_elf] += int(line)
    result.sort(reverse=True)
    print("result: {}".format(result[0]))


def get_input() -> str:
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

"""


solve()
