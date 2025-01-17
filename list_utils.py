from typing import List
import math


def get_item_at_position(list_in: List, pos: int) -> List:
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """
    return list_in[pos]


# print(get_item_at_position(['a', 'b', ['d', 'e', 'f']],0))


def print_list_items(list_in: List) -> None:
    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """
    for i in list_in:
        print(i)


# print_list_items(['a', 'b', ['d', 'e', 'f']])


def sort_by_commit_count(list_in: List) -> List:
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
    new_list = sorted(list_in, key=lambda list_in: list_in[1])
    return new_list


# print(sort_by_commit_count([['T', 4], ['A', 3], ['B', 6], ['H', 10]]))


def gen_list_of_nums(n: int) -> List[int]:
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).

    :param n: The number of items the result should contain
    :return: A list of integers
    """
    list = []
    for i in range(n):
        list.append(i)
    return list


# print(gen_list_of_nums(90))

def half_list(list_in: List, half: int) -> List:
    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the return value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """
    length = len(list_in)//2
    #print(length)
    if half == 1:
        if len(list_in)%2==0:
            return list_in[:length]
        else:
            return list_in[:length+1]
    elif half == 2:
        if len(list_in)%2==0:
            return list_in[length:]
        else:
            return list_in[length:]
    else:
        return ['invalid input']


#print(half_list([['T', 4], ['A', 3], ['B', 6], ['H', 10]],1))
#print(half_list([['T', 4], ['A', 3], ['B', 6], ['H', 10], ['R', 2]],1))



def remove_odds(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the odd numbers from the same list.

    :return: None
    """
    for i in list_in:
        if i % 2 == 0:
            continue
        else:
            list_in.remove(i)
    #print(list_in)


#remove_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


def remove_evens(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the even numbers from the same list.

    :return: None
    """
    for i in list_in:
        if i % 2 == 0:
            list_in.remove(i)
        else:
            continue
    #print(list_in)


#remove_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


def concatenate_lists(list_a: List, list_b: List) -> List:
    """
    Given two lists, this function combines them and returns the result as a new list.

    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    list_c = list_a + list_b
    return list_c


# print(concatenate_lists(['Summer'], ['Fall', ['Winter', 'Spring']]))


def multiply_list(list_in: List, scalar: int) -> List:
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.

    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """
    list_new = list_in * scalar
    return list_new

# print(multiply_list([['Summer'], ['Fall', ['Winter', 'Spring']]],2))



# ballakeerthi@zipcodes-MacBook-Pro-3 PyPart5 % python3 -m unittest test_list_utils.py
# .........
# ----------------------------------------------------------------------
# Ran 9 tests in 0.001s
#
# OK