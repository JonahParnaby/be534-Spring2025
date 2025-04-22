#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-04-22
Purpose: Add Your Purpose
"""

import argparse
import os
import sys
from statistics import mean
from typing import List
from tabulate import tabulate

PRG = './seqmagique.py'
EMPTY = ('./inputs/empty.fa', './tests/inputs/empty.fa.out')
TEST1 = ('./inputs/1.fa', './tests/inputs/1.fa.out')
TEST2 = ('./inputs/2.fa', './tests/inputs/2.fa.out')
ALL = ('./inputs/*.fa', './tests/inputs/all.fa.out')


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                                            metavar='FILE',
                                            nargs='+',
                                            help='Input FASTA file(s)')

    parser.add_argument('-t',
                                            '--tablefmt',
                                            metavar='style',
                                            default='plain',
                                            help='Tabulate table style')

    return parser.parse_args()

# --------------------------------------------------
def die(msg: str) -> None:
    """Exit with an error message"""
    print('usage: seqmagique.py [-h] [-t style] FILE [FILE ...]', file=sys.stderr)
    print(msg, file=sys.stderr)
    sys.exit(1)

# --------------------------------------------------
def read_fasta(filename: str) -> List[int]:
    """Read FASTA file and return list of sequence lengths"""
    if not os.path.isfile(filename):
        die(f"No such file or directory: '{filename}'")

    seqs = []
    seq = ''
    with open(filename) as fh:
        for line in fh:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    seqs.append(len(seq))
                    seq = ''
            else:
                seq += line
        if seq:
            seqs.append(len(seq))
    return seqs

# --------------------------------------------------
def print_table(headers: List[str], rows: List[List[str]], fmt: str = 'plain') -> None:
    """Print table in various styles"""

    if fmt == 'plain':
        print(' '.join(headers))
        for row in rows:
            print(' '.join(str(cell) for cell in row))

    elif fmt == 'simple':
        col_widths = [max(len(str(cell)) for cell in col) for col in zip(headers, *rows)]
        def format_row(row):
            return ' | '.join(str(cell).ljust(w) for cell, w in zip(row, col_widths))

        sep = '-+-'.join('-' * w for w in col_widths)
        print(format_row(headers))
        print(sep)
        for row in rows:
            print(format_row(row))
    else:
        print(tabulate(rows, headers=headers, tablefmt=fmt))


# --------------------------------------------------
def main():
    """Main function to process FASTA files and print stats"""
    args = get_args()

    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    rows = []

    for file in args.files:
        lengths = read_fasta(file)
        num = len(lengths)
        min_len = min(lengths) if num else 0
        max_len = max(lengths) if num else 0
        avg_len = f'{mean(lengths):.2f}' if num else '0.00'
        rows.append([file, min_len, max_len, avg_len, num])
        
    print_table(headers, rows, args.tablefmt)



# --------------------------------------------------
if __name__ == '__main__':
    main()
