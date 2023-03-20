#!/usr/bin/env python3
"""
Author : masondepaola <masondepaola@localhost>
Date   : 2023-03-19
Purpose: syndna
"""

import argparse
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default='out.fa')
    parser.add_argument('-t',
                        '--seqtype',
                        metavar='str',
                        help='DNA or RNA',
                        type=str,
                        choices=['rna', 'dna'],
                        default='dna')
    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)
    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)
    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)
    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    arguments = parser.parse_args()
    if not 0 < arguments.pctgc < 1:
        parser.error(f'--pctgc "{arguments.pctgc}" must be between 0 and 1')

    return parser.parse_args()

def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)
    return ''.join(sorted(pool))

# --------------------------------------------------
def main():
    """Proteins"""
    
    args = get_args()
    output_file = args.outfile
    seq_type = args.seqtype
    num_seq = args.numseqs
    min_len = args.minlen
    max_len = args.maxlen
    percent = args.pctgc
    seed = args.seed
    random.seed(seed)
    
    pool = create_pool(percent, max_len, seq_type)

    with open(output_file.name, 'w', encoding="utf8") as output:
        for i in range(num_seq):
            seq_len = random.randint(min_len, max_len)
            seq = random.sample(pool, seq_len)
            output.write(f">{i+1}\n{''.join(seq)}\n")
    output.close()
    print(f'Done, wrote {num_seq} {seq_type.upper()} sequences to \"{output_file.name}\".')

# --------------------------------------------------

if __name__ == '__main__':
    main()