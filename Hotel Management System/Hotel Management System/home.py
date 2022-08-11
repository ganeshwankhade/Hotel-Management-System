

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import home_support
import os
from subprocess import call

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    home_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    home_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def book(self):
        call(["python", "register.py"])

    def roomdetails(self):
        call(["python", "room.py"])

    def food(self):
        call(["python", "menu.py"])

    def guest(self):
        call(["python", "details.py"])

    def bill(self):
        call(["python", "Bill.py"])

    def ext(self):
        os._exit(0) 
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("872x700+350+10")
        top.minsize(160, 12)
        top.maxsize(1936, 1067)
        top.resizable(0, 0)
        top.title("Home Page")
        top.configure(background="#721287")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.framemain = tk.Frame(top)
        self.framemain.place(relx=0.148, rely=0.14, relheight=0.779
                , relwidth=0.717)
        self.framemain.configure(relief='groove')
        self.framemain.configure(borderwidth="10")
        self.framemain.configure(relief="groove")
        self.framemain.configure(background="#b3009d")
        self.framemain.configure(highlightbackground="#d9d9d9")
        self.framemain.configure(highlightcolor="black")

        self.btnbook = tk.Button(self.framemain)
        self.btnbook.place(relx=0.193, rely=0.069, height=63, width=396)
        self.btnbook.configure(activebackground="#ececec")
        self.btnbook.configure(activeforeground="#620373")
        self.btnbook.configure(background="#d973cc")
        self.btnbook.configure(borderwidth="10")
        self.btnbook.configure(disabledforeground="#a3a3a3")
        self.btnbook.configure(font="-family {Segoe UI} -size 14")
        self.btnbook.configure(foreground="#000000")
        self.btnbook.configure(highlightbackground="#d9d9d9")
        self.btnbook.configure(highlightcolor="black")
        self.btnbook.configure(pady="0")
        self.btnbook.configure(text='''Book Room''')
        self.btnbook.configure(command=self.book)

        self.btnroomdetails = tk.Button(self.framemain)
        self.btnroomdetails.place(relx=0.193, rely=0.22, height=63, width=396)
        self.btnroomdetails.configure(activebackground="#ececec")
        self.btnroomdetails.configure(activeforeground="#000000")
        self.btnroomdetails.configure(background="#d973cc")
        self.btnroomdetails.configure(borderwidth="10")
        self.btnroomdetails.configure(disabledforeground="#a3a3a3")
        self.btnroomdetails.configure(font="-family {Segoe UI} -size 14")
        self.btnroomdetails.configure(foreground="#000000")
        self.btnroomdetails.configure(highlightbackground="#d9d9d9")
        self.btnroomdetails.configure(highlightcolor="black")
        self.btnroomdetails.configure(pady="0")
        self.btnroomdetails.configure(text='''Check Room Details''')
        self.btnroomdetails.configure(command=self.roomdetails)

        self.btnfood = tk.Button(self.framemain)
        self.btnfood.place(relx=0.193, rely=0.372, height=63, width=396)
        self.btnfood.configure(activebackground="#ececec")
        self.btnfood.configure(activeforeground="#000000")
        self.btnfood.configure(background="#d973cc")
        self.btnfood.configure(borderwidth="10")
        self.btnfood.configure(disabledforeground="#a3a3a3")
        self.btnfood.configure(font="-family {Segoe UI} -size 14")
        self.btnfood.configure(foreground="#000000")
        self.btnfood.configure(highlightbackground="#d9d9d9")
        self.btnfood.configure(highlightcolor="black")
        self.btnfood.configure(pady="0")
        self.btnfood.configure(text='''Order Food''')
        self.btnfood.configure(command=self.food)

        self.btnguest = tk.Button(self.framemain)
        self.btnguest.place(relx=0.193, rely=0.524, height=63, width=396)
        self.btnguest.configure(activebackground="#ececec")
        self.btnguest.configure(activeforeground="#000000")
        self.btnguest.configure(background="#d973cc")
        self.btnguest.configure(borderwidth="10")
        self.btnguest.configure(disabledforeground="#a3a3a3")
        self.btnguest.configure(font="-family {Segoe UI} -size 14")
        self.btnguest.configure(foreground="#000000")
        self.btnguest.configure(highlightbackground="#d9d9d9")
        self.btnguest.configure(highlightcolor="black")
        self.btnguest.configure(pady="0")
        self.btnguest.configure(text='''Customer Details''')
        self.btnguest.configure(command=self.guest)

        self.btnbill = tk.Button(self.framemain)
        self.btnbill.place(relx=0.193, rely=0.674, height=63, width=396)
        self.btnbill.configure(activebackground="#ececec")
        self.btnbill.configure(activeforeground="#000000")
        self.btnbill.configure(background="#d973cc")
        self.btnbill.configure(borderwidth="10")
        self.btnbill.configure(disabledforeground="#a3a3a3")
        self.btnbill.configure(font="-family {Segoe UI} -size 14")
        self.btnbill.configure(foreground="#000000")
        self.btnbill.configure(highlightbackground="#d9d9d9")
        self.btnbill.configure(highlightcolor="black")
        self.btnbill.configure(pady="0")
        self.btnbill.configure(text='''Generate Bill''')
        self.btnbill.configure(command=self.bill)

        self.exit = tk.Button(self.framemain)
        self.exit.place(relx=0.193, rely=0.821, height=63, width=396)
        self.exit.configure(activebackground="#ececec")
        self.exit.configure(activeforeground="#000000")
        self.exit.configure(background="#d973cc")
        self.exit.configure(borderwidth="10")
        self.exit.configure(disabledforeground="#a3a3a3")
        self.exit.configure(font="-family {Segoe UI} -size 14")
        self.exit.configure(foreground="#000000")
        self.exit.configure(highlightbackground="#d9d9d9")
        self.exit.configure(highlightcolor="black")
        self.exit.configure(pady="0")
        self.exit.configure(text='''Exit''')
        self.exit.configure(command=self.ext)

        self.frametitle = tk.Frame(top)
        self.frametitle.place(relx=0.023, rely=0.032, relheight=0.081
                , relwidth=0.945)
        self.frametitle.configure(relief='groove')
        self.frametitle.configure(borderwidth="5")
        self.frametitle.configure(relief="groove")
        self.frametitle.configure(background="#b3009d")
        self.frametitle.configure(highlightbackground="#d9d9d9")
        self.frametitle.configure(highlightcolor="black")

        self.lblhead = tk.Label(self.frametitle)
        self.lblhead.place(relx=0.012, rely=0.129, height=53, width=802)
        self.lblhead.configure(activebackground="#f9f9f9")
        self.lblhead.configure(activeforeground="black")
        self.lblhead.configure(background="#d973cc")
        self.lblhead.configure(disabledforeground="#a3a3a3")
        self.lblhead.configure(font="-family {Arial} -size 18 -weight bold -underline 1")
        self.lblhead.configure(foreground="#000000")
        self.lblhead.configure(highlightbackground="#d9d9d9")
        self.lblhead.configure(highlightcolor="black")
        self.lblhead.configure(text='''====WELCOME TO HOTEL MEGASTAR====''')

if __name__ == '__main__':
    vp_start_gui()





