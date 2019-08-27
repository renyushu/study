# # import os
# #
# #
# # print(os.getcwd())
# # # ls = os.listdir(os.getcwd())
# # # print(ls)
# # #
# # # for l in ls:
# # #     times = os.path.getctime(l)
# # #     print(times)
# # #     print(type(times))
# #
# # # pa = os.path.realpath(__file__)     # 获取当前文件路径
# # # print(os.path.abspath(__file__))     # 获取当前文件路径
# # # p = os.path.split(pa)  # 分开目录与文件返回一个元祖
# # # print(p)
# #
# # # test_dir = '~/github/api_test_master/'
# # # print(os.listdir('../loop/'))
# #
# # print(os.path.abspath('../../'))
#
# import os
# from pathlib import Path
#
#
# p = Path()
# # # 返回家目录
# print(p.home())
# # # # 返回当前工作目录
# # print(p.cwd())
# # #
# # # # 默认当前目录
# # # print(p)
#
# # # 将path路径实例化对象
# # p1 = Path('/Python3LearnNote/os_module_learn')
# # p2 = Path('demo')
# # # print(str(p1))
# # print(p1 / p2)
#
#
# # def get_home_path():
# #     p = Path()
# #     work = p.cwd()
# #     return work
import os

p = os.path.relpath('os_test.py')

print(p)