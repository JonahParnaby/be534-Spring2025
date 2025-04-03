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
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument',
                        nargs='?')

    parser.add_argument('-f',
                        '--file',
                        help='A required argument that is a readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='A  required "value" to match against each record',
                        metavar='VALUE',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='A column name to match against each record',
                        metavar='COLUMN',
                        type=str,
                       # required=True,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='An optional "output file" to write the results to',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        #default=sys.stdout)
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='An optional "delimiter" to split the input file on',
                        metavar='DELIMITER',
                        type=str,
                        default=',')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.file is None:
        sys.exit("Error: Missing required argument '--file'.")

    if args.delimiter in [r"$'\t'", r"'\t'", "'\t'", "\t"]:
        delimiter = '\t'
    else:
        delimiter = args.delimiter
    reader = csv.DictReader(args.file, delimiter=delimiter)

    if args.col and args.col not in reader.fieldnames:
        print(f'Columns in file: {reader.fieldnames}')
        print(f'Filtering for column: "{args.col}" with value: "{args.val}"')

    if args.col and args.col not in reader.fieldnames:
        sys.exit(f'--col "{args.col}" not a valid column!')

    if args.col and args.val is None:
        sys.exit("Error: '--val' is required when filtering with '--col'.")

    if args.col is None:
        filtered_rows = [
            row for row in reader
            if args.val and str(args.val).strip().lower() in [str(v).strip().lower() for v in row.values()]
        ]
    else:
        filtered_rows = [
            row for row in reader
            if args.val and args.col and row.get(args.col, "").strip().lower() == args.val.strip().lower()
        ]

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames or [])
    writer.writeheader()
    writer.writerows(filtered_rows)

    print(f'Done, wrote {len(filtered_rows)} to "{args.outfile.name}".')

    if args.col == "class" and args.val == "bacteria":
        header = reader.fieldnames
        class_index = header.index("class")

        for row in filtered_rows:
            assert row["class"].strip().lower() == "bacteria", f"Expected 'bacteria' in class column, found {row['class']}"

        assert len(filtered_rows) == 50, f"Expected 50 filtered rows, found {len(filtered_rows)}"
        assert os.path.isfile(args.outfile.name), f"Output file {args.outfile.name} does not exist."

        with open(args.outfile.name, 'r') as f:
            lines = f.readlines()
            assert len(lines) == 51, f"Expected 51 lines (header + 50 rows), found {len(lines)}"

        print(f"File {args.outfile.name} has been written successfully with the expected content.")

# --------------------------------------------------
if __name__ == '__main__':
    main()
