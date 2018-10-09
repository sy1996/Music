from tkinter import *
from pygame import mixer
import time
window=Tk()
window.title("播放器")
window.geometry("600x400")
var4=StringVar()
var4.set("欢迎来到傻子音乐")
label=Label(window,width=50,height=4,textvariable=var4,bg="white",font=("宋体，25"))
label.pack()
var=StringVar()
var.set("暂停")
mixer.init()
li =[r'D:\CloudMusic\Jiaye - Fade Again.mp3',
     r'D:\CloudMusic\Conor Maynard - Faded.mp3',
     r'D:\CloudMusic\Mario - 永昼.mp3',
     r'D:\CloudMusic\赵雷 - 彩虹下面.mp3',
     r'D:\CloudMusic\薛之谦 - 最好.mp3',]
num=0
def playMusic():
    num=0
   # var1= list.get("anchor")
    path=li[num]
    var4.set(path)
    mixer.music.load(path)
    mixer.music.play()


def up():
    global num
    num-1
    if num<=-5:
        num=num+5
    num -=1
    var4.set(li[num])
    path = li[num]
    mixer.music.load(path)
    mixer.music.play()
    return num

def down():
    global num
    num-1
    if num>=4:
        num=num-5
    num +=1
    var4.set(li[num])
    path = li[num]
    mixer.music.load(path)
    mixer.music.play()
    return num
flag=True
def left():
    global  flag

    if flag:
        var.set("继续")
        mixer.music.pause()
        flag = False
    else:
        var.set("暂停")
        mixer.music.unpause()
        flag = True

var3=StringVar()

but=Button(window,text="上一首",command=up)
but.place(x=150,y=80,width=50,height=20)

but1=Button(window,text="播放",command=playMusic)
but1.place(x=230,y=80,width=50,height=20)

but2=Button(window,text="暂停",textvariable=var,command=(left))
but2.place(x=310,y=80,width=50,height=20)

but3=Button(window,text="下一曲",command=down)
but3.place(x=400,y=80,width=50,height=20)

list=Listbox(window,font=("宋体，25"),listvariable=var3)
list.place(x=150,y=120,width=300,height=200)

for i in li:
    list.insert("end", i)
window.mainloop()