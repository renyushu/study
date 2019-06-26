# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mp
import os


"""
csv: 储存数据

  
"""

data_path = "/Users/yushufeng/Downloads/data/bikeshare/"
files = os.listdir(data_path)

# for f in files:
#     print(f)


def collect_data():
    """
        数据收集
    :return:
    """
    data_arr_list = []
    for f in files:
        file_path = data_path + f
        # print(file_path)
        data_arry = np.loadtxt(file_path, delimiter=',', dtype='str', skiprows=1)
        # print(data_arry)
        # for d in data_arry:
        #     print(d)
        # break
        data_arr_list.append(data_arry)
    return data_arr_list


def process_data(date_arr_list):
    """
        数据处理
    :param date_arr_list:
    :return:
    """
    duration_min_list = []
    for data in date_arr_list:
        duration_str_col = data[:, 0]  # list[:] 表示整个列表的切片, 选中第0列 == duration col
        # 去掉双引号
        # 向量化操作，然后在考虑for循环
        duration_in_ms = np.core.defchararray.replace(duration_str_col, '"', '')  # 向量化操作 duration col，把" 替换为 ' '
        #类型转换
        duration_in_min = duration_in_ms.astype('float') / 1000 / 60 # 多维数组可以使用向量化操作
        duration_min_list.append(duration_in_min)
    return duration_min_list


def analyze_data(duration_min_list):
    """
        数据分析
    :return:
    """
    duration_mean_list = []
    for i, duration in enumerate(duration_min_list):
        duration_meadn = np.mean(duration)
        print('第{}季度的平均骑行时间：{:.2f}分钟'.format(i+1, duration_meadn)) # .2f: 表示小数点后两位
        duration_mean_list.append(duration_meadn)
    return duration_mean_list


def show_results(duration_mean_list):
    mp.figure() #
    mp.bar(range(len(duration_mean_list)), duration_mean_list) # 柱状图的个数和数值
    mp.show() # 结果展示


def main():
    # 数据获取
    data_arr_list = collect_data()
    # print(data_arr_list)

    # 分析数据
    duration_min_list = process_data(data_arr_list)

    duration_mean_list = analyze_data(duration_min_list)

    show_results(duration_mean_list)


if __name__ == "__main__":
    main()