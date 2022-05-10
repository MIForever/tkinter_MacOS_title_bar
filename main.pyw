from tkinter import *
from tkinter import ttk
from time import sleep
from os import getcwd

root = Tk()
root.geometry('500x500+100+100')
root.overrideredirect(True)

def config(e):
    if root.wm_state() == 'normal':
        root.overrideredirect(True)
    exit_btn.config(image=exit_btn_img)
    maximize_btn.config(image=maximize_img)
    minimize_btn.config(image=minimize_img)
    exit_btn.place(x=root.winfo_width()-25,y=4)
    maximize_btn.place(x=root.winfo_width()-50,y=5)
    minimize_btn.place(x=root.winfo_width()-75,y=5)
    title_bar.place(width=root.winfo_width()+50)

# Window resizes as full screen when maximize button clicked 
fulled_screen = 0  #Variable for cheking window is full sized or not
def full_screen():
    global fulled_screen
    if fulled_screen==0:
        fulled_screen=1
        root.state('zoomed')
    elif fulled_screen==1:
        root.state('normal')
        fulled_screen=0

# Window hiding like iconify
def hide_screen():
    root.overrideredirect(False)
    root.iconify()
    screen_hidden=1

# For dragging window
def dragwin(event):
    x = title_bar.winfo_pointerx() - title_bar._offsetx
    y = title_bar.winfo_pointery() - title_bar._offsety
    root.geometry(f'+{x}+{y}'.format(x=x,y=y))

# Gettinng coordinates of title bar for dragging
def clickwin(event):
    title_bar._offsetx = event.x
    title_bar._offsety = event.y


root._offsetx = 0
root._offsety = 0

# Title bar (bar where located on top side)
title_bar = Label(root,bg='gray25')
title_bar.place(x=0,y=0,height=25,width=root.winfo_width())
title_bar.bind('<Button-1>',clickwin)
title_bar.bind('<B1-Motion>',dragwin)


# Exit button
exit_btn_img = PhotoImage(file=f'{getcwd()}\\photos\\red.png')
exit_btn = Button(title_bar,image=exit_btn_img,bd=0,bg='gray25',activebackground='gray25',command=root.destroy)
exit_btn.place(x=475,y=5,height=15,width=15)


# Maximize button (changes root size to full screen)
maximize_img = PhotoImage(file=f'{getcwd()}\\photos\\yellow.png')
maximize_btn = Button(title_bar,image=maximize_img,bd=0,bg='gray25',activebackground='gray25',command=full_screen)
maximize_btn.place(x=450,y=5,height=15,width=15)


# Minimize button (hiding)
minimize_img = PhotoImage(file=f'{getcwd()}\\photos\\green.png')
minimize_btn = Button(title_bar,image=minimize_img,bd=0,bg='gray25',activebackground='gray25',command=hide_screen)
minimize_btn.place(x=425,y=5,height=15,width=15)


#          SIDE RESIZING FUNCTIONS

def right_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry("%sx%s" % ((x1-x0),root.winfo_height()))


def left_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry(f"{root.winfo_width()-(x1-x0)}x{root.winfo_height()}+{root.winfo_x()+(x1-x0)}+{root.winfo_y()}")

def top_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()-(y1-y0)}+{root.winfo_x()}+{root.winfo_y()+(y1-y0)}")
    title_bar.config(height=25)

def bottom_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry(f"{root.winfo_width()}x{y1-y0}")

def right_bottom_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry(f"{x1-x0}x{y1-y0}")

def left_top_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry(f"{root.winfo_width()-(x1-x0)}x{root.winfo_height()-(y1-y0)}+{root.winfo_x()+(x1-x0)}+{root.winfo_y()+(y1-y0)}")
    title_bar.config(height=25)

def left_bottom_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry(f"{root.winfo_width()-(x1-x0)}x{y1-y0}+{root.winfo_x()-(x0-x1)}+{root.winfo_y()}")

def right_top_resizing(event):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry(f"{x1-x0}x{root.winfo_height()-(y1-y0)}+{root.winfo_x()}+{root.winfo_y()+(y1-y0)}")
    title_bar.config(height=25)

# Getting coordinates for resizing
def clicked(event):
    x_cor, y_cor = event.x_root-root.winfo_x(),event.y_root-root.winfo_y()
    if root.winfo_width()-5<=x_cor<=root.winfo_width() and not(root.winfo_height()-5<=y_cor<=root.winfo_height() or 0<=y_cor<=5):
        root.bind('<B1-Motion>',right_resizing)
    elif 0<=x_cor<=5 and not(root.winfo_height()-5<=y_cor<=root.winfo_height() or 0<=y_cor<=5):
        root.bind('<B1-Motion>',left_resizing)
    elif root.winfo_height()-5<=y_cor<=root.winfo_height() and not(root.winfo_width()-5<=x_cor<=root.winfo_width() or 0<=x_cor<=5):
        root.bind('<B1-Motion>',bottom_resizing) 
    elif 0<=y_cor<=5 and not(root.winfo_width()-5<=x_cor<=root.winfo_width() or 0<=x_cor<=5):
        root.bind('<B1-Motion>',top_resizing)
    elif root.winfo_width()-5<=x_cor<=root.winfo_width() and root.winfo_height()-5<=y_cor<=root.winfo_height():
        root.bind('<B1-Motion>',right_bottom_resizing)
    elif 0<=x_cor<=5 and 0<=y_cor<=5:
        root.bind('<B1-Motion>',left_top_resizing)
    elif root.winfo_width()-4<=x_cor<=root.winfo_width() and 0<=y_cor<=5:
        root.bind('<B1-Motion>',right_top_resizing)
    elif 0<=x_cor<=5 and root.winfo_height()-5<=y_cor<=root.winfo_height():
        root.bind('<B1-Motion>',left_bottom_resizing)
    else:
        root.unbind('<B1-Motion>')

# Changing cursor for resizing cursor when cursor's coordinates same with resizing coordinates
def changing_cursor(event):
    x, y = event.x_root-root.winfo_x(),event.y_root-root.winfo_y()
    if (root.winfo_width()-5<= x <=root.winfo_width() or 0<=x<=5) and not(root.winfo_height()-5<= y <=root.winfo_height() or 0<=y<=5):
        root.config(cursor='sb_h_double_arrow')
    elif (root.winfo_height()-5<= y <=root.winfo_height() or 0<=y<=5) and not(root.winfo_width()-5<= x <=root.winfo_width() or 0<=x<=5):
        root.config(cursor='sb_v_double_arrow')
    elif (root.winfo_width()-5<=x<=root.winfo_width() and root.winfo_height()-5<=y<=root.winfo_height()) or (0<=x<=5 and 0<=y<=5):
        root.config(cursor="size_nw_se")
    elif (root.winfo_width()-5<=x<=root.winfo_width() and 0<=y<=5) or (0<=x<=5 and root.winfo_height()-5<=y<=root.winfo_height()):
        root.config(cursor="size_ne_sw")
    else:
        root.config(cursor='left_ptr')



# root bindings
root.bind('<Motion>',changing_cursor)
root.bind('<Button-1>',clicked)
root.bind('<Configure>',config)
root.mainloop()
