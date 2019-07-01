# -*- coding: utf-8 -*-
import requests
from datetime import datetime
from datetime import timedelta
import time

"""
从 GitHub 上选出符合这些条件的项目：1. 最近一周内发布的2. Star 数大于 2003. topic 是 blockchain当出现时，发送手机推送

"""


def get_new_lib():
    new_lib = []
    api = "https://api.github.com/search/repositories?q"
    query = "=" + "blockchain"
    full_url = api + query
    # print(full_url)
    res = requests.get(full_url).json()
    items = res['items']
    # print(items)
    date_now = datetime.now()
    date_week_ago = date_now - timedelta(days=1)
    for item in items:
        # print(item['name'])
        # print(item['updated_at'])
        if item['updated_at'] > str(date_week_ago) and item['updated_at'] < str(date_now) and item['stargazers_count'] > 200:
            # print(item['name'])
            data = {
                # "item": item,
                "name": item['name'],
                "html": item['html_url'],
                "stars": item["stargazers_count"]
            }
            new_lib.append(data)

    return new_lib


# libs = get_new_lib()
# print(libs)


def make_message():
    pass


def push_message(message):
    api = "https://api.pushover.net/1/messages.json"
    data = {
        'token': 'ar598cxqpcxzb3obks61archfyo5w3',
        'user': 'ubdxvtczjnqsqthvhsm1nd2angkx9d',
        'title': 'new rep',
        'url': ' ',
        'message': message
    }
    res = requests.post(url=api, data=data)
    # print(res)


# message = 'hello'
# push_message(message)



result = []
while True:
    new_lib = get_new_lib()
    # print(new_lib)
    for lib in new_lib:
        # print(lib['html'])
        if lib['html'] not in result:
            message = 'The Project' + lib['name'] + ' is qualified.' + ' URL: ' + lib['html']
            push_message(message)
            result.append(lib['html'])
            print('{} push done'.format(lib['html']))
    print(len(result))
    time.sleep(6)
    print('{} while done'.format(datetime.now()))
    print('')