from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text='GeeksForGeeks', font="50")
w.pack()

checkButton1 = IntVar(value=1)
Button1 = Checkbutton(root, text = 'Option1', variable = checkButton1, onvalue = 1, offvalue = 0, height = 2, width = 10)
Button1.pack()

checkButton2 = IntVar(value=0)
Button2 = Checkbutton(root, text = 'Option2', variable = checkButton2, onvalue = 1, offvalue = 0, height = 2, width = 10)
Button2.pack()

checkButton3 = IntVar(value=0)
Button3 = Checkbutton(root, text = 'Option3', variable = checkButton3, onvalue = 1, offvalue = 0, height = 2, width = 10)
Button3.pack()

checkButton4 = IntVar(value=0)
Button4 = Checkbutton(root, text = 'Check Button', variable = checkButton4, onvalue = 1, offvalue = 0, height = 2, width = 10)
Button4.pack()


mainloop()