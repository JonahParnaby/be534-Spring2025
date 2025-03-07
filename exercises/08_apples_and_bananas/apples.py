#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-03-05
Purpose: Apples and bananas 
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""


    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

args = get_args()
text = args.text
vowel = args.vowel

for v in 'aeiou':
    text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

print(text)
# --------------------------------------------------
if __name__ == '__main__':
    main()
