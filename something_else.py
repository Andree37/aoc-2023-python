def solve():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    other_numbers = [123, 122, 41, 3, 2123, 4, 123, 5123, 123, 50, 235, 123, 12, 542, 432, 78, 9]
    result = []
    for i, num in enumerate(numbers):
        if other_numbers[i] % num == 0:
            result.append((num, other_numbers[i]))
    return result


def prime():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    result = map(lambda x: (is_prime(x), x), numbers)
    print(list(result))


def is_prime(n):
    return (4 > n > 0) or (n % 2 != 0 and n % 3 != 0)


def is_pow_2(n):
    bits = bin(n)
    count = 0
    for b in bits:
        if b == "1":
            count += 1
    return count == 1


print(is_pow_2(0))
print(is_pow_2(1))
print(is_pow_2(2))
print(is_pow_2(3))
print(is_pow_2(6))
print(is_pow_2(8))
print(is_pow_2(9))
print(is_pow_2(12))
print(is_pow_2(16))
