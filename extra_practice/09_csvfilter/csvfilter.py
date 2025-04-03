#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@aizona.edu>
Date   : 2025-03-31
Purpose: Add Your Purpose
"""

import argparse
from typing import Optional
import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput
import sys
import csv


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Add Your Purpose",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "-f",
        "--file",
        help="A required argument that is a readable file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        required=True,
        default=None)

    parser.add_argument(
        "-v",
        "--val",
        help='A  required "value" to match against each record',
        metavar="VALUE",
        type=str,
        default=None)

    parser.add_argument(
        "-c",
        "--col",
        help="A column name to match against each record",
        metavar="COLUMN",
        type=str,
        default=None)

    parser.add_argument(
        "-o",
        "--outfile",
        help='An optional "output file" to write the results to',
        metavar="OUTFILE",
        type=argparse.FileType("wt"),
        # default=sys.stdout)
        default="out.csv")

    parser.add_argument(
        "-d",
        "--delimiter",
        help='An optional "delimiter" to split the input file on',
        metavar="DELIMITER",
        type=str,
        default=",")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    delimiter = (
        "\t" if args.delimiter in [r"$'\t'", r"'\t'", "'\t'", "\t"] else args.delimiter
    )
    reader = csv.DictReader(args.file, delimiter=delimiter)

    if args.col and args.col not in reader.fieldnames:
        print(f'Invalid column "{args.col}", available: {reader.fieldnames}')
        sys.exit(f'--col "{args.col}" not a valid column!')

    if args.col and args.val is None:
        sys.exit("Error: '--val' is required when filtering with '--col'.")

    filtered_rows = []
    for rec in reader:
        text = rec.get(args.col) if args.col else " ".join(rec.values())
        if re.search(args.val, text, re.IGNORECASE):
            filtered_rows.append(rec)

    csv.DictWriter(args.outfile, fieldnames=reader.fieldnames).writeheader()
    csv.DictWriter(args.outfile, fieldnames=reader.fieldnames).writerows(filtered_rows)

    print(f'Done, wrote {len(filtered_rows)} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
