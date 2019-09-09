import os

"""
实现从shell命令行读取连接的Android设备，返回一个列表
"""

# print(os.popen('adb devices').readlines()) # ['List of devices attached\n', '8TFDU18802000479\tdevice\n', 'S2D7N18B05005633\tdevice\n', '\n']
# device_list = os.popen('adb devices').readlines()
# dev = []
# for d in device_list:
#     if '\tdevice' in d:
#         print(id(d))
#         d = d.replace('\n', ' ')
#         print(id(d))
#         d = d.split('\t')
#         print(d[0])
#         print(type(d))
#         dev.append(d[0])
# print(dev)


def device_list(cmd):
    """
    返回设备列表
    :param cmd:
    :return:
    """
    dev = []
    cmd_res = os.popen(cmd).readlines()
    for d in cmd_res:
        if '\tdevice' in d:
            d = d.replace('\n', '').split('\t')
            dev.append(d[0])
    return dev


res = device_list('adb devices')
print(res)