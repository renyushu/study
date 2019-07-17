from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import *
# ui# ui update
# business
info = {'path': []}


def make_app():
    app = Tk()
    Label(app,   text='Image   compress   tool',   font=('Hack',20)).pack()#Hack是自己安装的字体，如果你没安装，可以用系统自带的Arial字体
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='open', command=ui_getdata).pack()
    Button(app, text='compresss', command=compress).pack()
    app.geometry('300x400')
    return app


def ui_getdata():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])# abc.jpg


def compress():
    for f_path in info['path']:
        output = '/Users/yushufeng/Desktop/'  #这里需要换成你的图片输出路径
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        image.save(output+'c_'+name, quality=60)


app = make_app()
app.mainloop()

