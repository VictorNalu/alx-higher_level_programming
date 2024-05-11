#!/usr/bin/python3
"""
A module designed to identify a peak element
in an unsorted list of integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: Peak value found in the list.
    """
    if not list_of_integers:
        return None  # Handle empty list case

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
