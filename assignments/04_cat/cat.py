#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-02-18
Purpose: cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get  arguments"""

    parser = argparse.ArgumentParser(prog='cat.py',
        description='conCATenate files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None ,
                        nargs='+')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',)
    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Main"""

    args = get_args()
    files = args.FILE
    number_flag = args.number

    for file in files:
        for index, line in enumerate(file):
            if number_flag is True:
                print(f'     {index+1}\t{line}'.rstrip('\n'))
            else:
                print(line.rstrip('\n'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
