import os

DIRNAME = r"./second_work_directory/"

def rename_files(folder):
    counter = 0
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

    res = os.listdir(folder)
    print(res)

if __name__ == '__main__':
    rename_files(DIRNAME)