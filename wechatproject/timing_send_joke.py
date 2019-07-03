import requests
from wxpy import *
import time


def get_joke():
    url = 'https://www.mxnzp.com/api/jokes/list/random'
    res = requests.get(url).json()
    joke = res['data'][0]['content']
    return joke


# j = get_joke()
# print(j)

bot = Bot(cache_path=True)
found = bot.friends().search('Stu Yu')[0] # 搜索朋友
wx_group = bot.groups().search('一起玩耍鸭')[0] # 搜索群聊
# found.send('hello')
# wx_group[0].send('hello')


while True:
    joke = get_joke()
    joke = '粑粑给猪猪讲个笑话: \n' + joke + '\n'
    wx_group.send(joke)

    time.sleep(60)