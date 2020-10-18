# This is a sample Python script.

import tkinter

# 创建窗口
window = tkinter.Tk()
window.title("计算器")

# 记录算式
expstr = ""

# 记录运算历史
history_label_obj_list = []


# 按钮点击事件
def onClick(key):
    global expstr  # 定义全局变量

    if key == "=":
        jieguo = round(eval(expstr), 2)  # 结果保留2位小数
        result["text"] = jieguo

        frame_right.pack()

        # 将算式记录显示出来
        t = tkinter.Label(frame_inner, text=expstr + "=" + str(jieguo),
                          background="seashell")
        t.pack()

        history_label_obj_list.append(t)  # 容器存储算式记录
    elif key == "AC":
        result["text"] = ""
        expstr = ""
    else:
        expstr = expstr + str(key)
        result["text"] = expstr


frame_grap = tkinter.Frame(window)
frame_grap.pack(fill="y", side="left")  # 按y坐标填满放在左侧

frame_left = tkinter.Frame(window)

# 定义一个标签，设置相关参数，存放结果
result = tkinter.Label(frame_left, bg="seashell", text="0", height=2, font=("Arial", 34, "bold"))
result.grid(row=0, column=0, columnspan=4, sticky=tkinter.E)  # 采用表格式布局管理器gid

# 设置“清空”按钮
ac = tkinter.Button(frame_left, text="AC", width=6, height=2, command=lambda: onClick("AC"))
ac.grid(row=1, column=0)  # (第1行，第0列)

#
negative = tkinter.Button(frame_left, text="+/-", width=6, height=2, command=lambda: onClick("-"))
negative.grid(row=1, column=1)

percent = tkinter.Button(frame_left, text="%", width=6, height=2, command=lambda: onClick("/100"))
percent.grid(row=1, column=2)

division = tkinter.Button(frame_left, text="/", width=6, height=2, command=lambda: onClick("/"))
division.grid(row=1, column=3)

num7 = tkinter.Button(frame_left, text="7", width=6, height=2, command=lambda: onClick(7))
num7.grid(row=2, column=0)

num8 = tkinter.Button(frame_left, text="8", width=6, height=2, command=lambda: onClick(8))
num8.grid(row=2, column=1)

num9 = tkinter.Button(frame_left, text="9", width=6, height=2, command=lambda: onClick(9))
num9.grid(row=2, column=2)

multi = tkinter.Button(frame_left, text="*", width=6, height=2, command=lambda: onClick("*"))
multi.grid(row=2, column=3)

num4 = tkinter.Button(frame_left, text="4", width=6, height=2, command=lambda: onClick(4))
num4.grid(row=3, column=0)

num5 = tkinter.Button(frame_left, text="5", width=6, height=2, command=lambda: onClick(5))
num5.grid(row=3, column=1)

num6 = tkinter.Button(frame_left, text="6", width=6, height=2, command=lambda: onClick(6))
num6.grid(row=3, column=2)

sub = tkinter.Button(frame_left, text="-", width=6, height=2, command=lambda: onClick("-"))
sub.grid(row=3, column=3)

num1 = tkinter.Button(frame_left, text="1", width=6, height=2, command=lambda: onClick(1))
num1.grid(row=4, column=0)

num2 = tkinter.Button(frame_left, text="2", width=6, height=2, command=lambda: onClick(2))
num2.grid(row=4, column=1)

num3 = tkinter.Button(frame_left, text="3", width=6, height=2, command=lambda: onClick(3))
num3.grid(row=4, column=2)

add = tkinter.Button(frame_left, text="+", width=6, height=2, command=lambda: onClick("+"))
add.grid(row=4, column=3)

num0 = tkinter.Button(frame_left, text="0", width=12, height=2, command=lambda: onClick(0))
num0.grid(row=5, column=0, columnspan=2)

point = tkinter.Button(frame_left, text=".", width=6, height=2, command=lambda: onClick("."))
point.grid(row=5, column=2)

equals = tkinter.Button(frame_left, text="=", width=6, height=2, command=lambda: onClick("="))
equals.grid(row=5, column=3)

frame_left.pack(fill="y", side="left")

frame_right = tkinter.Frame(window, width=200)
tkinter.Label(frame_right, text="运算历史", font=("Arial", 14, "underline bold")).pack()

frame_inner = tkinter.Frame(frame_right)
frame_inner.pack(fill="x", side="top")


# 清空运算历史
def clean_history():
    for x in history_label_obj_list:
        print(x)
        x.destroy()


cls_button = tkinter.Button(frame_right, text="清空", command=lambda: clean_history())
cls_button.pack(fill="x", side="top")

window.mainloop()