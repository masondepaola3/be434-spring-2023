#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-02-07
Purpose: Solfege
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('keys',
                        # add nargs to say 1 or more
                        nargs='+',
                        metavar='str',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Play Song"""

    args = get_args()
    keys = args.keys
    ref = { 
        "Do" : "A deer, a female deer", 
        "Re" : "A drop of golden sun", 
        "Mi" : "A name I call myself", 
        "Fa" : "A long long way to run",
        "Sol" : "A needle pulling thread",
        "La" : "A note to follow sol",
        "Ti" : "A drink with jam and bread", 
    }

    # you forgot to loop through the notes from user input
    # this is a list not a string, I changed the variables above to "keys"
    # to show that the list is one or more items
    for key in keys:
        if key in ref:
            print(key + ", " + ref[key])
            # I usually use the get method to get the key
            #print(key + ", " + ref.get(key))
        else:
            # fixed this line for punctuation expected by the test
            print("I don't know" + ' "' + key + '"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
