#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-04-09
Purpose: common
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('file1', 
                        help='Input file 1',
                        metavar='FILE1',
                        type=str,
                        #type=argparse.FileType('rt'),
                        default=None)
    
    parser.add_argument('file2', 
                        help='Input file 2',
                        metavar='FILE2',
                        type=str,
                        #type=argparse.FileType('rt'),
                        default=None)
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        required=False,
                        default=sys.stdout)
    
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    file1_arg = args.file1
    file2_arg = args.file2
    out_arg = args.outfile
    
    with open(file1_arg, 'r') as file1:
        words1 = set(file1.read().split())
    with open(file2_arg, 'r') as file2:
        words2 = set(file2.read().split())
    
    commonWords = sorted(list(words1 & words2))
    
    if out_arg != sys.stdin:
        #with open(out_arg, 'w') as outfile:
        for word in commonWords:
            out_arg.write(word + '\n')
    else:
        for word in commonWords:
            print(word)

# --------------------------------------------------
if __name__ == '__main__':
    main()
