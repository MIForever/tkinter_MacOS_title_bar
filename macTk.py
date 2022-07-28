from tkinter import *

class MacTk(Tk):
    def __init__(self):
        Tk.__init__(self=self)
        self.geometry('500x400+100+100')
        self.minsize(width='200',height='150')
        self.overrideredirect(True)

        self.fulled_screen = 0  #Variable for cheking window is full sized or not

        self._offsetx = 0
        self._offsety = 0

        # Title bar (bar where located on top side)
        self.title_bar = Label(self,bg='gray25')
        self.title_bar.place(x=0,y=0,height=25,width=self.winfo_width())
        self.title_bar.bind('<Button-1>',self.clickwin)
        self.title_bar.bind('<B1-Motion>',self.dragwin)


        # Exit button
        self.exit_btn_img = PhotoImage(file='photos/red.png')
        self.exit_btn = Button(self.title_bar,image=self.exit_btn_img,bd=0,bg='gray25',activebackground='gray25',command=self.destroy)
        self.exit_btn.place(x=475,y=5,height=15,width=15)


        # Maximize button (changes root size to full screen)
        self.maximize_img = PhotoImage(file='photos/yellow.png')
        self.maximize_btn = Button(self.title_bar,image=self.maximize_img,bd=0,bg='gray25',activebackground='gray25',command=self.full_screen)
        self.maximize_btn.place(x=450,y=5,height=15,width=15)


        # Minimize button (hiding)
        self.minimize_img = PhotoImage(file='photos/green.png')
        self.minimize_btn = Button(self.title_bar,image=self.minimize_img,bd=0,bg='gray25',activebackground='gray25',command=self.hide_screen)
        self.minimize_btn.place(x=425,y=5,height=15,width=15)

        # root bindings
        self.bind('<Motion>',self.changing_cursor)
        self.bind('<Button-1>',self.clicked)
        self.bind('<Configure>',self._config)


    def _config(self,e):
        if self.wm_state() == 'normal':
            self.overrideredirect(True)
        self.exit_btn.config(image=self.exit_btn_img)
        self.maximize_btn.config(image=self.maximize_img)
        self.minimize_btn.config(image=self.minimize_img)
        self.exit_btn.place(x=self.winfo_width()-25,y=4)
        self.maximize_btn.place(x=self.winfo_width()-50,y=5)
        self.minimize_btn.place(x=self.winfo_width()-75,y=5)
        self.title_bar.place(width=self.winfo_width()+50)

    def full_screen(self):
        if self.fulled_screen==0:
            self.fulled_screen=1
            self.state('zoomed')
        elif self.fulled_screen==1:
            self.state('normal')
            self.fulled_screen=0

    def hide_screen(self):
        self.overrideredirect(False)
        self.iconify()
        self.screen_hidden=1

    def dragwin(self,event):
        x = self.title_bar.winfo_pointerx() - self.title_bar._offsetx
        y = self.title_bar.winfo_pointery() - self.title_bar._offsety
        self.geometry(f'+{x}+{y}')

    # Gettinng coordinates of title bar for dragging
    def clickwin(self,event):
        self.title_bar._offsetx = event.x
        self.title_bar._offsety = event.y


    #SIDE RESIZING FUNCTIONS
    def right_resizing(self,event):
        x1 = self.winfo_pointerx()
        x0 = self.winfo_rootx()
        self.geometry("%sx%s" % ((x1-x0),self.winfo_height()))


    def left_resizing(self,event):
        x1 = self.winfo_pointerx()
        x0 = self.winfo_rootx()
        self.geometry(f"{self.winfo_width()-(x1-x0)}x{self.winfo_height()}+{self.winfo_x()+(x1-x0)}+{self.winfo_y()}")

    def top_resizing(self,event):
        y1 = self.winfo_pointery()
        y0 = self.winfo_rooty()
        self.geometry(f"{self.winfo_width()}x{self.winfo_height()-(y1-y0)}+{self.winfo_x()}+{self.winfo_y()+(y1-y0)}")
        self.title_bar.config(height=25)

    def bottom_resizing(self,event):
        y1 = self.winfo_pointery()
        y0 = self.winfo_rooty()
        self.geometry(f"{self.winfo_width()}x{y1-y0}")

    def right_bottom_resizing(self,event):
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry(f"{x1-x0}x{y1-y0}")

    def left_top_resizing(self,event):
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry(f"{self.winfo_width()-(x1-x0)}x{self.winfo_height()-(y1-y0)}+{self.winfo_x()+(x1-x0)}+{self.winfo_y()+(y1-y0)}")
        self.title_bar.config(height=25)

    def left_bottom_resizing(self,event):
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry(f"{self.winfo_width()-(x1-x0)}x{y1-y0}+{self.winfo_x()-(x0-x1)}+{self.winfo_y()}")

    def right_top_resizing(self,event):
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry(f"{x1-x0}x{self.winfo_height()-(y1-y0)}+{self.winfo_x()}+{self.winfo_y()+(y1-y0)}")
        self.title_bar.config(height=25)

    # Getting coordinates for resizing
    def clicked(self,event):
        x_cor, y_cor = event.x_root-self.winfo_x(),event.y_root-self.winfo_y()
        if self.winfo_width()-5<=x_cor<=self.winfo_width() and not(self.winfo_height()-5<=y_cor<=self.winfo_height() or 0<=y_cor<=5):
            self.bind('<B1-Motion>',self.right_resizing)
        elif 0<=x_cor<=5 and not(self.winfo_height()-5<=y_cor<=self.winfo_height() or 0<=y_cor<=5):
            self.bind('<B1-Motion>',self.left_resizing)
        elif self.winfo_height()-5<=y_cor<=self.winfo_height() and not(self.winfo_width()-5<=x_cor<=self.winfo_width() or 0<=x_cor<=5):
            self.bind('<B1-Motion>',self.bottom_resizing) 
        elif 0<=y_cor<=5 and not(self.winfo_width()-5<=x_cor<=self.winfo_width() or 0<=x_cor<=5):
            self.bind('<B1-Motion>',self.top_resizing)
        elif self.winfo_width()-5<=x_cor<=self.winfo_width() and self.winfo_height()-5<=y_cor<=self.winfo_height():
            self.bind('<B1-Motion>',self.right_bottom_resizing)
        elif 0<=x_cor<=5 and 0<=y_cor<=5:
            self.bind('<B1-Motion>',self.left_top_resizing)
        elif self.winfo_width()-4<=x_cor<=self.winfo_width() and 0<=y_cor<=5:
            self.bind('<B1-Motion>',self.right_top_resizing)
        elif 0<=x_cor<=5 and self.winfo_height()-5<=y_cor<=self.winfo_height():
            self.bind('<B1-Motion>',self.left_bottom_resizing)
        else:
            self.unbind('<B1-Motion>')

    # Changing cursor for resizing cursor when cursor's coordinates same with resizing coordinates
    def changing_cursor(self,event):
        x, y = event.x_root-self.winfo_x(),event.y_root-self.winfo_y()
        if (self.winfo_width()-5<= x <=self.winfo_width() or 0<=x<=5) and not(self.winfo_height()-5<= y <=self.winfo_height() or 0<=y<=5):
            self.config(cursor='sb_h_double_arrow')
        elif (self.winfo_height()-5<= y <=self.winfo_height() or 0<=y<=5) and not(self.winfo_width()-5<= x <=self.winfo_width() or 0<=x<=5):
            self.config(cursor='sb_v_double_arrow')
        elif (self.winfo_width()-5<=x<=self.winfo_width() and self.winfo_height()-5<=y<=self.winfo_height()) or (0<=x<=5 and 0<=y<=5):
            self.config(cursor="size_nw_se")
        elif (self.winfo_width()-5<=x<=self.winfo_width() and 0<=y<=5) or (0<=x<=5 and self.winfo_height()-5<=y<=self.winfo_height()):
            self.config(cursor="size_ne_sw")
        else:
            self.config(cursor='left_ptr')