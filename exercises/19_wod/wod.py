#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-03-31
Purpose: Create a WOD
"""

import argparse
import io
import csv 
import random
#from tabulate import tabulate
from pprint import pprint
from subprocess import getstatusoutput

prg = './wod.py'
input1 = 'inputs/exercises.csv'
input2 = 'inputs/silly-exercises.csv'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create a WOD',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--numm',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='Input File of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()
    
    if args.numm < 1:
        parser.error(f'--num "{args.numm}" must be greater than 0')
                    
    return args 
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
   
    wod = []
    for exercise, low, high in random.sample(exercises, k=args.numm):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps / 2)
        wod.append((exercise, reps))
   
    print(tabulate(wod, headers=('Exercise', 'Reps')))

# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""

    reader = csv.DictReader(fh, delimiter=',') 
    exercises = []
    for rec in reader:
        name, reps = rec['exercise'], rec['reps'] 
        low, high = map(int, reps.split('-'))
        exercises.append((name, low, high))
    return exercises
                    
# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""

    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]
    expected = """

# --------------------------------------------------
def test_seed1():

Exercise      Reps
----------  ------
Pushups         56
Situps          88
Crunches        27
Burpees         35
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput(f'{prg} {seed_flag} 1')
    assert rv == 0
    assert out.strip() == expected.strip()

# 
if __name__ == '__main__':
    main()
