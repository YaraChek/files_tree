import random

NAMES_NUMBER = 30
FILES_PATH = (r'/mnt/forwork/study/it/projects/something_for_gruzchik_3/files_tree/'
              r'first_work_directory/')
filenames = set()

with open('words.txt', 'r', encoding='utf-8') as inf:
    words = [line.strip() for line in inf]

while len(filenames) < NAMES_NUMBER:
    add_patch = random.choice(('patch', ''))
    words_number = random.randint(2, 6)
    separator = random.choice(('_', '-'))
    filename = separator.join(random.choices(words, k=words_number))

    if filename[-5:] != 'patch' and add_patch:
        filename = ''.join((filename, separator, add_patch))
    filename = ''.join((FILES_PATH, filename, '.yaml'))
    filenames.add(filename)

print(len(filenames))
print(filenames)

for filename in filenames:
    open(filename, 'x')
