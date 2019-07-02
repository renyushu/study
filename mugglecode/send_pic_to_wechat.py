# -*- coding: utf-8 -*-
from wxpy import *


pic_path = '/Users/yushufeng/Downloads/180_dog.jpeg'
bot = Bot(cache_path=True)
friends = ['Stu Yu', 'Echo海', '野猪佩奇']


def send_pic_to_friend(friends):
    for friend in friends:
        friend_search = bot.friends().search(friend)
        print(friend_search)
        if friend_search:
            friend_search[0].send_image(pic_path)
        else:
            print("发送失败！请检查用户名：" + friend)


send_pic_to_friend(friends)