from tkinter import *
from pip._internal.utils.misc import get_installed_distributions

libs = get_installed_distributions()
# print(libs)
tk = Tk()
label = Label(text='All python libs', font=('Hack',25,'bold'))
label.pack()

listbox = Listbox(bg='#f2f2f2', fg='red')
listbox.pack(fill=BOTH, expand=True)

for l in libs:
    # print(l)
    listbox.insert(END, l)
tk.mainloop()