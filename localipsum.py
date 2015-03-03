#!/usr/bin/env python3 

import os
import random
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='TODO')
    parser.add_argument('integer', type=int,
                   help='The number of [paragraphes|sentences|words] you want.')
    parser.add_argument('--paragraphs', action='store_true')
    parser.add_argument('--sentences', action='store_true')
    parser.add_argument('--words', action='store_true')
    parser.add_argument('--lorem', action='store_true')

    args = parser.parse_args()

    if not (args.paragraphs or args.sentences or args.words):
        print('One of the following argument is required:\n\
                --paragraphs\n\
                --sentences\n\
                --words ')
        sys.exit(0)

    n = args.integer
    if n < 1:
        print('We need a value > 0')
        sys.exit(0)

    # let's build a word list
    words = []

    # let's see if there is a locations file
    try:
        locations = open('locations', 'r')
    except FileNotFoundError:
        print("No location file found, you need one !")
        sys.exit(0)

    # open all files contain in locations
    for location in locations:
        if location[0] != '#':
            if os.path.exists(location.strip()):
                try:
                    for filename in os.listdir(location.strip()):
                        f = open(location.strip()+filename, 'r')
                        try:
                            for line in f:
                                words.append(line.strip())
                        except UnicodeDecodeError:
                            print('No reconize file: {}'.format(filename),
                                  file=sys.stderr)
                except FileNotFoundError:
                    pass

    # did we find a dictionary ?
    if len(words) == 0:
        print("No dictionary found, you may want to add one in the locations file")
        sys.exit(0)

    # TODO sort all the words ? (if not to slow)

    str = ""
    if args.lorem:
        # let's start with the well know Latin locution
        str = "Lorem ipsum dolor sit amet, "

    # print random
    if args.paragraphs:
        str += printParagraphs(words, n)
    if args.sentences:
        str += printSentences(words, n)
    if args.words:
        str += printWords(words, n)

    print(str)


def printWords(words, n):
    # TODO if n > ? : let's add some comma
    str = ""
    for i in range(0, n-1):
        str += words[random.randint(0, len(words)-1)]+" "
    return (str + words[random.randint(0, len(words)-1)])


def printSentences(words, n):
    str = ""
    for i in range(0, n-1):
        str += (printWords(words, random.randint(10, 25))+". ").capitalize()
    return str + (printWords(words, random.randint(10, 25))+".").capitalize()


def printParagraphs(words, n):
    str = ""
    for i in range(0, n-1):
        str += printSentences(words, random.randint(4, 8))+"\n\n"
    return str + printSentences(words, random.randint(4, 8))


if __name__ == "__main__":
    main()
