from tkinter import *
from tkinter import messagebox
import math
screen=Tk()
screen.title('Calculator')
screen.configure(bg='blue')
screen.maxsize(width=453,height=490)
screen.minsize(width=362,height=490)
screen.geometry('362x488')

tex=StringVar()
operator=''

def click(number):
    global operator
    operator+=str(number)

def clear():
    global operator
    operator=''
    tex.set(operator)

def equal():
    tex.set(operator)
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification','Invalid input!',parent=screen)

def cmsin():
    global  operator
    result=math.sin(eval(tex.get()))
    operator=str(result)
    tex.set((operator))

def cmcos():
    global  operator
    result=math.cos(eval(tex.get()))
    operator=str(result)
    tex.set((operator))

def cmtan():
    global  operator
    result=math.tan(eval(tex.get()))
    operator=str(result)
    tex.set((operator))

def cmsqrt():
    global  operator
    result=math.sqrt(eval(tex.get()))
    operator=str(result)
    tex.set((operator))

def cmlog():
    global  operator
    result=math.log(eval(tex.get()))
    operator=str(result)
    tex.set((operator))

#touch color
def on_enter7(e):
    btn7.configure(bg='red')
def on_leave7(e):
    btn7.configure(bg='white')

def on_enter8(e):
    btn8.configure(bg='red')
def on_leave8(e):
    btn8.configure(bg='white')

def on_enter9(e):
    btn9.configure(bg='red')
def on_leave9(e):
    btn9.configure(bg='white')

def on_enteradd(e):
    btnadd.configure(bg='red')
def on_leaveadd(e):
    btnadd.configure(bg='white')

def on_enter4(e):
    btn4.configure(bg='red')
def on_leave4(e):
    btn4.configure(bg='white')

def on_enter5(e):
    btn5.configure(bg='red')
def on_leave5(e):
    btn5.configure(bg='white')

def on_enter6(e):
    btn6.configure(bg='red')
def on_leave6(e):
    btn6.configure(bg='white')

def on_entersub(e):
    btnsub.configure(bg='red')
def on_leavesub(e):
    btnsub.configure(bg='white')

def on_enter1(e):
    btn1.configure(bg='red')
def on_leave1(e):
    btn1.configure(bg='white')

def on_enter2(e):
    btn2.configure(bg='red')
def on_leave2(e):
    btn2.configure(bg='white')

def on_enter3(e):
    btn3.configure(bg='red')
def on_leave3(e):
    btn3.configure(bg='white')

def on_entermul(e):
    btnmul.configure(bg='red')
def on_leavemul(e):
    btnmul.configure(bg='white')

def on_enter0(e):
    btn0.configure(bg='red')
def on_leave0(e):
    btn0.configure(bg='white')

def on_enterC(e):
    btnC.configure(bg='red')
def on_leaveC(e):
    btnC.configure(bg='white')

def on_enterequal(e):
    btnequal.configure(bg='red')
def on_leaveequal(e):
    btnequal.configure(bg='white')

def on_enterdiv(e):
    btndiv.configure(bg='red')
def on_leavediv(e):
    btndiv.configure(bg='white')

#advance
def on_entersin(e):
    btnsin.configure(bg='red')
def on_leavesin(e):
    btnsin.configure(bg='white')

def on_entercos(e):
    btncos.configure(bg='red')
def on_leavecos(e):
    btncos.configure(bg='white')

def on_entertan(e):
    btntan.configure(bg='red')
def on_leavetan(e):
    btntan.configure(bg='white')

def on_entersqrt(e):
    btnsqrt.configure(bg='red')
def on_leavesqrt(e):
    btnsqrt.configure(bg='white')

def on_enterlog(e):
    btnlog.configure(bg='red')
def on_leavelog(e):
    btnlog.configure(bg='white')


def on_enterentry(e):
    entry1.configure(bg='red',fg='white')
def on_leaveentry(e):
    entry1.configure(bg='orange',fg='black')

