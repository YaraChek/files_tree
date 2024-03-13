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

settings_file = './presets/settings_rename_files.yaml'

with open(settings_file, encoding='utf-8') as presets:
    config = yaml.load(presets, Loader=yaml.FullLoader)

PATH_TO_RENAMING = config['path-to-renaming']      # path to files to be renamed
PATH_TO_LOG = config['path-to-log']                # path to log file
LOGFILE = config['logfile']                        # name of log file
PATH_TO_CUSTOM = config['path-to-custom']          # path to the yaml file to update
CUSTOMIZATION_FILE = config['customization-file']  # name of the file to be updated

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
                with open(''.join((PATH_TO_LOG, LOGFILE)), 'a', encoding='utf-8') as ouf:
                    print(message, file=ouf)
            else:
                full_filename = os.path.join(PATH_TO_RENAMING, filename)
                full_new_filename = os.path.join(PATH_TO_RENAMING, new_filename)
                was_renamed[full_filename] = full_new_filename
                os.rename(full_filename, full_new_filename)
    return was_renamed


def change_yaml(path_to_file: str, filename: str, patches_key: str, was_renamed: dict):
    """
    Overwrites yaml-file: renamed old filenames will be deleted from file list,
    new filenames will be added to the end of the file list
    """
    fullname = os.path.join(path_to_file, filename)
    with open(fullname, encoding='utf-8') as inf:
        depl = yaml.load(inf, Loader=yaml.FullLoader)
    patches = depl.get(patches_key)

    # delete old filenames from file list
    depl[patches_key] = [elem for elem in patches if elem not in was_renamed]

    # add new filenames to the end of the file list
    for name in was_renamed:
        depl[patches_key].append(was_renamed[name])

    with open(fullname, 'w', encoding='utf-8') as ouf:
        yaml.dump(depl, ouf)


def main():
    old_names = os.listdir(PATH_TO_RENAMING)
    to_search = '.'.join((REMOVING_WORD, EXTENSION))
    search_index = -len(to_search)
    change_yaml(PATH_TO_CUSTOM, CUSTOMIZATION_FILE,
                EXAMPLE_KEY, renaming(old_names, to_search, search_index))


if __name__ == '__main__':
    main()
