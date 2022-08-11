

import sys
import os
import pickle
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

import register_support
import sqlite3 as sql

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    register_support.set_Tk_var()
    top = Toplevel1 (root)
    register_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    register_support.set_Tk_var()
    top = Toplevel1 (w)
    register_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def data(self):
        name=self.name.get()
        address=self.Address.get("1.0","end")
        contact=self.contact.get()
        stay=self.days.get()
        gend=register_support.gender.get()
        roomtype=register_support.Type.get()
        cnx = sql.connect('project.sqlite')
        c=cnx.cursor()
        c.execute("SELECT RoomNo,Rate FROM room where Available='0' and Type=?",(roomtype,))
        result=c.fetchall()
        if result:
            for row in result:
                roomno=row[0]
                rate=row[1]
            tup=(name,address,int(contact),int(stay),gend,roomno,roomtype,int(rate))
            c.execute("INSERT INTO `data`(`Name`, `Address`, `Contact`, `Days`, `Gender`, `Room`, `RoomType`,`RoomBill`) VALUES (?,?,?,?,?,?,?,?)",tup)
            c.execute("UPDATE room SET Available='1' where RoomNo=?",(roomno,))
            cnx.commit()
            c.close()
            msg="Welcome to MEGASTAR HOTEL.Your Hotel Room Number is "+roomno
            messagebox.showinfo("Successful",msg)
        else:
            messagebox.showerror("Error","All rooms of selected type are full.Please select another type")
            

        
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
        top.title("Book Room")
        top.configure(background="#c109e8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lblreg = tk.Label(top)
        self.lblreg.place(relx=0.08, rely=0.029, height=56, width=730)
        self.lblreg.configure(activebackground="#f9f9f9")
        self.lblreg.configure(activeforeground="black")
        self.lblreg.configure(background="#c109e8")
        self.lblreg.configure(borderwidth="10")
        self.lblreg.configure(disabledforeground="#a3a3a3")
        self.lblreg.configure(font="-family {Times New Roman} -size 22 -weight bold -underline 1")
        self.lblreg.configure(foreground="#ffffff")
        self.lblreg.configure(highlightbackground="#d9d9d9")
        self.lblreg.configure(highlightcolor="black")
        self.lblreg.configure(text='''=====Register Room=====''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.149, rely=0.143, relheight=0.72, relwidth=0.705)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#721287")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.name = tk.Entry(self.Frame1)
        self.name.place(relx=0.293, rely=0.04,height=30, relwidth=0.641)
        self.name.configure(background="white")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="TkFixedFont")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="black")
        self.name.configure(insertbackground="black")
        self.name.configure(selectbackground="#c4c4c4")
        self.name.configure(selectforeground="black")

        self.lblname = tk.Label(self.Frame1)
        self.lblname.place(relx=0.065, rely=0.04, height=26, width=92)
        self.lblname.configure(activebackground="#f9f9f9")
        self.lblname.configure(activeforeground="black")
        self.lblname.configure(background="#721287")
        self.lblname.configure(disabledforeground="#a3a3a3")
        self.lblname.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.lblname.configure(foreground="#ffffff")
        self.lblname.configure(highlightbackground="#d9d9d9")
        self.lblname.configure(highlightcolor="black")
        self.lblname.configure(text='''Name''')

        self.lbladdress = tk.Label(self.Frame1)
        self.lbladdress.place(relx=0.065, rely=0.198, height=26, width=92)
        self.lbladdress.configure(activebackground="#f9f9f9")
        self.lbladdress.configure(activeforeground="black")
        self.lbladdress.configure(background="#721287")
        self.lbladdress.configure(disabledforeground="#a3a3a3")
        self.lbladdress.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.lbladdress.configure(foreground="#ffffff")
        self.lbladdress.configure(highlightbackground="#d9d9d9")
        self.lbladdress.configure(highlightcolor="black")
        self.lbladdress.configure(text='''Address''')

        self.lblmobile = tk.Label(self.Frame1)
        self.lblmobile.place(relx=0.065, rely=0.357, height=26, width=92)
        self.lblmobile.configure(activebackground="#f9f9f9")
        self.lblmobile.configure(activeforeground="black")
        self.lblmobile.configure(background="#721287")
        self.lblmobile.configure(disabledforeground="#a3a3a3")
        self.lblmobile.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.lblmobile.configure(foreground="#ffffff")
        self.lblmobile.configure(highlightbackground="#d9d9d9")
        self.lblmobile.configure(highlightcolor="black")
        self.lblmobile.configure(text='''Contact''')

        self.lbldays = tk.Label(self.Frame1)
        self.lbldays.place(relx=0.065, rely=0.496, height=26, width=92)
        self.lbldays.configure(activebackground="#f9f9f9")
        self.lbldays.configure(activeforeground="black")
        self.lbldays.configure(background="#721287")
        self.lbldays.configure(disabledforeground="#a3a3a3")
        self.lbldays.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.lbldays.configure(foreground="#ffffff")
        self.lbldays.configure(highlightbackground="#d9d9d9")
        self.lbldays.configure(highlightcolor="black")
        self.lbldays.configure(text='''Stay Days''')

        self.Address = tk.Text(self.Frame1)
        self.Address.place(relx=0.293, rely=0.179, relheight=0.107
                , relwidth=0.641)
        self.Address.configure(background="white")
        self.Address.configure(font="TkTextFont")
        self.Address.configure(foreground="black")
        self.Address.configure(highlightbackground="#d9d9d9")
        self.Address.configure(highlightcolor="black")
        self.Address.configure(insertbackground="black")
        self.Address.configure(selectbackground="#c4c4c4")
        self.Address.configure(selectforeground="black")
        self.Address.configure(wrap="word")

        self.contact = tk.Entry(self.Frame1)
        self.contact.place(relx=0.293, rely=0.357,height=30, relwidth=0.641)
        self.contact.configure(background="white")
        self.contact.configure(disabledforeground="#a3a3a3")
        self.contact.configure(font="TkFixedFont")
        self.contact.configure(foreground="#000000")
        self.contact.configure(highlightbackground="#d9d9d9")
        self.contact.configure(highlightcolor="black")
        self.contact.configure(insertbackground="black")
        self.contact.configure(selectbackground="#c4c4c4")
        self.contact.configure(selectforeground="black")

        self.days = tk.Entry(self.Frame1)
        self.days.place(relx=0.293, rely=0.496,height=30, relwidth=0.641)
        self.days.configure(background="white")
        self.days.configure(disabledforeground="#a3a3a3")
        self.days.configure(font="TkFixedFont")
        self.days.configure(foreground="#000000")
        self.days.configure(highlightbackground="#d9d9d9")
        self.days.configure(highlightcolor="black")
        self.days.configure(insertbackground="black")
        self.days.configure(selectbackground="#c4c4c4")
        self.days.configure(selectforeground="black")

        self.lblgender = tk.Label(self.Frame1)
        self.lblgender.place(relx=0.065, rely=0.635, height=26, width=93)
        self.lblgender.configure(activebackground="#f9f9f9")
        self.lblgender.configure(activeforeground="black")
        self.lblgender.configure(background="#721287")
        self.lblgender.configure(disabledforeground="#a3a3a3")
        self.lblgender.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.lblgender.configure(foreground="#ffffff")
        self.lblgender.configure(highlightbackground="#d9d9d9")
        self.lblgender.configure(highlightcolor="black")
        self.lblgender.configure(text='''Gender''')

        self.male = tk.Radiobutton(self.Frame1)
        self.male.place(relx=0.293, rely=0.635, relheight=0.062, relwidth=0.192)
        self.male.configure(activebackground="#ececec")
        self.male.configure(activeforeground="#000000")
        self.male.configure(background="#721287")
        self.male.configure(disabledforeground="#a3a3a3")
        self.male.configure(font="-family {Segoe UI} -size 10")
        self.male.configure(foreground="#000000")
        self.male.configure(highlightbackground="#d9d9d9")
        self.male.configure(highlightcolor="black")
        self.male.configure(justify='left')
        self.male.configure(text='''Male''')
        self.male.configure(value="male")
        self.male.configure(variable=register_support.gender)

        self.female = tk.Radiobutton(self.Frame1)
        self.female.place(relx=0.618, rely=0.635, relheight=0.062
                , relwidth=0.192)
        self.female.configure(activebackground="#ececec")
        self.female.configure(activeforeground="#000000")
        self.female.configure(background="#721287")
        self.female.configure(disabledforeground="#a3a3a3")
        self.female.configure(font="-family {Segoe UI} -size 10")
        self.female.configure(foreground="#000000")
        self.female.configure(highlightbackground="#d9d9d9")
        self.female.configure(highlightcolor="black")
        self.female.configure(justify='left')
        self.female.configure(text='''Female''')
        self.female.configure(value="female")
        self.female.configure(variable=register_support.gender)

        self.lblroomtype = tk.Label(self.Frame1)
        self.lblroomtype.place(relx=0.049, rely=0.813, height=26, width=133)
        self.lblroomtype.configure(activebackground="#f9f9f9")
        self.lblroomtype.configure(activeforeground="black")
        self.lblroomtype.configure(background="#721287")
        self.lblroomtype.configure(disabledforeground="#a3a3a3")
        self.lblroomtype.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.lblroomtype.configure(foreground="#ffffff")
        self.lblroomtype.configure(highlightbackground="#d9d9d9")
        self.lblroomtype.configure(highlightcolor="black")
        self.lblroomtype.configure(text='''Type of Room''')

        self.kingbed = tk.Radiobutton(self.Frame1)
        self.kingbed.place(relx=0.293, rely=0.774, relheight=0.062
                , relwidth=0.192)
        self.kingbed.configure(activebackground="#ececec")
        self.kingbed.configure(activeforeground="#000000")
        self.kingbed.configure(background="#721287")
        self.kingbed.configure(disabledforeground="#a3a3a3")
        self.kingbed.configure(font="-family {Segoe UI} -size 10")
        self.kingbed.configure(foreground="#000000")
        self.kingbed.configure(highlightbackground="#d9d9d9")
        self.kingbed.configure(highlightcolor="#000000")
        self.kingbed.configure(justify='left')
        self.kingbed.configure(text='''King Bed''')
        self.kingbed.configure(value="King")
        self.kingbed.configure(variable=register_support.Type)

        self.ac = tk.Radiobutton(self.Frame1)
        self.ac.place(relx=0.618, rely=0.774, relheight=0.062, relwidth=0.192)
        self.ac.configure(activebackground="#ececec")
        self.ac.configure(activeforeground="#000000")
        self.ac.configure(background="#721287")
        self.ac.configure(disabledforeground="#a3a3a3")
        self.ac.configure(font="-family {Segoe UI} -size 10")
        self.ac.configure(foreground="#000000")
        self.ac.configure(highlightbackground="#d9d9d9")
        self.ac.configure(highlightcolor="black")
        self.ac.configure(justify='left')
        self.ac.configure(text='''AC Room''')
        self.ac.configure(value="Ac")
        self.ac.configure(variable=register_support.Type)

        self.Premium = tk.Radiobutton(self.Frame1)
        self.Premium.place(relx=0.293, rely=0.853, relheight=0.062
                , relwidth=0.192)
        self.Premium.configure(activebackground="#ececec")
        self.Premium.configure(activeforeground="#000000")
        self.Premium.configure(background="#721287")
        self.Premium.configure(disabledforeground="#a3a3a3")
        self.Premium.configure(font="-family {Segoe UI} -size 10")
        self.Premium.configure(foreground="#000000")
        self.Premium.configure(highlightbackground="#d9d9d9")
        self.Premium.configure(highlightcolor="black")
        self.Premium.configure(justify='left')
        self.Premium.configure(text='''Premium''')
        self.Premium.configure(value="Premium")
        self.Premium.configure(variable=register_support.Type)

        self.supreme = tk.Radiobutton(self.Frame1)
        self.supreme.place(relx=0.618, rely=0.853, relheight=0.062
                , relwidth=0.192)
        self.supreme.configure(activebackground="#ececec")
        self.supreme.configure(activeforeground="#000000")
        self.supreme.configure(background="#721287")
        self.supreme.configure(disabledforeground="#a3a3a3")
        self.supreme.configure(font="-family {Segoe UI} -size 10")
        self.supreme.configure(foreground="#000000")
        self.supreme.configure(highlightbackground="#d9d9d9")
        self.supreme.configure(highlightcolor="black")
        self.supreme.configure(justify='left')
        self.supreme.configure(text='''Supreme''')
        self.supreme.configure(value="Supreme")
        self.supreme.configure(variable=register_support.Type)

        self.btnreg = tk.Button(top)
        self.btnreg.place(relx=0.39, rely=0.914, height=43, width=206)
        self.btnreg.configure(activebackground="#ececec")
        self.btnreg.configure(activeforeground="#000000")
        self.btnreg.configure(background="#721287")
        self.btnreg.configure(disabledforeground="#a3a3a3")
        self.btnreg.configure(foreground="#000000")
        self.btnreg.configure(highlightbackground="#d9d9d9")
        self.btnreg.configure(highlightcolor="black")
        self.btnreg.configure(pady="0")
        self.btnreg.configure(text='''Register''')
        self.btnreg.configure(command=self.data)
        
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