#enter box
entry1=Entry(screen,bg='orange',font=('aerial',20,'italic bold'),bd=30,justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)
entry1.bind('<Enter>',on_enterentry)
entry1.bind('<Leave>',on_leaveentry)

#row 1
btn7=Button(screen,text='7',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(7),activebackground='green',activeforeground='white')
btn7.grid(row=1,column=0)
btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)


btn8=Button(screen,text='8',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(8),activebackground='green',activeforeground='white')
btn8.grid(row=1,column=1)
btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)


btn9=Button(screen,text='9',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(9),activebackground='green',activeforeground='white')
btn9.grid(row=1,column=2)
btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)


btnadd=Button(screen,text='+',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click('+'),activebackground='green',activeforeground='white')
btnadd.grid(row=1,column=3)
btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)


#row 2
btn4=Button(screen,text='4',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(4),activebackground='green',activeforeground='white')
btn4.grid(row=2,column=0)
btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)


btn5=Button(screen,text='5',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(5),activebackground='green',activeforeground='white')
btn5.grid(row=2,column=1)
btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)


btn6=Button(screen,text='6',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(6),activebackground='green',activeforeground='white')
btn6.grid(row=2,column=2)
btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)


btnsub=Button(screen,text='-',font=('aerial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda :click('-'),activebackground='green',activeforeground='white')
btnsub.grid(row=2,column=3)
btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)



#row 3
btn1=Button(screen,text='1',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(1),activebackground='green',activeforeground='white')
btn1.grid(row=3,column=0)
btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)


btn2=Button(screen,text='2',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(2),activebackground='green',activeforeground='white')
btn2.grid(row=3,column=1)
btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)


btn3=Button(screen,text='3',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(3),activebackground='green',activeforeground='white')
btn3.grid(row=3,column=2)
btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)


btnmul=Button(screen,text='*',font=('aerial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda :click('*'),activebackground='green',activeforeground='white')
btnmul.grid(row=3,column=3)
btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)


#row 4
btn0=Button(screen,text='0',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda :click(0),activebackground='green',activeforeground='white')
btn0.grid(row=4,column=0)
btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnC=Button(screen,text='C',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=clear,activebackground='green',activeforeground='white')
btnC.grid(row=4,column=1)
btnC.bind('<Enter>',on_enterC)
btnC.bind('<Leave>',on_leaveC)


btnequal=Button(screen,text='=',font=('aerial',20,'italic bold'),bd=8,padx=16,pady=16,command=equal,activebackground='green',activeforeground='white')
btnequal.grid(row=4,column=2)
btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)


btndiv=Button(screen,text='/',font=('aerial',20,'italic bold'),bd=8,padx=19,pady=16,command=lambda :click('/'),activebackground='green',activeforeground='white')
btndiv.grid(row=4,column=3)
btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

#advance
#coloumn 4
btnsin=Button(screen,text='sin',font=('aerial',15,'italic bold'),bd=8,padx=14,pady=19,command=cmsin,activebackground='green',activeforeground='white')
btnsin.grid(row=0,column=4)
btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos=Button(screen,text='cos',font=('aerial',15,'italic bold'),bd=8,padx=14,pady=19,command=cmcos,activebackground='green',activeforeground='white')
btncos.grid(row=1,column=4)
btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)


btntan=Button(screen,text='tan',font=('aerial',15,'italic bold'),bd=8,padx=16,pady=19,command=cmtan,activebackground='green',activeforeground='white')
btntan.grid(row=2,column=4)
btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)


btnsqrt=Button(screen,text='sqrt',font=('aerial',15,'italic bold'),bd=8,padx=14,pady=19,command=cmsqrt,activebackground='green',activeforeground='white')
btnsqrt.grid(row=3,column=4)
btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog=Button(screen,text='log',font=('aerial',15,'italic bold'),bd=8,padx=16,pady=19,command=cmlog,activebackground='green',activeforeground='white')
btnlog.grid(row=4,column=4)
btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)

#end
screen.mainloop()