# -*- coding: utf-8 -*-


"""
如何对比多个库
    用哪些参考数值
        生态值
            社区，根据fork值来判断
        star
        fork
    如何获取数据
        github api

    如何查询数据
        input模拟查询


"""
import requests


# get names
def get_names():
    print("输入库的名字以空格空开")
    names = input()
    return names.split(' ')


def check_repos(names):
    api_rep = "https://api.github.com/search/repositories?q="
    ecosys_api = "https://api.github.com/search/repositories?q=topic:"
    for name in names:
        res = requests.get(api_rep+name).json()['items'][0]
        stars  = res['stargazers_count']
        forks = res['forks_count']

        ecosys_info = requests.get(ecosys_api+name).json()['total_count']
        print(name)
        print('strars:'+str(stars))
        print('forks:'+str(forks))
        print('ecosys_info:'+ str(ecosys_info))
        print('--------------')


names = get_names()
check_repos(names)