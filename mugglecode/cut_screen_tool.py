# -*- coding: utf-8 -*-
from PIL import Image as Img
from tkinter.filedialog import *
from tkinter import *
from tkinter import ttk


size = [50, 100, 120, 180, 512]
info = {}

def make_app():
    app = Tk()
    app.title('cut screen')
    Label(app, text='请上传正方形图片，点击[打开]按钮可以输入多张图片，点击[生成]可以等比例生成指定多个尺寸(50x50、100x100、120x120、180x180、512x512)').pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    ttk.Button(app, text='open', width=10, command=ui_update).pack()
    ttk.Button(app, text='create', width=10, command=business).pack()
    ttk.Button(app, text='choose path', width=10, command=None).pack()
    app.geometry('1000x700')
    return app


def ui_update():
    files = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = files
    if info['path']:
        for file in files:
            lbox.insert(END, file.split('/')[-1])


def business():
    if info['path']:
        for file in info['path']:
            print('file: '+file)
            output = '/Users/yushufeng/Downloads/'
            name = file.split('/')[-1]
            print('name: '+name)
            image = Img.open(file)
            for s in size:
                print(output+str(s)+"_"+name)
                image.resize((s,s)).save(output+str(s)+"_"+name)


def choose_path():
    folder = askdirectory()
    


app = make_app()
app.mainloop()

