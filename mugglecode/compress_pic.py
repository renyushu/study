


"""
    如何压缩图片
        第三方库实现：PIL
    如何以界面展示出来
        以用户为中心

    # compress image

"""

from PIL import Image as pic
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk


# image_path = "/Users/yushufeng/Desktop/pycharm.jpg"
# out_path = "/Users/yushufeng/Desktop/test.jpg"
# image = Image.open(image_path)
# image.save(out_path, quality=60)

info = {
    'path': []
}


def do():
    print('hello')


def make_app():
    app = Tk()
    Label(app, text='Image compress tool').pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    ttk.Button(app, text='open', width=10, command=ui_update).pack()
    ttk.Button(app, text='compresss', command=compress).pack()
    app.geometry('300x400')
    return app


def ui_update():
    file_names = askopenfilenames()
    # print(file_names)
    lbox = app.children['lbox']
    info['path'] = file_names
    if info['path']:
        for name in file_names:
            lbox.insert(END, name.split('/')[-1])


def compress():
    for file_name in info['path']:
        print('file path '+file_name)
        output = "/Users/yushufeng/Desktop/"
        name = file_name.split('/')[-1]
        image = pic.open(file_name)
        image.save(output+'c_'+name, quality=60)


app = make_app()
app.mainloop()