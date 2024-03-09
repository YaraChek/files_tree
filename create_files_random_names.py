import random
import os

NAMES_NUMBER = 30  # number of files to create
DIRNAME = 'first_work_directory'  # files will be created in this directory
PWD = os.getcwd()  # current directory
FILES_PATH = '/'.join((PWD, DIRNAME + r'/'))  # path to created files
WORDS = 'words.txt'  # file with words for file names


def create_directory(pwd, dirname):
    try:
        os.mkdir(os.path.join(pwd, dirname))
    except FileExistsError:
        print(f'Directory "{DIRNAME}" already exists')


def create_files(names):
    for name in names:
        open(name, 'x')


def create_filenames(names_number, word_lst):
    filenames = set()
    while len(filenames) < names_number:
        add_patch = random.choice(('patch', ''))
        words_number = random.randint(2, 6)
        separator = random.choice(('_', '-'))
        filename = separator.join(random.choices(word_lst, k=words_number))

        if filename[-5:] != 'patch' and add_patch:
            filename = ''.join((filename, separator, add_patch))
        filename = ''.join((FILES_PATH, filename, '.yaml'))
        filenames.add(filename)
    return filenames


create_directory(PWD, DIRNAME)

with open(WORDS, 'r', encoding='utf-8') as inf:
    words = [line.strip() for line in inf]

create_files(create_filenames(NAMES_NUMBER, words))
