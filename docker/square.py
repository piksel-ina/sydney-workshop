#!/usr/bin/env python3

import argparse


# Return the square of a number
def square_number(num):
    return num * num


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the square of a number.")
    parser.add_argument("number", type=int, help="The number to be squared.")
    args = parser.parse_args()

    result = square_number(args.number)
    print(f"The square of {args.number} is {result}.")
