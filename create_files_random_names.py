#!/usr/bin/env python3

"""
Script creates test files by randomly combining a random number (up to six) of words from
“words.txt” and sometimes adds the words “patch” to the end of the name.
"""

import random
import os

NAMES_NUMBER = 30                             # number of files to create
LABEL = 'patch'                               # a label added randomly
INDEX_LABEL = -len(LABEL)                     # index for search label
EXTENSION = 'yaml'                            # extension of creating files
DIRNAME = 'first_work_directory'              # files will be created in this directory
PWD = os.getcwd()                             # current directory
FILES_PATH = '/'.join((PWD, DIRNAME + r'/'))  # path to created files
WORDS = 'words.txt'                           # file with words for file names


def create_directory(pwd, dirname):
    """   Creating an empty directory at the specified path if it does not exist there.   """
    try:
        os.mkdir(os.path.join(pwd, dirname))
    except FileExistsError:
        print(f'Directory "{DIRNAME}" already exists')


def create_files(names):
    """   Creating empty text files in specified directory   """
    for name in names:
        open(name, 'x')


def create_filenames(names_number, word_lst):
    """
    Create filenames by randomly combining a random number (up to six) of words from
    “words.txt” sometimes adding the words “patch” to the end of the name.
    """
    filenames = set()
    while len(filenames) < names_number:
        add_patch = random.choice((LABEL, ''))
        words_number = random.randint(2, 6)
        separator = random.choice(('_', '-'))
        filename = separator.join(random.choices(word_lst, k=words_number))

        if filename[INDEX_LABEL:] != LABEL and add_patch:
            filename = ''.join((filename, separator, add_patch))
        filename = ''.join((FILES_PATH, filename, f'.{EXTENSION}'))
        filenames.add(filename)
    return filenames


def main():
    create_directory(PWD, DIRNAME)

    with open(WORDS, 'r', encoding='utf-8') as inf:
        words = [line.strip() for line in inf]

    create_files(create_filenames(NAMES_NUMBER, words))


if __name__ == '__main__':
    main()
