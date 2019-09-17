from wechat_sender import Sender


sender = Sender(token='test')
sender.send('hello wechat')
sender.send('send to wechat')
