from tkinter import *
from tkinter import ttk
import math as mt

root = Tk()
root.resizable(False,False)
root.title('Calc')
#------IO ENTRY----------
io_entry = ttk.Entry(width=15)
io_entry.grid(row = 0, column = 1)
#--------Functions-------
def cls_entry():
    io_entry.delete(0,END)
def ioentry_get():
    entry_get = io_entry.get()
    return entry_get
def sin_f():
    get_s = ioentry_get()
    cls_entry()
    ans = mt.sin(mt.radians(float(get_s)))
    io_entry.insert(END,ans)
def cos_f():
    get_s = ioentry_get()
    cls_entry()
    ans = mt.cos(mt.radians(float(get_s)))
    io_entry.insert(END,ans)
def tan_f():
    get_s = ioentry_get()
    cls_entry()
    ans = mt.tan(mt.radians(float(get_s)))
    io_entry.insert(END,ans)
def sqrt_f():
    num = float(io_entry.get())
    sqr_ans = mt.sqrt(num)
    io_entry.delete(0,END)
    io_entry.insert(END,sqr_ans)
def equal_f():
    inpt = io_entry.get()
    c = eval(str(inpt))
    io_entry.delete(0,END)
    io_entry.insert(END, c)
def bspace_f():
    io_len = len(io_entry.get())
    io_entry.delete(io_len-1,END)
#----------Symbols-----------
sqrt_s = '√'
pi_s = 'π'
bspace_s = '←'
#--------Buttons lists---------

num_btn_l = ['1','2','3','4',
          '5','6','7','8',
          '9','0','.']

op_btn_l = ['+','-','*','/',
            sqrt_s,pi_s,'sin','cos',
            'tan',]
#-------------numbers----------
r = 1
col = 1
for i in num_btn_l:
    com = lambda x=i: io_entry.insert(END,x)
    b_n = ttk.Button(text=i, command = com,width=15)
    if col == 4:
        col = 1
        r += 1
    
    b_n.grid(column = col, row=r)
    col += 1

#--------operations-----------
r = 1
col = 5
for j in op_btn_l:
    com = lambda x=j: io_entry.insert(END,x)
    if j == sqrt_s:
        com = sqrt_f
    if j == pi_s:
        com = lambda x=0: io_entry.insert(END,mt.pi)
    if j == 'sin':
        com = sin_f
    if j == 'cos':
        com = cos_f
    if j == 'tan':
        com = tan_f     
    b_o = ttk.Button(text = j, command = com, width = 5)
    if col == 7:
        col = 5
        r += 1
    b_o.grid(column = col, row = r)
    col += 1
#-----indipended buttons------------
clear_com = lambda x=0: io_entry.delete(0,END)
c_b = ttk.Button(text = 'C',command=clear_com,width=5)#clear al
c_b.grid(row=5,column=6)
equal_b = ttk.Button(text='=', command = equal_f,width = 15)
equal_b.grid(column =3 ,row=4)
bspace_b = ttk.Button(text = '←', command =bspace_f ,width = 5)  
bspace_b.grid(column = 6, row = 0)




    
    
root.mainloop()
