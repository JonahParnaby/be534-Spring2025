#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-02-19
Purpose: Print the reverse complement of DNA
"""

import argparse
import os
import io
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='Input sequence or file')

    parser.add_argument('-o',
                        '--out',
                        help='Output filename',
                        metavar='str',
                        type=str)
                        #default='')

    args = parser.parse_args()

    if os.path.isfile(args.DNA):
        args.DNA = open(args.DNA).read().strip()

    return args


# --------------------------------------------------
def reverse_complement(DNA):

    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}

    return ''.join(complement.get(base, base) for base in reversed(DNA))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    revc = reverse_complement(args.DNA)

    print(revc)

    if args.out:
        open(args.out, 'wt').write(revc + '\n')
 

# --------------------------------------------------
if __name__ == '__main__':
    main()
