#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-04-09
Purpose: Add Your Purpose
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Add Your Purpose",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("File", metavar="FILE", help="Input file")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if not os.path.isfile(args.File):
        sys.exit(f"No such file or directory: '{args.File}'")

    with open(args.File) as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        print(line)

    conserved = []
    for chars in zip(*lines):
        if all(char == chars[0] for char in chars):
            conserved.append("|")
        else:
            conserved.append("X")

    print("".join(conserved))


# --------------------------------------------------
if __name__ == "__main__":
    main()
