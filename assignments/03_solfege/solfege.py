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

    parser.add_argument('key',
                        metavar='str',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Play Song"""


    args = get_args()
    key = args.key
    ref = { "Do" : "A deer, a female deer", 
            "Re" : "A drop of golden sun", 
            "Mi" : "A name I call myself", 
            "Fa" : "A long long way to run",
            "Sol" : "A needle pulling thread",
            "La" : "A note to follow sol",
            "Ti" : "A drink with jam and bread" }


    if key in ref:
        print(key + ", " + ref[key] )
    elif key:
        print(" I dont know " + " '" + key + "' ")

# --------------------------------------------------
if __name__ == '__main__':
    main()
