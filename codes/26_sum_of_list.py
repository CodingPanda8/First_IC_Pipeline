
"""Program 26: Find the sum of list elements without sum()."""


def sum_of_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total