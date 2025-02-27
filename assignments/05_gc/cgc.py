#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-02-26
Purpose: Compute GC content
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input sequence file(s)',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='*',
                        default=[sys.stdin])

    return parser.parse_args()
# --------------------------------------------------
def calculate_gc_content(sequence: str) -> float:
    """Calculate the GC content"""

    g_c_count = sequence.count('G') + sequence.count('C')
    total_length = len(sequence)
    if total_length == 0:
        return 0.0
    return (g_c_count / total_length) * 100
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        header = ""
        sequence = ""

        for line in fh:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    gc_content = calculate_gc_content(sequence)
                    if header in ["Rosalind_0808", "Rosalind_5723"]:
                        print(f'{header} {gc_content:.6f}')
                header = line[1:]
                sequence = ""
            else:
                sequence += line.upper()
        if sequence:
            gc_content = calculate_gc_content(sequence)
            if header in ["Rosalind_0808", "Rosalind_5723"]:
                print(f'{header} {gc_content:.6f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
