#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-02-26
Purpose: proteins
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument ('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)
    

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')
    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Proteins"""

    args = get_args()
    seq = args.positional
    codons_file = args.codons
    output_file = args.outfile
    table = {}
    for line in codons_file:
        (key, val) = line.rstrip().split()
        table[str(key)] = val
        
    protein = ""
    
    try:
        k = 3
        for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
            protein+= table[codon.upper()]
    except KeyError as key:
        protein+= "-"
        
    with open(output_file.name, 'w', encoding="utf8") as output:
        output.write(protein)
        output.close()
    print(f'Output written to \"{output_file.name}\".')


# --------------------------------------------------
if __name__ == '__main__':
    main()

