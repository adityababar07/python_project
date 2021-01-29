import tkinter
from tkinter.constants import *

root = tkinter.Tk()
frame = tkinter.Frame(root, relief=RIDGE, borderwidth=4)
frame.pack(fill=BOTH, expand=1)
label = tkinter.Label(frame, text="hello world!!!")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame, text='Exit', command=root.destroy)
button.pack(side=BOTTOM)
root.mainloop()
