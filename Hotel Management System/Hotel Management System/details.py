

import sys
from tkinter import messagebox
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

import details_support
import sqlite3 as sql
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Bill (root)
    details_support.init(root, top)
    root.mainloop()

w = None
def create_Bill(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Bill(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Bill (w)
    details_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Bill():
    global w
    w.destroy()
    w = None

class Bill:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Arial} -size 22 -weight bold -underline 1"
        font12 = "-family {Times New Roman} -size 12"

        top.geometry("750x750+350+10")
        top.minsize(160, 12)
        top.maxsize(1936, 1067)
        top.resizable(0, 0)
        top.title("Bill Generator")
        top.configure(background="#400080")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lbl1 = tk.Label(top)
        self.lbl1.place(relx=0.147, rely=0.027, height=39, width=549)
        self.lbl1.configure(activebackground="#f9f9f9")
        self.lbl1.configure(activeforeground="black")
        self.lbl1.configure(background="#400080")
        self.lbl1.configure(disabledforeground="#a3a3a3")
        self.lbl1.configure(font=font10)
        self.lbl1.configure(foreground="#ffffff")
        self.lbl1.configure(highlightbackground="#d9d9d9")
        self.lbl1.configure(highlightcolor="black")
        self.lbl1.configure(text='''Customer Detail''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.12, rely=0.144, relheight=0.803, relwidth=0.768)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#721287")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.find = tk.Button(self.Frame1)
        self.find.place(relx=0.347, rely=0.897, height=43, width=156)
        self.find.configure(activebackground="#ececec")
        self.find.configure(activeforeground="#000000")
        self.find.configure(background="#ffffff")
        self.find.configure(disabledforeground="#a3a3a3")
        self.find.configure(font=font12)
        self.find.configure(foreground="#000000")
        self.find.configure(highlightbackground="#d9d9d9")
        self.find.configure(highlightcolor="black")
        self.find.configure(pady="0")
        self.find.configure(text='''Details''')
        self.find.configure(command=self.details)

        self.lblr = tk.Label(self.Frame1)
        self.lblr.place(relx=0.115, rely=0.058, height=35, width=188)
        self.lblr.configure(activebackground="#f9f9f9")
        self.lblr.configure(activeforeground="black")
        self.lblr.configure(background="#721287")
        self.lblr.configure(disabledforeground="#a3a3a3")
        self.lblr.configure(foreground="#ffffff")
        self.lblr.configure(highlightbackground="#d9d9d9")
        self.lblr.configure(highlightcolor="black")
        self.lblr.configure(text='''Enter Room No''')

        self.room = tk.Entry(self.Frame1)
        self.room.place(relx=0.505, rely=0.058,height=30, relwidth=0.267)
        self.room.configure(background="white")
        self.room.configure(borderwidth="5")
        self.room.configure(disabledforeground="#a3a3a3")
        self.room.configure(font="TkFixedFont")
        self.room.configure(foreground="#000000")
        self.room.configure(highlightbackground="#d9d9d9")
        self.room.configure(highlightcolor="black")
        self.room.configure(insertbackground="black")
        self.room.configure(selectbackground="#c4c4c4")
        self.room.configure(selectforeground="black")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.092, rely=0.154, relheight=0.709
                , relwidth=0.839)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.name = tk.Label(self.Frame2)
        self.name.place(relx=0.041, rely=0.117, height=54, width=198)
        self.name.configure(activebackground="#f9f9f9")
        self.name.configure(activeforeground="black")
        self.name.configure(background="#721287")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.name.configure(foreground="#ffffff")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="black")
        self.name.configure(text='''Name''')

        self.days = tk.Label(self.Frame2)
        self.days.place(relx=0.041, rely=0.281, height=54, width=198)
        self.days.configure(activebackground="#f9f9f9")
        self.days.configure(activeforeground="black")
        self.days.configure(background="#721287")
        self.days.configure(disabledforeground="#a3a3a3")
        self.days.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.days.configure(foreground="#ffffff")
        self.days.configure(highlightbackground="#d9d9d9")
        self.days.configure(highlightcolor="black")
        self.days.configure(text='''Stay Days''')

        self.type = tk.Label(self.Frame2)
        self.type.place(relx=0.041, rely=0.445, height=54, width=198)
        self.type.configure(activebackground="#f9f9f9")
        self.type.configure(activeforeground="black")
        self.type.configure(background="#721287")
        self.type.configure(disabledforeground="#a3a3a3")
        self.type.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.type.configure(foreground="#ffffff")
        self.type.configure(highlightbackground="#d9d9d9")
        self.type.configure(highlightcolor="black")
        self.type.configure(text='''Room Type''')

        self.gender = tk.Label(self.Frame2)
        self.gender.place(relx=0.041, rely=0.609, height=54, width=198)
        self.gender.configure(activebackground="#f9f9f9")
        self.gender.configure(activeforeground="black")
        self.gender.configure(background="#721287")
        self.gender.configure(disabledforeground="#a3a3a3")
        self.gender.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.gender.configure(foreground="#ffffff")
        self.gender.configure(highlightbackground="#d9d9d9")
        self.gender.configure(highlightcolor="black")
        self.gender.configure(text='''Geneder''')

        self.contact = tk.Label(self.Frame2)
        self.contact.place(relx=0.041, rely=0.773, height=54, width=198)
        self.contact.configure(activebackground="#f9f9f9")
        self.contact.configure(activeforeground="black")
        self.contact.configure(background="#721287")
        self.contact.configure(disabledforeground="#a3a3a3")
        self.contact.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.contact.configure(foreground="#ffffff")
        self.contact.configure(highlightbackground="#d9d9d9")
        self.contact.configure(highlightcolor="black")
        self.contact.configure(text='''Contact Number''')

        self.lbldays = tk.Label(self.Frame2)
        self.lbldays.place(relx=0.518, rely=0.281, height=54, width=198)
        self.lbldays.configure(activebackground="#f9f9f9")
        self.lbldays.configure(activeforeground="black")
        self.lbldays.configure(background="#721287")
        self.lbldays.configure(disabledforeground="#a3a3a3")
        self.lbldays.configure(foreground="#ffffff")
        self.lbldays.configure(highlightbackground="#d9d9d9")
        self.lbldays.configure(highlightcolor="black")

        self.lbltype = tk.Label(self.Frame2)
        self.lbltype.place(relx=0.518, rely=0.445, height=54, width=198)
        self.lbltype.configure(activebackground="#f9f9f9")
        self.lbltype.configure(activeforeground="black")
        self.lbltype.configure(background="#721287")
        self.lbltype.configure(disabledforeground="#a3a3a3")
        self.lbltype.configure(foreground="#ffffff")
        self.lbltype.configure(highlightbackground="#d9d9d9")
        self.lbltype.configure(highlightcolor="black")

        self.lblgender = tk.Label(self.Frame2)
        self.lblgender.place(relx=0.518, rely=0.609, height=54, width=198)
        self.lblgender.configure(activebackground="#f9f9f9")
        self.lblgender.configure(activeforeground="black")
        self.lblgender.configure(background="#721287")
        self.lblgender.configure(disabledforeground="#a3a3a3")
        self.lblgender.configure(foreground="#ffffff")
        self.lblgender.configure(highlightbackground="#d9d9d9")
        self.lblgender.configure(highlightcolor="black")

        self.lblcontact = tk.Label(self.Frame2)
        self.lblcontact.place(relx=0.518, rely=0.773, height=54, width=198)
        self.lblcontact.configure(activebackground="#f9f9f9")
        self.lblcontact.configure(activeforeground="black")
        self.lblcontact.configure(background="#721287")
        self.lblcontact.configure(disabledforeground="#a3a3a3")
        self.lblcontact.configure(foreground="#ffffff")
        self.lblcontact.configure(highlightbackground="#d9d9d9")
        self.lblcontact.configure(highlightcolor="black")

        self.lblname = tk.Label(self.Frame1)
        self.lblname.place(relx=0.521, rely=0.233, height=54, width=198)
        self.lblname.configure(activebackground="#f9f9f9")
        self.lblname.configure(activeforeground="black")
        self.lblname.configure(background="#721287")
        self.lblname.configure(disabledforeground="#a3a3a3")
        self.lblname.configure(foreground="#ffffff")
        self.lblname.configure(highlightbackground="#d9d9d9")
        self.lblname.configure(highlightcolor="black")

    def details(self):
        roomno=self.room.get()
        cnx = sql.connect('project.sqlite')
        c=cnx.cursor()
        c.execute("""SELECT * FROM data where Room=?""",(roomno,))
        result=c.fetchone()
        if result:
            Name=result[0]
            Contact=result[2]
            Days=result[3]
            Type=result[6]
            Gender=result[4]
            self.lblname.configure(text=Name)
            self.lblcontact.configure(text=Contact)
            self.lblgender.configure(text=Gender)
            self.lbldays.configure(text=Days)
            self.lbltype.configure(text=Type)
            
        else:
            messagebox.showerror("Error","Room is Empty.No guests are accomodate")
            self.lblname.configure(text="")
            self.lblcontact.configure(text="")
            self.lblgender.configure(text="")
            self.lbldays.configure(text="")
            self.lbltype.configure(text="")
        

if __name__ == '__main__':
    vp_start_gui()





