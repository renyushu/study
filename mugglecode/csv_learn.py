import csv


csv_file = "/Users/yushufeng/Downloads/MeetingMsg.csv"

# with open(csv_file, 'r') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv) # 获取表头
#     print(headers)
#     for row in f_csv:
#         print(row) # 行
#         print(row[0])
#         print(row[2])
#         break

# 使用命名元祖获取

from collections import namedtuple
import re

# with open(csv_file, 'r') as f:
#     f_csv = csv.reader(f)
#     headings = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)] # 替换csv文件表头中不合法的cols name
#     Row = namedtuple('Row', headings)
#     for r in f_csv:
#         row = Row(*r)
#         print(row)
#         print(row.Duration__ms_) # 使用命名元祖，通过列名访问一行的某列的值，代替下标访问
#         break

# s_____d = 90 python 合法变量


# 将数据读取到一个字典序列中
with open(csv_file, 'r') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)
        # print(row['Start date'])
        break
        # OrderedDict([('Duration (ms)', '221834'), ('Start date', '2017-01-01 00:00:41'), ('End date', '2017-01-01 00:04:23'), ('Start station number', '31634'), ('Start station', '3rd & Tingey St SE'), ('End station number', '31208'), ('End station', 'M St & New Jersey Ave SE'), ('Bike number', 'W00869'), ('Member type', 'Member')])