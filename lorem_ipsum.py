#!/bin/python3

import os
import random


def main():
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

    str = "Lorem ipsum dolor sit amet, "

    # print random
    # str += printWords(words, 5)
    str += printParagraphs(words, 5)
    print(str)


def printWords(words, n):
    # if n > ? : let's add some comma
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
