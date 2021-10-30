def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    first = "".join(sorted(first_string.replace(" ", "")))
    second = "".join(sorted(second_string.replace(" ", "")))

    return first== second

# ballakeerthi@zipcodes-MacBook-Pro-3 PyPart5 % python3 -m unittest test_anagram.py
# False
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK