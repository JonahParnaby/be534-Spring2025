#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-03-18
Purpose: Create insults
"""

import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create insults',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    
    parser.add_argument('-n',
                        '--number',
                        help='The number of insults',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('-a',
                        '--adjectives',
                        help='The number of adjectives per insults',
                        metavar='int',  
                        type=int,
                        default=2)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)
                        
    args = parser.parse_args()

    if args.adjectives < 1:
       parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
                    
    adjectives  = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    for _ in range(args.number):
        adjs = ', '.join(random.sample(adjectives, k=args.adjectives))
        print(f'You {adjs} {random.choice(nouns)}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
