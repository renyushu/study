# var = 99
#
#
# def local():
#     var = 0
#
#
# def glob1():
#     global var
#     var += 1
#
#
# def glob2():
#     var = 0
#     import Python3LearnNote.learncode.string_method.var
#     Python3LearnNote.learncode.string_method.var += 1
#
#
# def glob3():
#     var = 1
#     import sys
#     glob = sys.modules['Python3LearnNote.learncode.string_method']
#     glob.var += 1
#
#
# def test():
#     print(var)
#     local()
#     glob1()
#     glob2()
#     glob3()
#     print(var)


print(__name__)