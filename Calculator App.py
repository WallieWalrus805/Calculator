from tkinter import *

root = Tk()
root.configure(background='light gray')
root.title('Simple Calculator')
root.iconbitmap('Cat.ico')

e = Entry(root, width=35, borderwidth=5)

def button_click(number):
    if e.get() == 'Cannot divide by zero':
        current = ''
    else:
        current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    math = ''

def button_add():
    try:
        global num1
        global math
        math = '+'
        num1 = e.get()
        num1 = float(num1)
        button_clear()
    except ValueError:
        pass

def button_subtract():
    try:
        global num1
        global math
        math = '-'
        num1 = e.get()
        num1 = float(num1)
        button_clear()
    except ValueError:
        pass

def button_multiply():
    try:
        global num1
        global math
        math = '*'
        num1 = e.get()
        num1 = float(num1)
        button_clear()
    except ValueError:
        pass

def button_divide():
    try:
        global num1
        global math
        math = '÷'
        num1 = e.get()
        num1 = float(num1)
        button_clear()
    except ValueError:
        pass
def button_equal():
    try:
        num2 = e.get()
        e.delete(0, END)
        if math == '+':
            e.insert(0, float(num1) + float(num2))
        elif math == '-':
            e.insert(0, float(num1) - float(num2))
        elif math == '*':
            e.insert(0, float(num1) * float(num2))
        elif math == '÷':
            try:
                e.insert(0, float(num1) / float(num2))
            except ZeroDivisionError:
                e.insert(0, 'Cannot divide by zero')
    except ValueError:
        pass

key1 = Button(root, text='1', command=lambda: button_click(1), padx=40, pady=20)
key2 = Button(root, text='2', command=lambda: button_click(2), padx=40, pady=20)
key3 = Button(root, text='3', command=lambda: button_click(3), padx=40, pady=20)
key4 = Button(root, text='4', command=lambda: button_click(4), padx=40, pady=20)
key5 = Button(root, text='5', command=lambda: button_click(5), padx=40, pady=20)
key6 = Button(root, text='6', command=lambda: button_click(6), padx=40, pady=20)
key7 = Button(root, text='7', command=lambda: button_click(7), padx=40, pady=20)
key8 = Button(root, text='8', command=lambda: button_click(8), padx=40, pady=20)
key9 = Button(root, text='9', command=lambda: button_click(9), padx=40, pady=20)
key0 = Button(root, text='0', command=lambda: button_click(0), padx=40, pady=20)
key_point = Button(root, text='. ', command=lambda: button_click('.'), padx=40, pady=20)
key_add = Button(root, text='+', command=button_add, padx=40, pady=20)
key_subtract = Button(root, text='- ', command=button_subtract, padx=40, pady=20)
key_multiply = Button(root, text='* ', command=button_multiply, padx=40, pady=20)
key_divide = Button(root, text='÷', command=button_divide, padx=40, pady=20)
key_equal = Button(root, text='=', command=button_equal, padx=40, pady=20)
key_clear = Button(root, text='C', command=button_clear, padx=40, pady=20)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
key_divide.grid(row=0, column=3)

key7.grid(row=1, column=0)
key8.grid(row=1, column=1)
key9.grid(row=1, column=2)
key_multiply.grid(row=1, column=3)

key4.grid(row=2, column=0)
key5.grid(row=2, column=1)
key6.grid(row=2, column=2)
key_subtract.grid(row=2, column=3)

key1.grid(row=3, column=0)
key2.grid(row=3, column=1)
key3.grid(row=3, column=2)
key_add.grid(row=3, column=3)

key_clear.grid(row=4, column=0)
key0.grid(row=4, column=1)
key_point.grid(row=4, column=2)
key_equal.grid(row=4, column=3)

root.mainloop()
