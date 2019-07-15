# 列表数据
list = [1,2,3,4,5,6,7,8,9]

# 实现列表中的元素都加100
for i in range(0, len(list)):
    list[i] = list[i] + 100
#
# for i in list:
#     print(i)

# print(len(list))
# 打印列表的第3-6个元素、和倒数第一个元素
for i in range(0, len(list)):
    # print(list[i])
    # print('list: ' + str(len(list)))
    # if i>1 and i<6:
    #     print(list[i])
    #     print(i)
    if i == len(list)-1:
        print(list[i])
        # print(i)