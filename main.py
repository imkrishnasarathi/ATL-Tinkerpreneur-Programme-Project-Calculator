from tkinter import *

root = Tk()
root.minsize(500, 700)
root.maxsize(500, 700)

display = Label(root, text='0', font="monospace 25 bold", background='#517059', height=2, anchor='w', width=22)
display.grid(columnspan=4, row=0, pady=35, padx=23)

buttons = Frame(root, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=200, height=100)
buttons.grid(columnspan=4, row=1)

# First row

btnClear = Button(buttons, text='C', width=37, height=3)
btnClear.grid(row=0, columnspan=3)

btnDivide = Button(buttons, text='/', height=3, width=10)
btnDivide.grid(row=0, column=3)

# Second Row

btnSeven = Button(buttons, text='7', height=3, width=10)
btnEight = Button(buttons, text='8', height=3, width=10)
btnNine = Button(buttons, text='9', height=3, width=10)
btnMultiply = Button(buttons, text='*', height=3, width=10)

btnSeven.grid(row=1, column=0)
btnEight.grid(row=1, column=1)
btnNine.grid(row=1, column=2)
btnMultiply.grid(row=1, column=3)


root.mainloop()