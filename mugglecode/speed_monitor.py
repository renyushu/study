

"""
如何实时测速？
    水缸：

    没有手动触发
        1，启动即执行
        2，循环执行

    'en0'
如何
    def fun1():
    print('hello')
    app.after(1000, fun1)


app = Tk()
app.after(1000, fun1)
app.mainloop() # 两个循环会导致卡死
"""

from tkinter import *
import psutil
import time


# while True:
#     s1 = psutil.net_io_counters(pernic=True)['en0']
#     time.sleep(1)
#     s2 = psutil.net_io_counters(pernic=True)['en0']
#     res = s2.bytes_recv - s1.bytes_recv
#     print(res/1024)

def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    Label(text='Speed Monitor',
          font=('Hack', 25, 'bold'),
          bg='#303030',
          fg='white').pack()
    Label(
          name='lb2',
          text='-',
          font=('Hack', 20, 'bold'),
          bg='#303030',
          fg='white'
          ).pack()
    return app


def speed_test():
    s1 = psutil.net_io_counters(pernic=True)['en0']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['en0']
    res = s2.bytes_recv - s1.bytes_recv
    # print(res/1024)
    return str(res/1024) + 'kb/s'


def ui_update(do):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    lb2.after(1000, lambda: ui_update(do))


app = make_app()
app.after(1000, lambda: ui_update(speed_test))
app.mainloop()
