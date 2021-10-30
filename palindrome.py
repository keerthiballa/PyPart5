def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """

    return value.replace(" ", "").lower() == value[::-1].replace(" ","").lower()

# ballakeerthi@zipcodes-MacBook-Pro-3 PyPart5 % python3 -m unittest test_palindrome.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK