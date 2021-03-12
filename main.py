# Exercise to find the missing element of an unsorted list.
import random


def find_missing(numbers):
    # element of the list
    n = len(numbers) + 1
    # This is the sum of all element of the list (sum=36)
    real_sum_number = n * (n + 1) / 2
    print("Sum of the numbers from the real list: ", real_sum_number)

    # count sum of the numbers in list
    sum_list = sum(numbers)
    print("Sum of the numbers without x = ", sum_list)

    # return the missing number
    return real_sum_number - sum_list


def test(n):
    # missing element from 1 to n
    missing_element = random.randint(1, n)
    # List Array for the numbers called 'numbers'
    numbers = []
    # create the list without the missing element
    for i in range(1, n):
        if i != missing_element:
            numbers.append(i)

    # assign actual missing numbers using 'find_missing()' function
    actual_missing = find_missing(numbers)
    print("Expected Missing = ", missing_element, "Actual Missing = ", actual_missing)
    assert missing_element == actual_missing


def main():
    for n in range(1, 3):
        test(10)


main()
