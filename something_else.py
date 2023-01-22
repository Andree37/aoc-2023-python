def solve():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    other_numbers = [123, 122, 41, 3, 2123, 4, 123, 5123, 123, 50, 235, 123, 12, 542, 432, 78, 9]
    result = []
    for i, num in enumerate(numbers):
        if other_numbers[i] % num == 0:
            result.append((num, other_numbers[i]))
    return result


print(solve())
