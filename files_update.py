import os
import yaml

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
    print(sorted(new_list))
    return sorted(new_list)

def rename_strings_settings(list_new_names):
    # print("\n"+str(list_new_names))
    count = 0
    updated_list = list()
    not_updated_list = list()

    # Read the YAML file
    with open("custom/customization2.yaml", "r") as output:
        data = yaml.safe_load(output)
        print("\n outdated data: \n")
        print(data['patcheskey'])

        for itemdata in data['patcheskey']:

            for item in list_new_names:
                itemdata_file = os.path.split(itemdata)[1]
                correct_itemdata = make_corrections(itemdata_file,DIRNAME)
                fDestination = "{}/{}".format(DIRNAME, correct_itemdata)
                print("/n")
                print(item)
                print(itemdata)
                count=count+1
                if item == fDestination:
                    print("\n {} identical: ".format(count))
                    # print(item)
                    # print(fDestination)
                    # Rename the list
                    updated_list.append(fDestination)
                    break

                else:
                    print("\n {} not identical: ".format(count))
                    print(item)
                    print(fDestination)
                    not_updated_list.append(fDestination)

    final_list = not_updated_list + updated_list
    print(f"updated list: \n {final_list}")
    print(yaml.safe_dump(final_list))




    # # Identify the list to be renamed and sorted
    # list_to_rename = data['patcheskey']

    # # Rename the list
    # data['new_list'] = list_to_rename
    # data.pop('old_list')


if __name__ == '__main__':
    rename_action = rename_files(DIRNAME)
    rename_strings_settings(rename_action)
