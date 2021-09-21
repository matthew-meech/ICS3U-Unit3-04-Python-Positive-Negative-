#!/usr/bin/env python3

# Created by: Mr. Matthew Meech
# Created on: Sep 2021
# This program is a number guessing game


def main():

    # input
    integer = int(input("Enter number a integer:"))
    print("")

    # if ... then ... elseif
    if integer > 0:
        print("your number is positive")
    elif integer < 0:
        print("your number is negative")
    elif integer == 0:
        print("your number is just zero")

    print("\nDone.")


if __name__ == "__main__":
    main()
