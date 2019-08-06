import os
import yaml


file_path = os.path.abspath('./test.yaml')
# print(file_path)

# f = open(file_path)
# y = yaml.load(f, Loader=yaml.FullLoader) # 读取文件
# print(y)

py_obj = {
    'key': 'value',
    'islist': [1, 3, 4],
    'int': 5,
    'boolean': True,
    'float': 12.33,
    'null': None,
    'time': '',
    'date': '',
    'dic': {'name': 'n', 'age': 'n', 'sex': 'n'},
    'listofdic': {},
    'dicoflist': [{'hell': 'n'}, {'n': 'jack', 'age': '89'}, {'key23': 'v23'}]
}

print(yaml.dump(py_obj, ))

"""
基本规则：
    1，大小写敏感
    2，使用缩进表示层级关系
    3，缩进时不允许使用tab键，只允许使用空格
    4，缩进的空格数目不重要，只要相同层级的元素左侧对其即可
    
支持的数据结构：
    1，对象，键值对
    2，数组
    3，纯量
        最基本的，不可再分的值
            字符串/布尔值/整数/浮点数/Null/时间/日期
            
"""