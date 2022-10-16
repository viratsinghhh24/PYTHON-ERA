from tkinter import Y


x="excellent"
def myfunc():
 print("python is "+x)
myfunc()
y="great"
def myfunc():
    global y 
    y="fantastic"

myfunc()
print("python is " +y)   