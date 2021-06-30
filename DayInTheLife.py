import numpy as np
import scipy as sp
import random
from scipy import constants as cst
import argparse #For future options


parser = argparse.ArgumentParser(description='Necessary Arguments')
parser.add_argument('character',\
 help="The integer number of muons to generate in csv", type=str,\
 action='store', default='Robyn')
args = parser.parse_args()

print(f'Hello! Today you will be experiencing a day in the life of {args.character}\n')
time.sleep(5)
print('As your day proceeds, you will be prompted to make choices.')
time.sleep(5)
print('to make a choice, input the number corresponding to the choice you would like to make')

print('Uh oh, looks like a wild Robyn has appeared out of nowhere! what will you do?!\n')
a1 = input('What you will do to the wild Robyn\n1 = Hug \n2 = Insult\n3 = Call Over\n4 = Compliment\n\n')
if a1 == 1
  print(f'\nYou walked up to the wild Avery and gave her a big hug...')
  time.sleep(2)
  input('hit enter to continue')