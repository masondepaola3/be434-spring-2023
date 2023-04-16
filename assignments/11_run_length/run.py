#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-04-15
Purpose: Run-length
"""

import argparse


# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='DNA text or file',
                        metavar='str',
                        type=str)

    args = parser.parse_args()
    try:
        with open(args.text, 'r') as file:
            contents = file.read().strip()
            setattr(args, 'text', contents)
    finally:
        return args

# --------------------------------------------------
def encode(string):
    encoded = ""
    
    prev = ''
    count = 1
    for char in string:
        if char == prev:
            count += 1
        else:
            encoded += prev 
            if count > 1:
                encoded += str(count)
            prev = char
            count = 1
    
    encoded += prev
    if count > 1:
        encoded += str(count)
    
    return encoded

def main():
    args = get_args()

    for seq in args.text.split():
        print(encode(seq))

# --------------------------------------------------
if __name__ == '__main__':
    main()
