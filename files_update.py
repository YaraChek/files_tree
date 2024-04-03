#!/usr/bin/env python3
"""
This file work with files location and listing of the file. With this script its possible
to update the names of the files in folder and also compare and update names in config
"""

import os
import re
import yaml
# import ruamel.yaml

DIRNAME = r"./second_work_directory"
SORTINGNAME = "patcheskey"
CONFIGFILE = "custom/customization2.yaml"

def make_corrections(filename):
    """
    Make correction to filenames with a patterns in name, and replace underscore with a dush
    """

    suffix_name1 = filename.replace ("_", "-")
    suffix_name2 = suffix_name1.replace ("-patch.yaml", ".yaml")
    new_name = suffix_name2.replace (".patch.yaml", ".yaml")

    # print(f"renamed file: - {new_name}")
    return new_name


def rename_files(folder):
    """
    Rename files in subfolder DIRNAME with a patterns in make_corrections
    """

    counter = 0
    new_list = []
    # Iterate
    for file in os.listdir(folder):

        correct_filename = make_corrections(file)

        counter=counter+1
        print(f"{counter}. old file: {file}")
        print(f"{counter}. new file: {correct_filename}\n")

        # Rename the file
        file_source = "{}/{}".format(folder, file)
        # print(file_source)
        file_destination = "{}/{}".format(folder, correct_filename)
        # print(fDestination)
        os.rename(file_source, file_destination)

        # print(file)
        new_list.append(os.path.basename(file_destination).split('/')[-1])

    # res = os.listdir(folder)
    print("new list: \n")
    print(new_list)
    return sorted(new_list)

def split_text(lst):
    """
    Split text for a three parts, for achieve ability to modify a second one
    """
    start_index = 0
    end_index = 0

    for i in range(len(lst)):

        if lst[i].strip().startswith(f'{SORTINGNAME}'):
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

    third = []

    # move all spaces from the end of the list to the beginning of the next block
    for i in range(len(second) - 1, -1, -1):
        if second[i].strip():
            break
        else:
            third.append(second.pop())

    third.extend(lst[end_index:])
    return first, second, third

def rename_strings_settings(list_new_names):
    """
    Update list with a files regarding to updated names and subfolders
    """
    count = 0
    updated_list = []
    not_updated_list = []

    fullname = os.path.join(CONFIGFILE)
    fullname_backup = fullname + '.back'

    os.rename(fullname, fullname_backup)

    with open(fullname_backup, 'r', encoding='utf-8') as listfile:
        lines = [line.rstrip('\n') for line in listfile]
        # print(lines)

    if len(lines) != 0:
        starttext, full_list, endtext = split_text(lines)
    else:
        print("lines value is empty, please fix")
        exit()

    # Read the YAML file
    with open(fullname_backup, "r", encoding='utf-8') as output:
        data = yaml.safe_load(output)

        # full_list = data["{SORTINGNAME}"]
        print(f"print_full_list: \n {full_list}")

        print(f"print_list_names: \n {list_new_names}")

        for itemdata in full_list:

            correct_itemdata = make_corrections(itemdata)
            fDestination = correct_itemdata
            count=count+1

            if fDestination.strip("\'\" -/.") in list_new_names:
                print(f"\n {count} identical: ")
                print(fDestination)
                # Add to the list
                filepatch = DIRNAME.rsplit('/', 1)[1]
                print(f" filepatch: {filepatch}")
                fixedline = fDestination.replace(fDestination.strip("\'\" -/."), filepatch+"/"+fDestination.strip("\'\" -/."))
                updated_list.append(fixedline)
            else:
                print(f"\n {count} not identical: ")
                print(fDestination)
                not_updated_list.append(itemdata)

    # sorting updated list
    updated_list.sort()

    final_list = not_updated_list + updated_list
    # print(f"updated list: \n {final_list}")
    newfile = '\n'.join(starttext + final_list + endtext)

    with open(CONFIGFILE, 'w', encoding='utf-8') as file:
        file.write(str(newfile))

    if os.path.isfile(fullname_backup):
        os.remove(fullname_backup)


if __name__ == '__main__':
    rename_action = rename_files(DIRNAME)
    rename_strings_settings(rename_action)
