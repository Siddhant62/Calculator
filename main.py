from tkinter import *
import cmath as math


class Calc():
    def __init__(self):
        self.total = 0
        self.curr = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def numPress(self, num):
        self.eq = False
        tmp = text_box.get()
        tmp2 = str(num)
        if self.new_num:
            self.curr = tmp2
            self.new_num = False
        else:
            if tmp2 == '.':
                if tmp2 in tmp:
                    return
            self.curr = tmp + tmp2
        self.show(self.curr)


    def calTot(self):
        self.eq = True
        self.curr = float(self.curr)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def show(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.curr
        if self.op == "sub":
            self.total -= self.curr
        if self.op == "times":
            self.total *= self.curr
        if self.op == "divide":
            self.total /= self.curr
        if self.op == "raise":
            self.total = self.total ** self.curr
        if self.op == "rootof":
            self.total = self.total ** 0.5
        if self.op == "complex1":
            self.total=complex(self.total,self.curr)
        if self.op == "log":
            self.total=log(self.total,10)
        if self.op == "inv":
            self.total = 1/self.total
        self.new_num = True
        self.op_pending = False
        self.show(self.total)

    def operation(self, op):
        self.curr = float(self.curr)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.curr
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.curr = "0"
        self.show(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.curr = -(float(text_box.get()))
        self.show(self.curr)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Our CALC")
text_box = Entry(calc, justify=RIGHT,width=30,font="Arial 10 bold")
text_box.grid(row = 0, column = 0,columnspan = 20,padx=30, pady = 30)
text_box.insert(0, "0")


numbers = "123456789"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        bttn[i]["bg"]= "yellow"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.numPress(x)
        i += 1

bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="yellow")
bttn_0["command"] = lambda: sum1.numPress(0)
bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

div = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="red")
div["command"] = lambda: sum1.operation("divide")
div.grid(row = 1, column = 3, padx=1, pady = 1)

mul = Button(calc,height =2,width=4,padx=10, pady = 10, text = "x",bg="red")
mul["command"] = lambda: sum1.operation("times")
mul.grid(row = 2, column = 3,  padx=1, pady = 1)

sub = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="red")
sub["command"] = lambda: sum1.operation("sub")
sub.grid(row = 3, column = 3, padx=1, pady = 1)

add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="red")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3,  padx=1, pady = 1)

power = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y",bg="green")
power["command"] = lambda: sum1.operation("raise")
power.grid(row=2,column = 4,padx=1,pady=1)

rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="sqrt", bg = "green")
rootof["command"] = lambda: sum1.operation("rootof")
rootof.grid(row=2, column=5, padx=1, pady=1)

complex1 = Button(calc, height=2, width=4, padx=10, pady=10, text="complex",bg="green")
complex1["command"] = lambda: sum1.operation("complex1")
complex1.grid(row=3, column=5, padx=1, pady=1)

log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="green")
log10["command"]= lambda: sum1.operation("log")
log10.grid(row=3, column=4, padx=1 , pady=1)

inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="green")
inv["command"] = lambda: sum1.operation("inv")
inv.grid(row=4,column=4,padx=1,pady=1)

point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="white")
point["command"] = lambda: sum1.numPress(".")
point.grid(row = 4, column = 1, padx=1, pady = 1)

neg= Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="white")
neg["command"] = sum1.sign
neg.grid(row = 4, column = 2,  padx=1, pady = 1)


clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="white")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 4,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="white")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

equals = Button(calc,height =4,width=4,padx=10, pady = 10, text = "=",bg="green")
equals["command"] = sum1.calTot
equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)

root.mainloop()