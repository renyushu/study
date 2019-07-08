from wxpy import *
import csv
import time


csv_path = '/Users/yushufeng/Downloads/MeetingMsg.csv'
FRIENDS = ['李总', '麻瓜编程', '沫沫']


def get_csv(path):
    with open(path, 'r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            pass
            # print(row)
            # print(row['微信昵称'])
            # print(row['时间'])

        return [info for info in f_csv]


# get_csv(csv_path)


def get_message(infos, name):
    template = "{name}, 提醒下, {time} 记得来参加{event}, 地点在{location}, {note}"
    for inf in infos:
        if inf['微信昵称'] == name:
            msg = template.format(
                    name=inf['微信昵称'],
                    time=inf['时间'],
                    event=inf['事件'],
                    location=inf['地址'],
                    note=inf['备注']
                )
            return msg


def send_msg(path, friends):
    bot = Bot()
