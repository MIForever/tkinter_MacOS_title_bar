from macTk import MacTk
from tkinter import *

root = MacTk() # create root
# all other stuff same as tkinter

# Don't forget to create your widgets with considering height of title bar (height=25)
btn = Button(root,bg='red',text='MyButton',activebackground='orange')
btn.place(x=200,y=200,height=30,width=80)
root.mainloop()