import tkinter as tk
from tkinter import ttk

# 定义窗口
window = tk.Tk()
# 窗口标题
window.title('my window')
# 窗口大小
window.geometry('200x100')

# 标签描述
l = tk.Label(window, text='this is a label', bg='green', font=('Arial', 12), width=15, height=2).pack
button = ttk.Button(window, text='click me').pack() # 需要使用ttk.button,否则不显示文字（https://my.oschina.net/nYtgEmMGe/blog/3032875
# 运行窗口
window.mainloop()