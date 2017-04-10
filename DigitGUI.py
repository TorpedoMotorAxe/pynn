"""
Develop ment of simple GUI to display digital form of digits
"""

from tkinter import *

root=Tk()

frameDigit=Frame(bg='red',width=200,height=450)
frameDigit.grid(row=0,column=0,rowspan=2)

frameButtons=Frame(bg='magenta',width=200,height=200)
frameButtons.grid(row=0,column=1)

frameOut=Frame(bg='green',width=200,height=200)
frameOut.grid(row=1,column=1)

def callback(msg):
    print(msg)

msg=0
for i in [0,1]:
    for j in [0,1,2,3,4]:
        b=Button(frameButtons,text=str(msg),font=("Arial 12 bold"))
        b.config(command=lambda k=msg: callback(k) )
        b.grid(row=i,column=j)
        msg += 1
        

mainloop()
