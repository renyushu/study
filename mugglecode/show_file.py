from tkinter import *
import os


"""
如何做一个展示隐藏文件的小工具
    1,如何找到隐形文件
        隐藏文件规则：
            mac/linux 系统的隐藏文件以.开头
            windows:
    2，如何以界面的形式表现出来？
        创建对象来呈现数据
            Tkinter 面向对象（集合很对
"""

app = Tk()
label = Label(text='All hidden files', font=('Hack',25,'bold'))
label.pack()
path = '/Users/yushufeng/'
files = os.listdir(path)
listbox = Listbox(bg='#f2f2f2', fg='red')
listbox.pack(fill=BOTH, expand=True)

for f in files:
    if f.startswith('.'):
        # print(f)
        # btn = Button(text=f).pack()
        listbox.insert(END, f)

app.mainloop()
