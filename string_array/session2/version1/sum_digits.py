


def sum_of_digits(num):
    sum = 0

    while num > 0:
        sum += num % 10
        num //= 10
    return sum

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))