def str_len(str_in: str) -> int:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    return len(str_in)


# str_len('Hello!')


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    return str_in[0]


# first_char('Hello!')


def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    return str_in[len(str_in) - 1]


# last_char('Hello!')


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    return sub_str_in in str_in


# input_has_substring('Hello!', 'ell')


def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    return str_in[start:stop]


# substring('Congratulations!', 2, 5)


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """
    return str_in.swapcase()

# opposite_case('Hello!')

# ballakeerthi@zipcodes-MacBook-Pro-3 PyPart5 % python3 -m unittest test_string_utils.py
# ./Users/ballakeerthi/dev/PyPart5/test_string_utils.py:41: DeprecationWarning: Please use assertEqual instead.
#   self.assertEquals(expected, string_utils.input_has_substring(word, substring))
# .....
# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s
#
# OK