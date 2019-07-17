import os


print(os.getcwd())
# ls = os.listdir(os.getcwd())
# print(ls)
#
# for l in ls:
#     times = os.path.getctime(l)
#     print(times)
#     print(type(times))

# pa = os.path.realpath(__file__)     # 获取当前文件路径
# print(os.path.abspath(__file__))     # 获取当前文件路径
# p = os.path.split(pa)  # 分开目录与文件返回一个元祖
# print(p)

# test_dir = '~/github/api_test_master/'
# print(os.listdir('../loop/'))

print(os.path.abspath('../../'))