# -*- coding: utf-8 -*-
import numpy
import os
import matplotlib.pyplot as mp

"""
    将摄氏温度批量转换为华氏温度

"""

csv_path = "/Users/yushufeng/Downloads/temp.csv"


def collect_data(csv_path):
    """
        读取数据
    :param csv_path:
    :return:
    """
    csv_data = numpy.loadtxt(csv_path, delimiter=',', skiprows=1, dtype='str')
    return csv_data


def process_data(csv_data):
    """
        数据处理
    :param csv_data:
    :return:
    """
    temperature_col_value = csv_data[:, 1]
    # 替换特殊字符
    temperature_str = numpy.core.defchararray.replace(temperature_col_value, "C", '')
    # 数据计算
    temperature_c_to_f = temperature_str.astype('float') * 1.8 + 32
    return temperature_c_to_f


def main():
    csv_data = collect_data(csv_path)

    temperature_c_to_f = process_data(csv_data)
    print(temperature_c_to_f)


if __name__ == "__main__":
    main()