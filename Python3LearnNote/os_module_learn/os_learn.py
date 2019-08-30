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
# import os
#
# p = os.path.relpath('os_test.py')
#
# print(p)


# import time
# N = 1000
# for i in range(N):
#     print("进度:{0}%".format(round((i + 1) * 100 / N)), end="\r")
#     time.sleep(0.01)


# import time
# N = 1000
# st = time.clock()
# for i in range(N):
#     p = round((i + 1) * 100 / N)
#     duration = round(time.clock() - st, 2)
#     remaining = round(duration * 100 / (0.01 + p) - duration, 2)
#     print("进度:{0}%，已耗时:{1}s，预计剩余时间:{2}s".format(p, duration, remaining), end="\r")
#     time.sleep(0.01)

# import time
# import progressbar
# p = progressbar.ProgressBar()
# N = 1000
# for i in p(range(N)):
#     time.sleep(0.01)


# import time
# import progressbar
# # p = progressbar.ProgressBar()
# # N = time.sleep(3)
# # p.start(N)
# # for i in range(N):
# #     time.sleep(0.01)
# #     p.update(i+1)
# # p.finish()
#
# for i in progressbar.progressbar(range(5)):
#     time.sleep(1)

