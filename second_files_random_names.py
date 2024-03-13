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
DIRNAME = 'second_work_directory'              # files will be created in this directory
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

def create_custom_file():
    """
    Create custom file with randomly generated files from "second_work_directory".
    """
    content = ""
    content += "apiVersion: apps/v1\n"
    content += "kind: Deployment\n"
    content += "metadata:\n"
    content += "  name: sl-demo-app\n\n\n"
    content += "resources:\n"
    content += "- ../../../base\n\n"
    content += "patcheskey:\n"

    # for i, (author, title) in enumerate(data.items()):
    # content += f"<td>{i + 1}</td>"
    # content += f"<td>{author}</td>"
    # content += f"<td>{title}</td>"
    content += "\n\nspec:\n"
    content += "  selector:\n"
    content += "    matchLabels:\n"
    content += "      app: sl-demo-app\n"
    content += "  template:\n"
    content += "    metadata:\n"
    content += "      labels:\n"
    content += "        app: sl-demo-app\n"
    content += "    spec:\n"
    content += "      containers:\n"
    content += "      - name: app\n"
    content += "        image: foo/bar:latest\n"
    content += "        ports:\n"
    content += "        - name: http\n"
    content += "          containerPort: 8080\n"
    content += "          protocol: TCP\n"

    final_output = content
    with open("custom/customization2.yaml", "w") as output:
        output.write(final_output)

def main():
    create_directory(PWD, DIRNAME)

    with open(WORDS, 'r', encoding='utf-8') as inf:
        words = [line.strip() for line in inf]

    create_files(create_filenames(NAMES_NUMBER, words))
    create_custom_file()


if __name__ == '__main__':
    main()
