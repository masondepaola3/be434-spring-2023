#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-02-07
Purpose: sum up numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='sum up numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='INT',
                        type=int,
                        nargs='+',
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Sum numbers """

    args = get_args()

    numbers = []
    total = 0
    for num in args.numbers:
        numbers.append(str(num))
        total += num

    print('{} = {}'.format(' + '.join(numbers), total))

# --------------------------------------------------
if __name__ == '__main__':
    main()
