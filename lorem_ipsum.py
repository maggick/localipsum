#!/bin/python3

import os
import random


def main():
    pass

# open all files contain in locations
locations = open('locations', 'r')
words = []
for location in locations:
    if os.path.exists(location.strip()):
        try:
            for filename in os.listdir(location.strip()):
                f = open(location.strip()+filename, 'r')
                for line in f:
                    words.append(line.strip())
        except FileNotFoundError:
            pass

# sort all the words ? (if not to slow)

# print random
print(words[random.randint(0, len(words)-1)])

if __name__ == "__main__":
    main()
