import os
import sys


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        print(relpath, dirs, files)
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(full_path)
            print(os.path.normpath(os.path.abspath(full_path))) # normpath: 用来返回正常路径，可以解决双斜杠、对目录的多重引用的问题


if __name__ == '__main__':
    findfile(sys.argv[1], sys.argv[2])

"""
os.walk: 返回一个三元组，包括相对于查找目录的相对路径，一个该目录下的目录名列表，以及哪个目录下面的文件列表

. [] ['findfile.py']
././findfile.py
/Users/yushufeng/study/Python3LearnNote/cookbook/findfile.py


"""


# path = '...//.../findfile.py/findfile.py'
# print(os.path.normpath(path))


