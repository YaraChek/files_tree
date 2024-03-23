import os
import yaml
import re
# import ruamel.yaml

DIRNAME = r"./second_work_directory"

def make_corrections(filename,folder):
        # Rename file with a patterns in name, and replace underscore with a dush
        suffixName1 = filename.replace ("_", "-")
        suffixName2 = suffixName1.replace ("-patch.yaml", ".yaml")
        newName = suffixName2.replace (".patch.yaml", ".yaml")

        fDestination = "{}/{}".format(folder, newName)
        # print(newName)
        return newName


def rename_files(folder):
    counter = 0
    new_list = list()
    # Iterate
    for file in os.listdir(folder):
        # Rename file with a patterns in name, and replace underscore with a dush
        suffixName1 = file.replace ("_", "-")
        suffixName2 = suffixName1.replace ("-patch.yaml", ".yaml")
        newName = suffixName2.replace (".patch.yaml", ".yaml")
        counter=counter+1
        print("{}. old file: {}".format(counter, file))
        print("{}. new file: {}\n".format(counter, newName))

        # Rename the file
        fSource = "{}/{}".format(folder, file)
        # print(fSource)
        fDestination = "{}/{}".format(folder, newName)
        # print(fDestination)
        os.rename(fSource, fDestination)
        # print(file)
        new_list.append(fDestination)

    res = os.listdir(folder)
    # print(sorted(new_list))
    return sorted(new_list)

def split_text(lst):
    start_index = 0
    end_index = 0

    for i in range(len(lst)):

        if lst[i].strip().startswith(f'patcheskey'):
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

def rename_strings_settings(list_new_names):
    count = 0
    updated_list = list()
    not_updated_list = list()

    fullname = os.path.join("custom/customization2.yaml")
    fullname_backup = fullname + '.back'

    os.rename(fullname, fullname_backup)

    with open(fullname_backup, 'r') as listfile:
        lines = [line.rstrip('\n') for line in listfile]
        # print(lines)

    if len(lines) != 0:
        starttext, full_list, endtext = split_text(lines)
    else:
        print("lines value is empty, please fix")
        exit()

    # Read the YAML file
    with open(fullname_backup, "r") as output:
        data = yaml.safe_load(output)

        # full_list = data['patcheskey']

        for itemdata in full_list:

            itemdata_file = os.path.split(itemdata)[1]
            correct_itemdata = make_corrections(itemdata_file,DIRNAME)
            fDestination = "{}/{}".format(DIRNAME, correct_itemdata)
            count=count+1

            if fDestination in list_new_names:
                print("\n {} identical: ".format(count))
                print(fDestination)
                # Add to the list
                updated_list.append(f"- {fDestination}")

            else:
                print("\n {} not identical: ".format(count))
                print(fDestination)
                not_updated_list.append(itemdata)

    final_list = not_updated_list + updated_list
    print(f"updated list: \n {starttext} {final_list} {endtext}")
    newfile = '\n'.join(starttext + final_list + endtext)

    with open('custom/customization2.yaml', 'w', encoding='utf-8') as file:
        file.write(str(newfile))

    if os.path.isfile(fullname_backup):
        os.remove(fullname_backup)



if __name__ == '__main__':
    rename_action = rename_files(DIRNAME)
    rename_strings_settings(rename_action)
