#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-03-26
Purpose: Add Your Purpose
"""

from subprocess import getstatusoutput
import argparse
import sys
import string
import re 
import os

PRG = './common.py'
FOO = './inputs/foo.txt'
BAR = './inputs/bar.txt'
EXPECTED1 = ['bar', 'foo']
SAMPLE1 = './inputs/sample1.txt'
SAMPLE2 = './inputs/sample2.txt'
EXPECTED2 = ['AAATAAA', 'TTTTCCC']
BRITISH = './inputs/british.txt'
AMERICAN = './inputs/american.txt'
EXPECTED3 = [
    'I', 'We', 'a', 'about', 'and', 'as', 'beer,', 'faults,', 'forgot',
    'generally', 'good', 'had', 'have', 'improve', 'into', 'last', 'merits,',
    'my', 'night', 'of', 'our', 'ourselves.', 'put', 'set', 'such', 'that',
    'the', 'thoughts,', 'to', 'us', 'we', 'went', 'which', 'with', 'without'
]


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        help='Input file 2')
  
    parser.add_argument('-o FILE',
                        '--outfile',
                        help='Output file ',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default= None)

    return parser.parse_args()


# --------------------------------------------------
def read_words(file):
    """Read words from file"""

    if not os.path.isfile(file):
        print(f"common.py: error: argument FILE1: can't open '{file}': [Errno 2] No such file or directory: '{file}'", file=sys.stderr)
        sys.exit(1)

    with open(file, encoding='utf-8') as f:
        words = set(f.read().split())  # Keep words as they are
    return words

# --------------------------------------------------

def normalize_text(text):
    """Normalize text by converting to lowercase and removing punctuation"""
    text = re.sub(f'[{string.punctuation}]', '', text)  # Remove punctuation
    return text.split()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    #print(f"Reading words from {args.FILE1} and {args.FILE2}")
  
    words1 = read_words(args.FILE1)
    words2 = read_words(args.FILE2)

    common_words = sorted(words1 & words2)

    output_str = "\n".join(common_words) + "\n"
    #args.outfile.write(output_str)

    if args.outfile:
        with open(args.outfile, 'w', encoding='utf-8') as out_fh:
            out_fh.write(output_str)
    else:
        print(output_str, end="")
    # Print for stdout
    #if args.outfile == sys.stdout:
       # print(output_str)
   # else:
       # args.outfile.write(output_str + '\n') 
    
   # sys.exit(0)
# --------------------------------------------------
if __name__ == '__main__':
    main()
