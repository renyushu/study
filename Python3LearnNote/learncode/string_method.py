# s = 'hello world'
# #
# # index = s.find('y')
# # print(index)
# #
# # strings = '''hello\n
# # world\n
# # python\n'''
# #
# # print(strings)


# -------------
S = 'spammy'
L = list(S) # 字符串转换为列表
print(L)

L[2] = '3'
L[4] = '4'

print(L)

S1 = ''.join(L)
print(S1)