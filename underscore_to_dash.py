#!/usr/bin/env python3

"""
The script renames files in the specified directory.
Underscores are replaced with dashes. The word “patch” at the end of the name has been removed.
"""

import os

PATH = r"${GITHUB_WORKSPACE}/first_work_directory/"
PATH_TO_LOG = r"${GITHUB_WORKSPACE}/"
# PATH = r'/mnt/forwork/study/it/projects/something_for_gruzchik_3/files_tree/first_work_directory/'
# PATH_TO_LOG = r'/mnt/forwork/study/it/projects/something_for_gruzchik_3/files_tree/'
LOGFILE = r'renaming_pass.log'
BAD_DELIMITER = '_'
GOOD_DELIMITER = '-'
REMOVING_WORD = 'patch'
EXTENSION = 'yaml'


def create_new_filename(name):
    if BAD_DELIMITER in name:
        name = name.replace(BAD_DELIMITER, GOOD_DELIMITER)
    if name[search_index:] == to_search:
        name = '.'.join((name[:search_index - 1], EXTENSION))
    return name


def main():
    for filename in old_filenames:
        if BAD_DELIMITER in filename or filename[search_index:] == to_search:
            new_filename = create_new_filename(filename)
            if new_filename in old_filenames:
                message = (f'file "{filename}" is not renamed, because file "{new_filename}" '
                           f'is already in "{PATH}"')
                print(message)
                with open(''.join((PATH_TO_LOG, LOGFILE)), 'a', encoding='utf-8') as ouf:
                    print(message, file=ouf)
                continue
            else:
                os.rename(os.path.join(PATH, filename), os.path.join(PATH, new_filename))


if __name__ == '__main__':
    old_filenames = os.listdir(PATH)
    to_search = '.'.join((REMOVING_WORD, EXTENSION))
    search_index = -len(to_search)
    main()
