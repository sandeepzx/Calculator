from tkinter import *

root = Tk()
i= 0
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def get_variable(num):
    global i
    display.insert(i,num)
    i+=1
def clear():
    display.delete(0,E)

def back_space():
    entire_str = display.get()
    if len(entire_str):
        new_str = entire_str[:-1]
        clear()
        display.insert(0,new_str)
    else:
        clear()
        display.insert(0,"Error")
def get_operation(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i+=1
def calculate():
    entire_str = display.get()
    if entire_str[-1]=="!":
        new = entire_str[:-1]
        result = factorial(int(new))
        clear()
        display.insert(0,result)
    else:
        try:
            result = eval(entire_str)
            clear()
            display.insert(0,result)
        except :
            clear()
            display.insert(0,"Error")



display = Entry(root)
display.grid(row=1,columnspan=6, sticky=W+E)

Button(root,text=" 1 ",command= lambda :get_variable(1)).grid(row=2,column=1)
Button(root,text=" 2 ",command= lambda :get_variable(2)).grid(row=2,column=2)
Button(root,text=" 3 ",command= lambda :get_variable(3)).grid(row=2,column=3)
Button(root,text=" 4 ",command= lambda :get_variable(4)).grid(row=3,column=1)
Button(root,text=" 5 ",command= lambda :get_variable(5)).grid(row=3,column=2)
Button(root,text=" 6 ",command= lambda :get_variable(6)).grid(row=3,column=3)
Button(root,text=" 7 ",command= lambda :get_variable(7)).grid(row=4,column=1)
Button(root,text=" 8 ",command= lambda :get_variable(8)).grid(row=4,column=2)
Button(root,text=" 9 ",command= lambda :get_variable(9)).grid(row=4,column=3)
Button(root,text=" 0 ",command= lambda :get_variable(0)).grid(row=5,column=2)
Button(root,text="AC", command=lambda: clear()).grid(row=5,column=1)
Button(root,text=" = ", command=lambda: calculate()).grid(row=5,column=3)
Button(root,text=" + ", command=lambda: get_operation("+")).grid(row=2,column=4)
Button(root,text=" - ", command=lambda: get_operation("-")).grid(row=3,column=4)
Button(root,text=" * ", command=lambda: get_operation("*")).grid(row=4,column=4)
Button(root,text=" / ", command=lambda: get_operation("/")).grid(row=5,column=4)
Button(root,text=" ( ", command=lambda: get_operation("(")).grid(row=6,column=4)
Button(root,text=" % ", command=lambda: get_operation("%")).grid(row=2,column=5)
Button(root,text=" x!", command=lambda: get_operation("!")).grid(row=3,column=5)
Button(root,text=" pi", command=lambda: get_operation("3.14")).grid(row=4,column=5)
Button(root,text="exp", command=lambda: get_operation("**")).grid(row=5,column=5)
Button(root,text=" ) ", command=lambda: get_operation(")")).grid(row=6,column=5)

root.mainloop()
