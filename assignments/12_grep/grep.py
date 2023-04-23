#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-04-23
Purpose: grep
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        help='Search pattern',
                        metavar='PATTERN',
                        type=str,
                        #required=True,
                        #type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        #metavar='',
                        required=False,
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        required=False,
                        default=sys.stdout)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    pattern = args.pattern
    case = args.insensitive
    outfile = args.outfile
    files = args.files

    for file in files:
        for line in file:
            if len(files) > 1:
                output = file.name + ':' + line
            else:
                output = line

            if case:
                search = re.search(pattern, line, re.I)
                if search:
                    outfile.write(output)
            else:
                search = re.search(pattern, line)
                if search:
                    outfile.write(output)

# --------------------------------------------------
if __name__ == '__main__':
    main()
