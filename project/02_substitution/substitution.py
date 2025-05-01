#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-05-01
Purpose: substitution cipher
"""

import argparse
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="substitution cipher",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file", metavar="FILE", type=argparse.FileType("rt"), help="Input file"
    )

    parser.add_argument(
        "-s", "--seed", metavar="SEED", type=int, default=3, help="A random seed"
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
    """Perform the substitution cipher"""

    args = get_args()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    random.seed(args.seed)
    cipher = "".join(random.sample(alpha, len(alpha)))

    if args.decode:
        mapping = {cipher[i]: alpha[i] for i in range(26)}
    else:
        mapping = {alpha[i]: cipher[i] for i in range(26)}

    out_f = args.outfile if args.outfile else sys.stdout

    for line in args.file:
        out = []
        for ch in line:
            up = ch.upper()
            if up in mapping:
                out.append(mapping[up])
            else:
                out.append(ch)
        out_f.write("".join(out))

    if args.outfile:
        args.outfile.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
