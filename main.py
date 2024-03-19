#!/usr/bin/env python3

"""
The script renames files in the specified directory.
Underscores are replaced with dashes. The word “patch” at the end of the name has been removed.
The script displays information about non-renamed *problematic* files to the terminal and writes
it to the log file.
Then it overwrites yaml-file: deletes renamed old filenames from the file list and adds new
filenames to the end of the file list.
"""

import os
import re
import yaml

settings_file = './presets/settings_rename_files.yaml'

with open(settings_file, encoding='utf-8') as presets:
    config = yaml.load(presets, Loader=yaml.FullLoader)

PATH_TO_RENAMING = config['path-to-renaming']      # path to files to be renamed
PATH_TO_CUSTOM = config['path-to-custom']          # path to the yaml file to update
CUSTOMIZATION_FILE = config['customization-file']  # name of the file to be updated
PATH_TO_LOG = config['path-to-log']                # path to log file
ERRLOGFILE = config['errlogfile']                  # name of log file for errors
LOGFILE = config['logfile']                        # old file names, new filenames, list of renames

BAD_DELIMITER = config['bad-delimiter']            # delimiter to be replaced
GOOD_DELIMITER = config['good-delimiter']          # delimiter for replacement
REMOVING_WORD = config['removing-word']          # the word at the end of the name has been removed
EXTENSION = config['extension']
EXAMPLE_KEY = config['example-key']   # keyword followed by a list of files that need to be updated


def create_new_filename(name: str, search: str, index: int) -> str:
    """
    Underscores are replaced with dashes. The word “patch” at the end of the name has been removed.
    :param name: filename
    :param search: the word to be removed
    :param index: the index from which the word to be removed begins
    :return: the new filename
    """
    if BAD_DELIMITER in name:
        name = name.replace(BAD_DELIMITER, GOOD_DELIMITER)
    if name[index:] == search:
        name = '.'.join((name[:index - 1], EXTENSION))
    return name


def renaming(old_filenames: list, search: str, index: int) -> dict:
    """
    Renames files according to conditions
    :param old_filenames: list of filenames to check
    :param search: the word to be removed
    :param index: the index from which the word to be removed begins
    :return: the renaming dictionary
    """
    was_renamed = dict()
    for filename in old_filenames:
        if BAD_DELIMITER in filename or filename[index:] == search:
            new_filename = create_new_filename(filename, search, index)
            if new_filename in old_filenames:
                message = (f'File "{filename}" is not renamed, because file "{new_filename}" '
                           f'is already in "{PATH_TO_RENAMING}"\n')
                print(message)
                with open(''.join((PATH_TO_LOG, ERRLOGFILE)), 'a', encoding='utf-8') as ouf:
                    print(message, file=ouf)
            else:
                full_filename = os.path.join(PATH_TO_RENAMING, filename)
                full_new_filename = os.path.join(PATH_TO_RENAMING, new_filename)
                was_renamed[full_filename] = full_new_filename
                os.rename(full_filename, full_new_filename)

    with open(''.join((PATH_TO_LOG, LOGFILE)), 'a', encoding='utf-8') as ouf:
        print('Files before renaming:', '', '\n'.join(old_filenames), '', sep='\n', file=ouf)
        print('Files after renaming:', '', '\n'.join(os.listdir(PATH_TO_RENAMING)),
              '', sep='\n', file=ouf)
        print('Was renamed:\n', file=ouf)
        for old, new in was_renamed.items():
            print(f'{old} ->\n-> {new}\n', file=ouf)

    return was_renamed


def division_into_three_parts(lst: list) -> tuple:
    """ Divides the list into three parts. The middle part is the one that needs to be changed.
    :returns: first - 1st part of input list
              third - 3rd part of input list
              spaces - the number of spaces after the `EXAMPLE_KEY` before the dash in the yaml file
    """
    start_index = 0
    end_index = 0

    for i in range(len(lst)):
        if lst[i].strip().startswith(f'{EXAMPLE_KEY}'):
            start_index = i + 1
            break

    first = lst[:start_index]
    second = lst[start_index:]

    num_iterations = len(second)

    # the keyword search to define the end of the list
    for i in range(num_iterations):
        if re.match(r'[a-zA-Z0-9 ]+ *:', second[i].strip()) or i == num_iterations:
            end_index = start_index + i
            break

    second = lst[start_index:end_index]

    third = list()

    # move all spaces from the end of the list to the beginning of the next block
    for i in range(len(second) - 1, -1, -1):
        if second[i].strip():
            break
        else:
            third.append(second.pop())

    third.extend(lst[end_index:])
    return first, second, third


def change_yaml(renamed: dict):
    """
    Overwrites yaml-file: renamed old filenames will be deleted from file list,
    new filenames will be added to the end of the file list
    """
    fullname = os.path.join(PATH_TO_CUSTOM, CUSTOMIZATION_FILE)
    fullname_backup = fullname + '.backup'

    os.rename(fullname, fullname_backup)

    with open(fullname_backup, encoding='utf-8') as inf:
        lines = [line.rstrip('\n') for line in inf]

    before, middle, after = division_into_three_parts(lines)

    not_renamed = [line for line in middle if line.strip("\'\" -") not in renamed]

    was_renamed = [line.replace(line.strip("\'\" -"), renamed[line.strip("\'\" -")])
                   for line in middle if line.strip("\'\" -") in renamed]

    middle = not_renamed + was_renamed

    text = '\n'.join(before + middle + after)
    with open(fullname, 'w', encoding='utf-8') as ouf:
        ouf.write(text)


def main():
    old_names = os.listdir(PATH_TO_RENAMING)
    to_search = '.'.join((REMOVING_WORD, EXTENSION))
    search_index = -len(to_search)
    change_yaml(renaming(old_names, to_search, search_index))


if __name__ == '__main__':
    main()
