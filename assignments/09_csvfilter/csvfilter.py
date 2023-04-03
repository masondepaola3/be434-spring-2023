#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-04-02
Purpose: csvfilter
"""

import csv
import argparse
import sys

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='{args.purpose}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    '''parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')'''
                        
    
    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='str',
                        type=str,
                        action='store',
                        required=False,
                        default = '')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=argparse.FileType('w'),
                        action='store',
                        required=False,
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='str',
                        type=str,
                        action='store',
                        required=False,
                        default=',')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file_arg = args.file
    val_arg = args.val
    col_arg = args.col
    out_arg = args.outfile
    delm_arg = args.delimiter
    
    reader = csv.DictReader(file_arg, delimiter=delm_arg)
    
    writer = csv.DictWriter(out_arg,fieldnames=reader.fieldnames)
    writer.writeheader()
    
    numRowsWritten = 0
    
    if not not col_arg:
        if col_arg not in reader.fieldnames:
            print('"' + col_arg + '" not a valid column!', file=sys.stderr)
            return -1
        for row in reader:
            for key,value in row.items():
                if key == col_arg and val_arg.lower() in value.lower():
                    writer.writerow(row)
                    numRowsWritten += 1
                    break
    else:
        for row in reader:
            values = row.values()
            for key,value in row.items():
                if val_arg.lower() in value.lower():
                    writer.writerow(row)
                    numRowsWritten += 1
                    break
    
    outFile = out_arg.name
    print('Done, wrote', numRowsWritten, 'to "' + str(outFile) + '".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
