#!/usr/bin/env python3

"""
Script creates test files by randomly combining a random number (up to six) of words from
“words.txt” and sometimes adds the words “patch” to the end of the name.
"""

import random
import os
import yaml

settings_create_files = './presets/settings_create_files.yaml'

with open(settings_create_files, encoding='utf-8') as presets:
    config = yaml.load(presets, Loader=yaml.FullLoader)

NAMES_NUMBER = config.get('names-number', 0)               # number of files to create
LABEL = config.get('label')                                # a label added randomly
INDEX_LABEL = -len(LABEL)                                  # index for search label
EXTENSION = config.get('extension')                        # extension of creating files
DIR_FOR_TEST_FILES = config.get('dirname-for-many-files')  # files will be created in this dir
DIR_FOR_YAML_FILE = config.get('dirname-for-yaml-files')   # yaml file will be created in this dir
YAML_FILE_NAME = config.get('yaml-files-name')             # test yaml file
EXAMPLE_KEY = config.get('example-key')                    # a line in a yaml file followed by a
                                                           # list of files for processing
PWD = config.get('pwd')                                    # path to DIR_FOR_TEST_FILES
CWD = config.get('cwd')                                    # path to DIR_FOR_YAML_FILE
TEST_FILES_PATH = os.path.join(PWD, DIR_FOR_TEST_FILES)    # path to created files
WORDS = config.get('words')                                # file with words for file names


def create_directory(pwd: str, dirname: str):
    """   Creating an empty directory at the specified path if it does not exist there.   """
    try:
        os.mkdir(os.path.join(pwd, dirname))
    except FileExistsError:
        print(f'Directory "{dirname}" already exists')


def create_files(names: list):
    """   Creating empty text files in specified directory   """
    for name in names:
        open(name, 'x')


def create_filenames(names_number: int, word_lst: list) -> list:
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
        filename = os.path.join(TEST_FILES_PATH, f'{filename}.{EXTENSION}')
        filenames.add(filename)
    return sorted(filenames)


def create_yaml_file():
    """   Creating yaml file with random filenames will be proceeded   """

    template_begin = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: sl-demo-app


resources:
- ../../../base

{EXAMPLE_KEY}:"""

    template_middle = '\n'.join((os.path.join(TEST_FILES_PATH, name)
                                 for name in os.listdir(TEST_FILES_PATH)))

    template_end = """
spec:
  selector:
    matchLabels:
      app: sl-demo-app
  template:
    metadata:
      labels:
        app: sl-demo-app
    spec:
      containers:
      - name: app
        image: foo/bar:latest
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
"""

    fullname = os.path.join(CWD, DIR_FOR_YAML_FILE, YAML_FILE_NAME + f'.{EXTENSION}')
    with open(fullname, 'w') as ouf:
        ouf.write('\n'.join((template_begin, template_middle, template_end)))


def main():
    create_directory(PWD, DIR_FOR_TEST_FILES)
    create_directory(CWD, DIR_FOR_YAML_FILE)

    with open(WORDS, 'r', encoding='utf-8') as inf:
        words = [line.strip() for line in inf]

    files_for_rename = create_filenames(NAMES_NUMBER, words)
    create_files(files_for_rename)
    create_yaml_file()


if __name__ == '__main__':
    main()
