#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-04-14
Purpose: Add Your Purpose
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Add Your Purpose",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,)

    parser.add_argument("positional", metavar="str", help="DNA text or file")

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Return run-length encoded sequence"""

    if not seq:
        return ""

    result = []
    prev = seq[0]
    count = 1

    for char in seq[1:]:
        if char == prev:
            count += 1
        else:
            result.append(prev + (str(count) if count > 1 else ""))
            prev = char
            count = 1

    result.append(prev + (str(count) if count > 1 else ""))
    return "".join(result)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    args = args.positional

    if os.path.isfile(args):
        with open(args) as file:
            for line in file:
                print(rle(line.strip()))
    else:
        print(rle(args))


# --------------------------------------------------
if __name__ == "__main__":
    main()
