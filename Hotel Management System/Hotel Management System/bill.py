

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

import bill_support
import sqlite3 as sql
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Bill (root)
    bill_support.init(root, top)
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
    bill_support.init(w, top, *args, **kwargs)
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

        top.geometry("700x700+350+10")
        top.minsize(160, 12)
        top.maxsize(1936, 1067)
        top.resizable(0, 0)
        top.title("Bill Generator")
        top.configure(background="#400080")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lblbill = tk.Label(top)
        self.lblbill.place(relx=0.157, rely=0.057, height=36, width=512)
        self.lblbill.configure(activebackground="#f9f9f9")
        self.lblbill.configure(activeforeground="black")
        self.lblbill.configure(background="#400080")
        self.lblbill.configure(disabledforeground="#a3a3a3")
        self.lblbill.configure(font="-family {Times New Roman} -size 18 -weight bold -underline 1")
        self.lblbill.configure(foreground="#ffffff")
        self.lblbill.configure(highlightbackground="#d9d9d9")
        self.lblbill.configure(highlightcolor="black")
        self.lblbill.configure(text='''BILL GENERATOR''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.2, rely=0.171, relheight=0.736, relwidth=0.621)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#721287")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.generate = tk.Button(self.Frame1)
        self.generate.place(relx=0.345, rely=0.893, height=43, width=156)
        self.generate.configure(activebackground="#ececec")
        self.generate.configure(activeforeground="#000000")
        self.generate.configure(background="#ffffff")
        self.generate.configure(disabledforeground="#a3a3a3")
        self.generate.configure(foreground="#000000")
        self.generate.configure(highlightbackground="#d9d9d9")
        self.generate.configure(highlightcolor="black")
        self.generate.configure(pady="0")
        self.generate.configure(text='''Generate Bill''')
        self.generate.configure(command=self.produce_bill)

        self.lblr = tk.Label(self.Frame1)
        self.lblr.place(relx=0.115, rely=0.058, height=30, width=142)
        self.lblr.configure(activebackground="#f9f9f9")
        self.lblr.configure(activeforeground="black")
        self.lblr.configure(background="#721287")
        self.lblr.configure(disabledforeground="#a3a3a3")
        self.lblr.configure(foreground="#ffffff")
        self.lblr.configure(highlightbackground="#d9d9d9")
        self.lblr.configure(highlightcolor="black")
        self.lblr.configure(text='''Enter Room No''')

        self.lbld = tk.Label(self.Frame1)
        self.lbld.place(relx=0.115, rely=0.175, height=36, width=142)
        self.lbld.configure(activebackground="#f9f9f9")
        self.lbld.configure(activeforeground="black")
        self.lbld.configure(background="#721287")
        self.lbld.configure(disabledforeground="#a3a3a3")
        self.lbld.configure(foreground="#ffffff")
        self.lbld.configure(highlightbackground="#d9d9d9")
        self.lbld.configure(highlightcolor="black")
        self.lbld.configure(text='''Stay Days''')

        self.room = tk.Entry(self.Frame1)
        self.room.place(relx=0.506, rely=0.058,height=30, relwidth=0.354)
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

        self.lbldays = tk.Label(self.Frame1)
        self.lbldays.place(relx=0.506, rely=0.175, height=36, width=142)
        self.lbldays.configure(activebackground="#f9f9f9")
        self.lbldays.configure(activeforeground="black")
        self.lbldays.configure(background="#721287")
        self.lbldays.configure(disabledforeground="#a3a3a3")
        self.lbldays.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.lbldays.configure(foreground="#ffffff")
        self.lbldays.configure(highlightbackground="#d9d9d9")
        self.lbldays.configure(highlightcolor="black")
        self.lbldays.configure(text='''none''')

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.161, rely=0.311, relheight=0.165
                , relwidth=0.724)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.rbill = tk.Label(self.Frame2)
        self.rbill.place(relx=0.381, rely=0.118, height=26, width=71)
        self.rbill.configure(activebackground="#f9f9f9")
        self.rbill.configure(activeforeground="black")
        self.rbill.configure(background="#ffffff")
        self.rbill.configure(disabledforeground="#a3a3a3")
        self.rbill.configure(foreground="#000000")
        self.rbill.configure(highlightbackground="#d9d9d9")
        self.rbill.configure(highlightcolor="black")
        self.rbill.configure(text='''Room Bill''')

        self.lblrbill = tk.Label(self.Frame2)
        self.lblrbill.place(relx=0.19, rely=0.588, height=26, width=192)
        self.lblrbill.configure(activebackground="#f9f9f9")
        self.lblrbill.configure(activeforeground="black")
        self.lblrbill.configure(background="#ffffff")
        self.lblrbill.configure(disabledforeground="#a3a3a3")
        self.lblrbill.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.lblrbill.configure(foreground="#000000")
        self.lblrbill.configure(highlightbackground="#d9d9d9")
        self.lblrbill.configure(highlightcolor="black")

        self.Frame2_7 = tk.Frame(self.Frame1)
        self.Frame2_7.place(relx=0.161, rely=0.563, relheight=0.165
                , relwidth=0.724)
        self.Frame2_7.configure(relief='groove')
        self.Frame2_7.configure(borderwidth="2")
        self.Frame2_7.configure(relief="groove")
        self.Frame2_7.configure(background="#ffffff")
        self.Frame2_7.configure(highlightbackground="#c0c0c0")
        self.Frame2_7.configure(highlightcolor="black")

        self.fbill = tk.Label(self.Frame2_7)
        self.fbill.place(relx=0.381, rely=0.118, height=26, width=71)
        self.fbill.configure(activebackground="#f9f9f9")
        self.fbill.configure(activeforeground="black")
        self.fbill.configure(background="#ffffff")
        self.fbill.configure(disabledforeground="#a3a3a3")
        self.fbill.configure(foreground="#000000")
        self.fbill.configure(highlightbackground="#d9d9d9")
        self.fbill.configure(highlightcolor="black")
        self.fbill.configure(text='''Food Bill''')

        self.lblfbill = tk.Label(self.Frame2_7)
        self.lblfbill.place(relx=0.19, rely=0.588, height=26, width=192)
        self.lblfbill.configure(activebackground="#f9f9f9")
        self.lblfbill.configure(activeforeground="black")
        self.lblfbill.configure(background="#ffffff")
        self.lblfbill.configure(disabledforeground="#a3a3a3")
        self.lblfbill.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.lblfbill.configure(foreground="#000000")
        self.lblfbill.configure(highlightbackground="#d9d9d9")
        self.lblfbill.configure(highlightcolor="black")

        self.tbill = tk.Label(self.Frame1)
        self.tbill.place(relx=0.115, rely=0.777, height=36, width=142)
        self.tbill.configure(activebackground="#f9f9f9")
        self.tbill.configure(activeforeground="black")
        self.tbill.configure(background="#721287")
        self.tbill.configure(disabledforeground="#a3a3a3")
        self.tbill.configure(foreground="#ffffff")
        self.tbill.configure(highlightbackground="#d9d9d9")
        self.tbill.configure(highlightcolor="black")
        self.tbill.configure(text='''Total Bill''')

        self.lbltotal = tk.Label(self.Frame1)
        self.lbltotal.place(relx=0.529, rely=0.777, height=36, width=142)
        self.lbltotal.configure(activebackground="#f9f9f9")
        self.lbltotal.configure(activeforeground="black")
        self.lbltotal.configure(background="#721287")
        self.lbltotal.configure(disabledforeground="#a3a3a3")
        self.lbltotal.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.lbltotal.configure(foreground="#ffffff")
        self.lbltotal.configure(highlightbackground="#d9d9d9")
        self.lbltotal.configure(highlightcolor="black")
        self.lbltotal.configure(text='''none''')
        
    def produce_bill(self):
        room=self.room.get()
        cnx = sql.connect('project.sqlite')
        c=cnx.cursor()
        c.execute("""SELECT Days,RoomType,Food,RoomBill FROM data where Room=?""",(room,))
        result=c.fetchone()
        if result:
            days=result[0]
            roomtype=result[1]
            foodbill=result[2]*int(days)
            roombill=result[3]*int(days)
            self.lbldays.configure(text=days)
            self.lblfbill.configure(text=foodbill)
            self.lblrbill.configure(text=roombill)
            totalbill=roombill+foodbill
            self.lbltotal.configure(text=totalbill)
            c.execute("""DELETE FROM data where Room=?""",(room,))
            c.execute("UPDATE room SET Available='0' where RoomNo=?",(room,))
            cnx.commit()
            c.close()
            
        else:
            messagebox.showerror("Error","Selected Room is empty and No guest accomodated in room") 

if __name__ == '__main__':
    vp_start_gui()





