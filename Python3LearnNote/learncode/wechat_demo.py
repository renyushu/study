from wxpy import *
from wechat_sender import *

# bot = Bot(cache_path=True, console_qr=2)
#
# bot.file_helper.send('hello')
#
# print('ending')
# print('hello')
# fs = bot.friends()
# for f in fs:
#     print(f)
#
# gs = bot.groups()
# for g in gs:
#     print(g)
#
# f = bot.friends().search('Stu Yu')[0]
# print(f)
#
# g = bot.groups().search('test')[0]
# print(g)
#
# embed()


bot = Bot(cache_path=True, console_qr=2)

f = bot.friends().search('Stu Yu')[0]

listen(bot, token='test', receivers=[f], status_report=True, status_receiver=[f]) # token用于避免多个listen导致sender混淆

