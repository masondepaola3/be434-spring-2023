#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-05-03
Purpose: substitution
"""

import argparse
import string
import random

# --------------------------------------------------
def get_args():
    '''Grabs arguments'''
    parser = argparse.ArgumentParser(prog = 'substitution.py',
                                     description='substitution cipher',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,)
    parser.add_argument('-s',
                        '--seed',
                        help='A random seed',
                        metavar='SEED',
                        type=int,
                        default=3)
    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action= 'store_true')
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='std.out')
    args = parser.parse_args()

    return args

def substitution_cipher(text, seed_val, decrypt):
    '''Encryption Function'''
    random.seed(seed_val)
    alphabet = list(string.ascii_uppercase)
    key = dict(zip(list(alphabet), random.sample(alphabet, 26)))
    result = ""
    if decrypt:
        key = {v: k for k, v in key.items()} # swap key and value in the dictionary

    for char in text:
        if char.isalpha():
            result += key.get(char.upper(), char)
        else:
            result += char
    return result


# --------------------------------------------------
def main():
    '''Main'''
    args = get_args()
    #print(args)
    input_file = args.FILE
    input_key = args.seed
    decode_bool = args.decode
    output_file = args.outfile

    with open(input_file.name, 'r', encoding="utf8") as input_text:
        text = input_text.read()
        input_text.close()

    cipher_text = substitution_cipher(text, input_key, decode_bool)
    with open(output_file.name, 'w', encoding="utf8") as output:
        output.write(cipher_text.upper())
        output.close()
    print(cipher_text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
