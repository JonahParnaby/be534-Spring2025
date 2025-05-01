#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-05-01
Purpose: Caesar‐shift encode/decode a file
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="caesar shift",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file", metavar="FILE", type=argparse.FileType("rt"), help="Input file"
    )

    parser.add_argument(
        "-n",
        "--number",
        metavar="NUMBER",
        type=int,
        default=3,
        help="A number to shift",
    )

    parser.add_argument(
        "-d", "--decode", action="store_true", help="Decode instead of encode"
    )

    parser.add_argument(
        "-o",
        "--outfile",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=None,
        help="Output file (default: stdout)",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = args.number % 26
    if args.decode:
        shift = -shift

    out_f = args.outfile if args.outfile else sys.stdout

    for line in args.file:
        result = []
        for ch in line:
            up = ch.upper()
            if up in alpha:
                idx = alpha.index(up)
                new = alpha[(idx + shift) % 26]
                result.append(new)
            else:
                result.append(ch)
        out_f.write("".join(result))

    if args.outfile:
        args.outfile.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
