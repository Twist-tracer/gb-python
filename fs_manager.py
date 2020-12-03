import os


def create_dirs():
    for i in range(1, 9):
        os.mkdir('dir_{}'.format(i))


def remove_dirs():
    for i in range(1, 9):
        os.rmdir('dir_{}'.format(i))

# create_dirs()
# remove_dirs()
