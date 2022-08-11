

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

import menu_support
import sqlite3 as sql
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    menu_support.set_Tk_var()
    top = Toplevel1 (root)
    menu_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    menu_support.set_Tk_var()
    top = Toplevel1 (w)
    menu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def place_order(self):
        room=self.room.get()
        cusine=menu_support.cusine.get()
        meal=menu_support.meal.get()
        cnx = sql.connect('project.sqlite')
        c=cnx.cursor()
        tup=(cusine,meal)
        c.execute("""SELECT * FROM food where FoodVariety=:f and Quantity=:q""",{'f':cusine,'q':meal})
        result=c.fetchall()
        if result:
            for row in result:
                price=row[2]
            c.execute("UPDATE data SET FoodVariety=?,Quantity=?,Food=? where Room=?",(cusine,int(meal),int(price),room,))
            cnx.commit()
            c.close()
            messagebox.showinfo("Successful","Thank you for Ordering Meal.Enjoy the Meal.")
        else:
            messagebox.showerror("Error","Food is not prepared till now.")    



    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI Black} -size 14 -weight bold"

        top.geometry("872x700+350+10")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Order Food")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#400080")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#ffffff")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.092, rely=0.185, relheight=0.631
                , relwidth=0.352)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="8")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#81b7e3")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.indian = tk.Radiobutton(self.Frame2)
        self.indian.place(relx=0.326, rely=0.336, relheight=0.065
                , relwidth=0.274)
        self.indian.configure(activebackground="#ececec")
        self.indian.configure(activeforeground="#000000")
        self.indian.configure(background="#81b7e3")
        self.indian.configure(disabledforeground="#a3a3a3")
        self.indian.configure(foreground="#000000")
        self.indian.configure(highlightbackground="#d9d9d9")
        self.indian.configure(highlightcolor="black")
        self.indian.configure(justify='left')
        self.indian.configure(text='''INDIAN''')
        self.indian.configure(value="indian")
        self.indian.configure(variable=menu_support.cusine)

        self.mexican = tk.Radiobutton(self.Frame2)
        self.mexican.place(relx=0.326, rely=0.472, relheight=0.065
                , relwidth=0.29)
        self.mexican.configure(activebackground="#ececec")
        self.mexican.configure(activeforeground="#000000")
        self.mexican.configure(background="#81b7e3")
        self.mexican.configure(disabledforeground="#a3a3a3")
        self.mexican.configure(foreground="#000000")
        self.mexican.configure(highlightbackground="#d9d9d9")
        self.mexican.configure(highlightcolor="black")
        self.mexican.configure(justify='left')
        self.mexican.configure(text='''MEXICAN''')
        self.mexican.configure(value="mexican")
        self.mexican.configure(variable=menu_support.cusine)

        self.italian = tk.Radiobutton(self.Frame2)
        self.italian.place(relx=0.326, rely=0.607, relheight=0.065
                , relwidth=0.274)
        self.italian.configure(activebackground="#ececec")
        self.italian.configure(activeforeground="#000000")
        self.italian.configure(background="#81b7e3")
        self.italian.configure(disabledforeground="#a3a3a3")
        self.italian.configure(foreground="#000000")
        self.italian.configure(highlightbackground="#d9d9d9")
        self.italian.configure(highlightcolor="black")
        self.italian.configure(justify='left')
        self.italian.configure(text='''ITALIAN''')
        self.italian.configure(value="italian")
        self.italian.configure(variable=menu_support.cusine)

        self.thai = tk.Radiobutton(self.Frame2)
        self.thai.place(relx=0.326, rely=0.743, relheight=0.065, relwidth=0.195)
        self.thai.configure(activebackground="#ececec")
        self.thai.configure(activeforeground="#000000")
        self.thai.configure(background="#81b7e3")
        self.thai.configure(disabledforeground="#a3a3a3")
        self.thai.configure(foreground="#000000")
        self.thai.configure(highlightbackground="#d9d9d9")
        self.thai.configure(highlightcolor="black")
        self.thai.configure(justify='left')
        self.thai.configure(text='''THAI''')
        self.thai.configure(value="thai")
        self.thai.configure(variable=menu_support.cusine)

        self.Frame4 = tk.Frame(self.Frame2)
        self.Frame4.place(relx=0.14, rely=0.104, relheight=0.151, relwidth=0.717)

        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="4")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#721287")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame4)
        self.Label1.place(relx=0.227, rely=0.149, height=41, width=132)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#721287")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''CUISINE''')

        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.55, rely=0.185, relheight=0.634, relwidth=0.352)

        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="8")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#81b7e3")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.dinner = tk.Radiobutton(self.Frame3)
        self.dinner.place(relx=0.326, rely=0.472, relheight=0.065
                , relwidth=0.274)
        self.dinner.configure(activebackground="#ececec")
        self.dinner.configure(activeforeground="#000000")
        self.dinner.configure(background="#81b7e3")
        self.dinner.configure(disabledforeground="#a3a3a3")
        self.dinner.configure(foreground="#000000")
        self.dinner.configure(highlightbackground="#d9d9d9")
        self.dinner.configure(highlightcolor="black")
        self.dinner.configure(justify='left')
        self.dinner.configure(text='''DINNER''')
        self.dinner.configure(value="2")
        self.dinner.configure(variable=menu_support.meal)

        self.landd = tk.Radiobutton(self.Frame3)
        self.landd.place(relx=0.293, rely=0.607, relheight=0.065, relwidth=0.518)

        self.landd.configure(activebackground="#ececec")
        self.landd.configure(activeforeground="#000000")
        self.landd.configure(background="#81b7e3")
        self.landd.configure(disabledforeground="#a3a3a3")
        self.landd.configure(foreground="#000000")
        self.landd.configure(highlightbackground="#d9d9d9")
        self.landd.configure(highlightcolor="black")
        self.landd.configure(justify='left')
        self.landd.configure(text='''LUNCH+DINNER''')
        self.landd.configure(value="3")
        self.landd.configure(variable=menu_support.meal)

        self.lunch = tk.Radiobutton(self.Frame3)
        self.lunch.place(relx=0.293, rely=0.315, relheight=0.065, relwidth=0.329)

        self.lunch.configure(activebackground="#ececec")
        self.lunch.configure(activeforeground="#000000")
        self.lunch.configure(background="#81b7e3")
        self.lunch.configure(disabledforeground="#a3a3a3")
        self.lunch.configure(foreground="#000000")
        self.lunch.configure(highlightbackground="#d9d9d9")
        self.lunch.configure(highlightcolor="black")
        self.lunch.configure(justify='left')
        self.lunch.configure(text='''LUNCH''')
        self.lunch.configure(value="1")
        self.lunch.configure(variable=menu_support.meal)

        self.combo = tk.Radiobutton(self.Frame3)
        self.combo.place(relx=0.326, rely=0.742, relheight=0.085, relwidth=0.29)
        self.combo.configure(activebackground="#ececec")
        self.combo.configure(activeforeground="#000000")
        self.combo.configure(background="#81b7e3")
        self.combo.configure(disabledforeground="#a3a3a3")
        self.combo.configure(foreground="#000000")
        self.combo.configure(highlightbackground="#d9d9d9")
        self.combo.configure(highlightcolor="black")
        self.combo.configure(justify='left')
        self.combo.configure(text='''COMBO''')
        self.combo.configure(value="4")
        self.combo.configure(variable=menu_support.meal)

        self.Frame5 = tk.Frame(self.Frame3)
        self.Frame5.place(relx=0.14, rely=0.081, relheight=0.155, relwidth=0.739)

        self.Frame5.configure(relief='groove')
        self.Frame5.configure(borderwidth="4")
        self.Frame5.configure(relief="groove")
        self.Frame5.configure(background="#721287")
        self.Frame5.configure(highlightbackground="#d9d9d9")
        self.Frame5.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame5)
        self.Label2.place(relx=0.238, rely=0.13, height=52, width=117)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#721287")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''MEAL''')

        self.order = tk.Button(self.Frame1)
        self.order.place(relx=0.424, rely=0.869, height=63, width=176)
        self.order.configure(activebackground="#ececec")
        self.order.configure(activeforeground="#000000")
        self.order.configure(background="#721287")
        self.order.configure(borderwidth="3")
        self.order.configure(disabledforeground="#a3a3a3")
        self.order.configure(font="-family {Times New Roman} -size 14 -weight bold")
        self.order.configure(foreground="#ffffff")
        self.order.configure(highlightbackground="#d9d9d9")
        self.order.configure(highlightcolor="black")
        self.order.configure(pady="0")
        self.order.configure(text='''ORDER''')
        self.order.configure(command=self.place_order)

        self.lblroom = tk.Label(self.Frame1)
        self.lblroom.place(relx=0.206, rely=0.057, height=46, width=243)
        self.lblroom.configure(background="#400080")
        self.lblroom.configure(disabledforeground="#a3a3a3")
        self.lblroom.configure(font=font9)
        self.lblroom.configure(foreground="#ffffff")
        self.lblroom.configure(text='''Enter Room Number''')

        self.room = tk.Entry(self.Frame1)
        self.room.place(relx=0.528, rely=0.057,height=44, relwidth=0.257)
        self.room.configure(background="#81b7e3")
        self.room.configure(borderwidth="5")
        self.room.configure(disabledforeground="#a3a3a3")
        self.room.configure(font="TkFixedFont")
        self.room.configure(foreground="#000000")
        self.room.configure(insertbackground="black")

if __name__ == '__main__':
    vp_start_gui()





