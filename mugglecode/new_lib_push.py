from datetime import datetime
import requests


"""
如何发送新库提醒到手机
    获取新库信息
        # https://api.github.com/search/repositories?q=topic:crawler+language:python&2019-06-28
    使用pushover推送

"""

# get_info list --> push_it


def get_info_list():
    api = "https://api.github.com/search/repositories?q"
    query = "=topic:crawler+language:python&"
    when = str(datetime.now()).split(' ')[0]
    full_url = api + query + when
    # print(full_url)
    res = requests.get(full_url)
    return res.json()['items']


def push_info():
    pass


info = get_info_list()
print(info)