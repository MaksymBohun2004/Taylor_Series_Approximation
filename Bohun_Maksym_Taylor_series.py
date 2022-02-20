from math import log as ln
from functools import lru_cache
import matplotlib.pyplot as plt
import sys


def get_input():
    while True:
        x = input('Enter the value of x:\n>>> ')
        if x == '1':
            print("1 isn't in the working function area, try a different x value!")
        else:
            try:
                x = float(x)
                break
            except ValueError:
                print('Please, Enter a correct value')
    while True:
        n = input('Enter the number of terms:\n>>> ')
        try:
            n = int(n)
            break
        except ValueError:
            print('Please, Enter a correct value')
    return x, n


@lru_cache()
def factorial(num):
    """
    Recursively calculates the factorial of a number
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    if num < 0:
        return None
    elif num <= 1:
        return 1
    return num * factorial(num - 1)


def calculate(x, n):
    """
    Main function of the program.
    Calculates the approximation with x = x and n terms.
    >>> calculate(1, 10)
    Series diverges!
    >>> calculate(2, 5)
    -3.9996585622122782
    """
    res = 0
    for k in range(-1, n):
        try:
            res += ((-1 + x) ** k *
                    (-2) * (ln(2)) ** (1 + k)) / factorial(1 + k)
        except ZeroDivisionError:
            print('Series diverges!')
            return None
    return res


def plot_difference(x):
    """
    This function plots the difference between the approximation
    with different numbers of terms and the real function
    """
    n = abs(x * 2)
    if n < 15:
        n = 15
    n = int(round(n, 0))
    x_numbers = [calculate(x, num) for num in range(1, n)]
    y_numbers = [y for y in range(1, n)]
    plt.plot(y_numbers, x_numbers, label="Approximation",
             color='green', linestyle='dashed', linewidth=6,
             marker='o', markerfacecolor='blue', markersize=10)
    real_res = (2 ** x) / (1 - x)
    real_x = [real_res for _ in range(1, n)]
    real_y = [i for i in range(1, n)]
    plt.plot(real_y, real_x, label="Real Function", color='red', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=1)
    plt.ylabel('Result')
    plt.xlabel('Number of terms')
    plt.legend()
    plt.show()


def number_of_terms(x):
    """
    Prints out the minimum number of terms
    for the approximation to be exact
    >>> number_of_terms(10) #doctest: +ELLIPSIS
    For difference between approximation and function to be less than...
    """
    numbers_of_terms = {}
    real_res = (2 ** x) / (1 - x)
    for n in range(1, 170):
        res = calculate(x, n)
        difference = abs(real_res - res)
        if difference < 10**(-6):
            if '-6' not in numbers_of_terms:
                numbers_of_terms['-6'] = n
        if difference < 10**(-3):
            if '-3' not in numbers_of_terms:
                numbers_of_terms['-3'] = n
        if difference < 10**(-1):
            if '-1' not in numbers_of_terms:
                numbers_of_terms['-1'] = n
        if len(numbers_of_terms) == 3:
            break
    print('For difference between approximation and function to be less than:')
    if '-6' in numbers_of_terms:
        print(f"\t10^(-6): {numbers_of_terms['-6']} terms needed;")
    else:
        print("\t10^(-6): more than 170;")
    if '-3' in numbers_of_terms:
        print(f"\t10^(-3): {numbers_of_terms['-3']} terms needed;")
    else:
        print("\t10^(-3): more than 170;")
    if '-1' in numbers_of_terms:
        print(f"\t10^(-1): {numbers_of_terms['-1']} terms needed.")
    else:
        print("\t10^(-1): more than 170.")


def main():
    """
    Main function of the program that gives user
    the needed info and navigates through the helping functions
    """
    print('This program will turn the function 2^x/(1-x) to Taylor series,')
    print('plot the difference between the approximation and the real function,')
    print('and show how many terms are enough for the approximation to be as exact as possible!')
    while True:
        try:
            x, n = get_input()
            plot_difference(x)
            number_of_terms(x)
            print(f"The real function 2^{x}/(1-{x}) = {2**x/(1-x)}")
            res = calculate(x, n)
            print(f"The approximation with n={n} and x={x} gives the result {res}.")
            print(f"The difference is {abs(2**x/(1-x) - res)}")
            sys.exit()
        except OverflowError:
            print('You entered too big of numbers, please, try again!')


if __name__ == "__main__":
    main()
