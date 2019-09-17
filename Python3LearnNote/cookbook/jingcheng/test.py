# Code to execute in an independent thread
import time
import os


# print(os.getpid())
#
#
# def countdown(n):
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#         time.sleep(5)
#
#
# # Create and launch a thread
# from threading import Thread
#
# t = Thread(target=countdown, args=(10,))
# t.start()
#
# print(os.getpid())

# s = 'str'
# print(type(s))
#
# if isinstance(s, str):
#     print('t')

print(type(__file__))
m = __file__.split('.')[0].split('/')[-1]
print(m)