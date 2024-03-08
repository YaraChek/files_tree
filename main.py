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
import yaml

PATH_TO_RENAMING = r'./first_work_directory/'
PATH_TO_LOG = r'./'
PATH_TO_CUSTOM = r'./customiz/'
CUSTOMIZATION_FILE = 'customization.yaml'
LOGFILE = r'renaming_pass.log'

BAD_DELIMITER = '_'
GOOD_DELIMITER = '-'
REMOVING_WORD = 'patch'
EXTENSION = 'yaml'


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
                with open(''.join((PATH_TO_LOG, LOGFILE)), 'a', encoding='utf-8') as ouf:
                    print(message, file=ouf)
            else:
                full_filename = os.path.join(PATH_TO_RENAMING, filename)
                full_new_filename = os.path.join(PATH_TO_RENAMING, new_filename)
                was_renamed[full_filename] = full_new_filename
                os.rename(full_filename, full_new_filename)
    return was_renamed


def change_yaml(path_to_file: str, filename: str, patches_key, was_renamed: dict):
    """
    Overwrites yaml-file: renamed old filenames will be deleted from file list,
    new filenames will be added to the end of the file list
    """
    fullname = os.path.join(path_to_file, filename)
    with open(fullname, encoding='utf-8') as inf:
        config = yaml.load(inf, Loader=yaml.FullLoader)
    patches = config.get(patches_key)

    # delete old filenames from file list
    config[patches_key] = [elem for elem in patches if elem not in was_renamed]

    # add new filenames to the end of the file list
    for name in was_renamed:
        config[patches_key].append(was_renamed[name])

    with open(fullname, 'w', encoding='utf-8') as ouf:
        yaml.dump(config, ouf)


def main():
    with open('example_key', encoding='utf-8') as inf:
        patches_key = inf.read().strip()
    old_names = os.listdir(PATH_TO_RENAMING)
    to_search = '.'.join((REMOVING_WORD, EXTENSION))
    search_index = -len(to_search)
    change_yaml(PATH_TO_CUSTOM, CUSTOMIZATION_FILE,
                patches_key, renaming(old_names, to_search, search_index))


if __name__ == '__main__':
    main()
