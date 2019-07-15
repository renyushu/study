# 电影及演员数据
data = {
	'霸王别姬' : ['张国荣','张丰毅','巩俐','葛优'],
	'无间道' : ['刘德华','梁朝伟','黄秋生','曾志伟','郑秀文'],
	'活着' : ['葛优','巩俐','姜武','牛犇','郭涛']
}

# 遍历字典中的元素
# 自己写的
# for k, v in data.items():
#     # print(k, v)
#     actor = ''
#     for i in v:
#         if not actor:
#             actor = actor + i
#         else:
#             actor = actor + '、' + i
#     print("电影《%s》的主演有%s等。" % (k, actor))

# 联系答案
for movie in data:
    # print(movie)
    actors = data[movie]
    # 将列表转成字符串
    string = "、 ".join(actors)  # str.join(list) 按照str连接list里面的每个元素，返回一个新的字符串
    print("电影《" + movie + "》的主演有" + string + "。")

# 将列表转换为字符串
# for k, v in data.items():
#     for i in v:
#         data[k] =