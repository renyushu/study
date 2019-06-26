# 姓名名单数据
string = "哈利·波特、罗恩·韦斯莱、赫敏·格兰杰、乔治·韦斯莱、弗雷·韦斯莱、纳威、卢娜、阿不思·珀西瓦尔·邓布立多"

# 筛选出姓氏并打印出来
string_list = string.split("、")
# print(string_list)
s = set([])
for i in string_list:
    s.add(i)

# print(s)

for item in s:
    # print(item)
    item_list = item.split("·")
    # print(item_list)
    if len(item_list) >= 2:
        print(item_list[-1])

# last_name_set = set([])
# # 分割字符串为列表
# data = string.split("、")
# for name in data:
# 	# 利用·字符来分割名字
#     list = name.split("·")
#     # 判断名字中是否有多个分割
#     if len(list) >= 2:
#         last_name = list[-1]
#         # 在集合中添加元素
#         last_name_set.add(last_name)
# # 打印结果
# print(last_name_set)