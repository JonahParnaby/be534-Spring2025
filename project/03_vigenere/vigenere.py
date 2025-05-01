#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-05-01
Purpose: vigenere cipher
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="vigenere cipher",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file", metavar="FILE", type=argparse.FileType("rt"), help="Input file"
    )

    parser.add_argument(
        "-k",
        "--keyword",
        metavar="KEYWORD",
        type=str,
        default="CIPHER",
        help="A keyword (default: CIPHER)",
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
        help="Output file (default: std.out)",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Perform the Vigenere cipher"""

    args = get_args()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = args.keyword.upper()
    key_len = len(key)

    out_f = args.outfile if args.outfile else sys.stdout

    for line in args.file:
        key_index = 0
        result = []

        for ch in line:
            if ch.isalpha():
                up = ch.upper()
                pi = alpha.index(up)
                ki = alpha.index(key[key_index % key_len])

                if args.decode:
                    ci = (pi - ki) % 26
                else:
                    ci = (pi + ki) % 26

                result.append(alpha[ci])
                key_index += 1
            else:
                result.append(ch)

        out_f.write("".join(result))

    if args.outfile:
        args.outfile.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
