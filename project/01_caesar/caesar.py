#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-05-03
Purpose: caesar shift
"""

import argparse


# --------------------------------------------------
def get_args():
    '''Grabs arguments'''
    parser = argparse.ArgumentParser(prog = 'caesar.py',
                                     description='caesar cipher',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,)
    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)
    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='std.out')
    args = parser.parse_args()

    return args


def caesar_cipher(text, shift, decrypt):
    '''doc string'''
    result = ""
    # If encrypt is True, shift the characters to encrypt the text
    # If encrypt is False, shift the characters in the opposite direction to decrypt the text
    if decrypt:
        direction = -1
    else:
        direction = 1
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift*direction - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift*direction - 97) % 26 + 97)
        else:
            result += char
    return result

# --------------------------------------------------

def main():
    '''Main'''
    args = get_args()
    #print(args)
    input_file = args.FILE
    input_shift = args.number
    decode_bool = args.decode
    output_file = args.outfile

    with open(input_file.name, 'r', encoding="utf8") as input_text:
        text = input_text.read()
        input_text.close()

    cipher_text = caesar_cipher(text, input_shift, decode_bool).upper()
    with open(output_file.name, 'w', encoding="utf8") as output:
        output.write(cipher_text)
        output.close()
    print(cipher_text)

# --------------------------------------------------

if __name__ == '__main__':
    main()
