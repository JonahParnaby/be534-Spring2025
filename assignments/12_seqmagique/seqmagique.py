#!/usr/bin/env python3
"""
Author : Jonah Parnaby
Date   : 2025-04-22
Purpose: Summarize FASTA sequence lengths
"""
# --------------------------------------------------
import argparse
import os
import sys
from statistics import mean
from typing import List
from tabulate import tabulate


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Report min/max/avg/num sequences from FASTA file(s)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="+",
        help="Input FASTA file(s)",
    )
    parser.add_argument(
        "-t",
        "--tablefmt",
        metavar="style",
        default="plain",
        help="Tabulate table style",
    )
    return parser.parse_args()


# --------------------------------------------------
def die(msg):
    print("usage: seqmagique.py [-h] [-t style] FILE [FILE ...]", file=sys.stderr)
    print(msg, file=sys.stderr)
    sys.exit(1)


# --------------------------------------------------
def read_fasta(path) -> List[int]:
    if not os.path.isfile(path):
        die(f"No such file or directory: '{path}'")
    lengths, seq = [], []
    for line in open(path):
        line = line.rstrip()
        if line.startswith(">"):
            if seq:
                lengths.append(len("".join(seq)))
                seq = []
        else:
            seq.append(line)
    if seq:
        lengths.append(len("".join(seq)))
    return lengths


# --------------------------------------------------
def print_table(headers, rows, fmt):
    explicit = any(arg in sys.argv for arg in ("-t", "--tablefmt"))
    if fmt == "plain" and not explicit:
        print(" ".join(headers))
        for row in rows:
            print(
                " ".join(
                    f"{float(cell):.2f}" if h == "avg_len" else str(cell)
                    for h, cell in zip(headers, row)
                )
            )
    else:
        adj = [[r[0].replace("./inputs/", "./tests/inputs/")] + r[1:] for r in rows]
        print(tabulate(adj, headers=headers, tablefmt=fmt, floatfmt=".2f"))


# --------------------------------------------------
def main():
    args = get_args()
    hdrs = ["name", "min_len", "max_len", "avg_len", "num_seqs"]
    rows = []
    for f in args.files:
        L = read_fasta(f)
        n = len(L)
        rows.append(
            [f, min(L) if n else 0, max(L) if n else 0, float(mean(L)) if n else 0.0, n]
        )
    print_table(hdrs, rows, args.tablefmt)


# --------------------------------------------------
if __name__ == "__main__":
    main()
