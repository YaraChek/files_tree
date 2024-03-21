#!/usr/bin/env python3

"""
Script creates test files by randomly combining a random number (up to six) of words from
“words.txt” and sometimes adds the words “patch” to the end of the name.
"""

import random
import os
# import ruamel.yaml
import yaml

NAMES_NUMBER = 30                             # number of files to create
LABEL = 'patch'                               # a label added randomly
INDEX_LABEL = -len(LABEL)                     # index for search label
EXTENSION = 'yaml'                            # extension of creating files
DIRNAME = 'second_work_directory'              # files will be created in this directory
SETTINGSNAME = 'custom'                       # folder for settings file
PWD = os.getcwd()                             # current directory
FILES_PATH = "./" + DIRNAME + "/"  # path to created files

WORDS = 'words.txt'                           # file with words for file names


def create_directory(pwd, dirname):
    """   Creating an empty directory at the specified path if it does not exist there.   """
    try:
        os.mkdir(os.path.join(pwd, dirname))
    except FileExistsError:
        print(f'Directory "{dirname}" already exists')


def create_files(names):
    """   Creating empty text files in specified directory   """
    for name in names:
        open(os.path.join(FILES_PATH, name), 'x')


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
        filen = f'./{filename}.{EXTENSION}'
        filename = os.path.join(FILES_PATH, f'{filename}.{EXTENSION}')
        filenames.add(filen)

    return sorted(filenames)

def create_custom_file(filenames: list):
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
    content += "- ./test_123_path.yaml\n"

    content += yaml.safe_dump(filenames)

    content += "- ./test-123-path.yaml\n"
    content += "- ./test-321.yaml\n"
    content += "\nspec:\n"
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

    # code = ruamel.yaml.YAML()
    # # yaml.indent(mapping=2, sequence=4, offset=2)
    # # data = yaml.load("custom/customization2.yaml")
    # # yaml.dump(filenames, output)

    # code = ruamel.yaml.load(content, Loader=ruamel.yaml.RoundTripLoader)
    # code["patcheskey"] = 'Astarte'  # Oh no you didn't.

    # print(ruamel.yaml.dump(code, Dumper=ruamel.yaml.RoundTripDumper), end='')

def main():
    create_directory(PWD, DIRNAME)
    create_directory(PWD, SETTINGSNAME)

    with open(WORDS, 'r', encoding='utf-8') as inf:
        words = [line.strip() for line in inf]

    list_files = create_filenames(NAMES_NUMBER, words)
    create_files(list_files)

    create_custom_file(list_files)


if __name__ == '__main__':
    main()
