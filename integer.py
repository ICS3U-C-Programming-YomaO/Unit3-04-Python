#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: October, 2025
# This program checks if the user input is positive or negative


def main():
    # ask user to guess number
    number = int(input("Enter an integer: "))

    # Tell user if number is postive, negative or zero
    if number > 0:
        print(" {} is a positive number!".format(number))
    elif number < 0:
        print("{} is a negative number".format(number))
    else:
        print("{} is just zero!".format(number))


if __name__ == "__main__":
    main()
