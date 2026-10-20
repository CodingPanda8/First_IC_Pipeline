
"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    first_clean = first.replace(" ", "").lower()
    second_clean = second.replace(" ", "").lower()

    return sorted(first_clean) == sorted(second_clean)