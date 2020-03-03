try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import tkinter as tk
import subprocess
import threading
import socket
from tkinter import messagebox
from tkinter import *
# import spinningGIF
# from utilities import write_log_file,log_except,remove_log_files
from PIL import Image, ImageTk
import os
import csv
import requests
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.pyplot as plt
import logging
from subprocess import Popen
import json
import sqlite3
# import report_generator
from datetime import datetime
import numpy.core._dtype_ctypes
from ctypes import *
import time
from math import floor

import tkinter as tk
from PIL import ImageTk, Image
entry1=None;entry2=None;entry3=None;entry4=None;entry5=None
username=""
password=""
canvas1=None;canvas2=None;canvas3=None;canvas4=None;canvas5=None; canvas6=None;canvas=None
try:
    global root
    canvas2 = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas2.pack(side='top', fill='both', expand='yes')

    # images
    image1 = Image.open("Pictures/App_Splash_background1.png")
    image1 = image1.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    photo_image1 = ImageTk.PhotoImage(image1)
    canvas2.create_image(0, 0, image=photo_image1, anchor='nw')
    image2 = Image.open("Pictures/soujhe_logo.png")
    image2 = image2.resize((150, 150), Image.ANTIALIAS)
    photo_image2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("Pictures/company_logo.png")
    image3 = image3.resize((150, 120), Image.ANTIALIAS)
    photo_image3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("Pictures/reporticon.jpg")
    image4 = image4.resize((150, 150), Image.ANTIALIAS)
    photo_image4 = ImageTk.PhotoImage(image4)
    image5 = Image.open("Pictures/gameicon.jpg")
    image5 = image5.resize((150, 150), Image.ANTIALIAS)
    photo_image5 = ImageTk.PhotoImage(image5)
    image6 = Image.open("Pictures/signout.png")
    image6 = image6.resize((150, 150), Image.ANTIALIAS)
    photo_image6 = ImageTk.PhotoImage(image5)
    image7 = Image.open("Pictures/homeicon.jpg")
    image7 = image7.resize((150, 150), Image.ANTIALIAS)
    photo_image7 = ImageTk.PhotoImage(image7)
    image8 = Image.open("Pictures/createaccount.jpg")
    image8 = image8.resize((190, 200), Image.ANTIALIAS)
    photo_image8 = ImageTk.PhotoImage(image8)
    image9 = Image.open("Pictures/backbuttonicon.png")
    image9 = image9.resize((90, 90), Image.ANTIALIAS)
    photo_image9 = ImageTk.PhotoImage(image9)
    image10 = Image.open("Pictures/viewuser.jpg")
    image10 = image10.resize((170, 180), Image.ANTIALIAS)
    photo_image10 = ImageTk.PhotoImage(image10)
    image11 = Image.open("Pictures/pdf-icon.png")
    image11 = image11.resize((50,50), Image.ANTIALIAS)
    photo_image11 = ImageTk.PhotoImage(image11)
    image12 = Image.open("Pictures/enter.png")
    image12 = image12.resize((20,20), Image.ANTIALIAS)
    photo_image12 = ImageTk.PhotoImage(image12)
    image13 = Image.open("Pictures/admin.png")
    image13 = image6.resize((30, 30), Image.ANTIALIAS)
    photo_image13 = ImageTk.PhotoImage(image13)

    # spinnerwheel = spinningGIF.Spinner(root, size=64)
    # canvas2.create_window(int(root.winfo_screenwidth() / 2 - 50), int(root.winfo_screenheight() / 2 - 50),
    #                       window=spinnerwheel)
except:
    # log_except()
    pass
def CanvasButton(canvas):
    # def __init__(self, canvas):
    global entry3,entry4
    canvas = canvas
    number = tk.IntVar()
    patientid = tk.StringVar()
    password=tk.StringVar()
    button = tk.Button(canvas, textvariable=number,
                            command=buttonclicked)

    id = canvas.create_window(screenWidgth, screenheight, width=25, height=25,
                                   window=button)
    # self.label=canvas.create_text(450, 190, font=("Purisa bold", 14),
    #                                                    fill="#4a3681",text="Patient ID")
    entry3 =Entry(canvas, textvariable=patientid, bd=3, width=20, font=("Purisa", 14))
    # excercise_game = entry3.bind("<FocusOut>", (lambda event: ChangeKey(entry3.get())))
    entry3.place(x=300, y=330)
    # entry3.insert(END,"User Id")
    entry3.focus_set()
    entry3.delete(0, END)

    entry4 =Entry(canvas, textvariable=password, bd=3, width=20, font=("Purisa", 14))
    # excercise_game = entry3.bind("<FocusOut>", (lambda event: ChangeKey(entry3.get())))
    entry4.place(x=300, y=410)
    # entry4.pack(ipady=3)
    # entry4.insert(END,"Password")
    entry4.focus_set()
    button1 = Button(canvas, text="Login",bg="white",activebackground="blue",font=('Helvetica', '15'),
                          width=10,cursor="hand2",command=checkLogIn)
    button1.place(x=230, y=490)
def buttonclicked(self):
    self.number.set(self.number.get()+1)  # auto updates Button
def checkLogIn() :


    global username, password, login, numberChoosen1,entry3,entry4

    act = "soujhe"
    pin = "soujhe"


    username=actNum = entry3.get()
    pinNum = entry4.get()

    if actNum == act and pinNum == pin:
        logging.info("Valid Login Credentials - " + str(time.strftime('%d %b %Y %X')) )

        homemiddlepart(actNum)
        print("im in next step")
    elif actNum == "":
        print("tkinter_Ui.py -- Line 1182 -- " + str(time.time()) + " " + "Please enter username")
        d = dialoguebox(root, text="Please enter a valid User ID", buttons=["OK"], default=0, cancel=2,
                        title='warn',
                        icon='Pictures/warn.png')
        d.go()

    elif pinNum == "":
        print("tkinter_Ui.py -- Line 1185 -- " + str(time.time()) + " " + "Please enter password")
        # messagebox.showerror("warning", "Please enter password.")

        d = dialoguebox(root, text="Please enter password.", buttons=["OK"], default=0, cancel=2, title='warn',
                        icon='Pictures/warn.png')
        d.go()

    else:
        # messagebox.showerror("warning", "User ID or Password is incorrect.")
        d = dialoguebox(root, text="User ID or Password is incorrect", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()
class dialoguebox:

    def __init__(self, master,
                 text='', buttons=[], default=None, cancel=None,title=None, class_=None,icon=None):
        if class_:
            self.root = Toplevel(master, class_=class_)
        else:
            self.root = Toplevel(master)
        if title:
            self.root.title(title)
            self.root.iconname(title)


        self.message = Message(self.root, text=text,aspect=700,bg="white")
        self.message.pack(expand=True, fill=BOTH)
        self.frame =tk.Frame(self.root)
        self.frame.pack(fill='both',expand=0)
        self.num = default
        self.cancel = cancel
        self.default = default
        self.root.bind('<Return>', self.return_event)
        for num in range(len(buttons)):
            s = buttons[num]
            b = Button(self.frame, text=s,command=(lambda self=self, num=num: self.done(num)),bg="#007ED9",fg="white",borderwidth=1,width=10,activebackground='blue',
                                         cursor="hand2")

            # infuture we need more buttons to add in popup disable from add belo code and remove the ****to **** code in comments
            # b = Button(self.frame, text=s,
            #            command=(lambda self=self, num=num: self.done(num)), bg="#007ED9", fg="white", borderwidth=2,
            #            width=6, font="Times 15 bold")
            # if num == default:
            #     b.config(relief=RAISED, borderwidth=2, bg="#007ED9")
            # b.pack(side=LEFT, expand=1, padx=10, pady=10)
            # *************
            if num == default:
                b.config(relief=RAISED, borderwidth=1)
                b.pack(pady=10)
            else:
                b.place(x=270,y=10)

        self.root.protocol('WM_DELETE_WINDOW', self.wm_delete_window)
        self._set_transient(master,icon)

    def _set_transient(self, master,icon, relx=0.45, rely=0.4):
        widget = self.root
        widget.withdraw() # Remain invisible while we figure out the geometry
        widget.transient(master)
        widget.update_idletasks()
        # Actualize geometry information
        widget.geometry('400x200')
        if master.winfo_ismapped():
            m_width = master.winfo_width()
            m_height = master.winfo_height()
            m_x = master.winfo_rootx()
            m_y = master.winfo_rooty()
        else:
            m_width = master.winfo_screenwidth()
            m_height = master.winfo_screenheight()
            m_x = m_y = 0
        w_width = widget.winfo_reqwidth()
        w_height = widget.winfo_reqheight()
        x = m_x + (m_width - w_width) * relx
        y = m_y + (m_height - w_height) * rely
        if x+w_width > master.winfo_screenwidth():
            x = master.winfo_screenwidth() - w_width
        elif x < 0:
            x = 0
        if y+w_height > master.winfo_screenheight():
            y = master.winfo_screenheight() - w_height
        elif y < 0:
            y = 0

        widget.geometry("+%d+%d" % (x, y))
        img = PhotoImage(file=icon)
        widget.tk.call('wm', 'iconphoto', widget._w, img)
        widget.deiconify() # Become visible at the desired location

    def go(self):
        self.root.wait_visibility()
        self.root.grab_set()
        self.root.mainloop()
        self.root.destroy()
        return self.num

    def return_event(self, event):
        if self.default is None:
            self.root.bell()
        else:
            self.done(self.default)

    def wm_delete_window(self):
        if self.cancel is None:
            self.root.bell()
        else:
            self.done(self.cancel)

    def done(self, num):
        self.num = num
        self.root.quit()
# ++++++++++++++++++++++Custom Dialoguebox ended+++++++++++++++++++++++

def homemiddlepart1() :


    global canvas5, photo_image4, photo_image5, username,password,canvas4, canvas1, login, back, photo_image6, reportGameGraph, canvas2, photo_image3, photo_image2
    # back.append(1)
    # canvas5.delete("all")
    if canvas is not None:
        canvas.destroy()

    login = 1

    canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                     highlightthickness=5)
    canvas1.place(x=0, y=0)
    canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Home")

    canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40, height=root.winfo_screenheight() - 165,
                     highlightbackground="blue", highlightthickness=20)
    canvas2.place(x=0, y=30)

    # Images
    image3 = Image.open("Pictures/company_logo.png")
    image3 = image3.resize((150, 120), Image.ANTIALIAS)



    #=============

    photo_image3 = ImageTk.PhotoImage(image3)
    canvas2.create_image(300, 100, image=photo_image3)

    canvas4 = Canvas(root, bg="white", width=230, height=200,
                     highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
    canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
    canvas4.create_text(80, 25, fill="black", font="Times 13 bold", text="Login : ")
    canvas4.create_text(140, 25, fill="blue", font="Times 13 bold ", text=username)
    image6 = Image.open("Pictures/signout.png")
    image6 = image6.resize((30, 30), Image.ANTIALIAS)
    photo_image6 = ImageTk.PhotoImage(image6)

    button1 = Button(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
                           activebackground='blue', cursor="hand2")#command=initialmiddlepart,

    button1.place(x=185, y=7)
    # canvas4.create_text(140, 70, fill="black", font="Times 12 bold", text="Sign Out ")Button(canvas5, text="Log in", font=('Helvetica', '15'), command=initialmiddlepart)

    canvas5 = Canvas(root, bg="white", width=550, height=350, bd=0, relief='ridge',
                     highlightthickness=0)  # , highlightbackground="black", highlightthickness=5)# highlightthickness=0)
    canvas5.place(x=400, y=200)
    canvas5.create_text(170, 90, fill="black", font="Times 20 italic bold", text="Run Report")
    canvas5.create_text(410, 90, fill="black", font="Times 20 italic bold", text="Run Game", )
    image4 = Image.open("Pictures/reports-png-1.png")
    image4 = image4.resize((170, 170), Image.ANTIALIAS)
    photo_image4 = ImageTk.PhotoImage(image4)
    button1 = Button(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image4,
                          borderwidth=0, cursor="hand2")# command=runreport,
    button1.place(x=80, y=140)

    # canvas5.create_image(150, 200, image=photo_image4)
    image5 = Image.open("Pictures/Physical-Therapy_Icon.png")
    image5 = image5.resize((170, 170), Image.ANTIALIAS)
    photo_image5 = ImageTk.PhotoImage(image5)
    # canvas5.create_image(400, 200, image=photo_image5)
    button2 = Button(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image5,
                          borderwidth=0, cursor="hand2")#, command=gamepage
    button2.place(x=320, y=140)

def homemiddlepart(user) :
    print("im in ")
    print(user)
    try:

        global canvas5, photo_image4, photo_image5, canvas4, canvas1, login, back, photo_image6, reportGameGraph, canvas2, photo_image3, photo_image2
        back.append(1)
        print(user)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas2 is not None:
            canvas2.config(height=0, width=0)
            canvas2.delete("all")
        if reportGameGraph is not None:
            reportGameGraph.destroy()
        # canvas5.config(height=0, width=0)
        # canvas5.delete("all")
        if canvas is not None:
            canvas.destroy()

        login = 1
        if user=="soujhe":
            print("im in admin")
            canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                             highlightthickness=5)
            canvas1.place(x=0, y=0)
            canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold",
                                text="Home")

            canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40,
                             height=root.winfo_screenheight() - 165,
                             highlightbackground="blue", highlightthickness=20)
            canvas2.place(x=0, y=30)

            # Images
            photo_image2 = ImageTk.PhotoImage(image2)
            canvas2.create_image(150, 100, image=photo_image2)
            photo_image3 = ImageTk.PhotoImage(image3)
            canvas2.create_image(300, 100, image=photo_image3)

            canvas4 = Canvas(root, bg="white", width=230, height=200,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            canvas4.create_text(80, 25, fill="black", font="Times 13 bold", text="Login : ")
            canvas4.create_text(140, 25, fill="blue", font="Times 13 bold ", text=str(username.get()).title())
            image6 = Image.open("Pictures/signout.png")
            image6 = image6.resize((30, 30), Image.ANTIALIAS)
            photo_image6 = ImageTk.PhotoImage(image6)

            # button1 = Button(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
            #                       command=initialmiddlepart, activebackground='blue', cursor="hand2")
            #
            # button1.place(x=185, y=7)
            # canvas4.create_text(140, 70, fill="black", font="Times 12 bold", text="Sign Out ")Button(canvas5, text="Log in", font=('Helvetica', '15'), command=initialmiddlepart)

            canvas5 = Canvas(root, bg="white", width=550, height=350, bd=0, relief='ridge',
                             highlightthickness=0)  # , highlightbackground="black", highlightthickness=5)# highlightthickness=0)
            canvas5.place(x=400, y=200)
            canvas5.create_text(170, 90, fill="black", font="Times 20 italic bold", text="Run Report")
            canvas5.create_text(410, 90, fill="black", font="Times 20 italic bold", text="Run Game")
            image4 = Image.open("Pictures/reports-png-1.png")
            image4 = image4.resize((170, 170), Image.ANTIALIAS)
            photo_image4 = ImageTk.PhotoImage(image4)
            # button1 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white",activebackground="white", image=photo_image4,
            #                       borderwidth=0, command=runreport, cursor="hand2")
            # button1.place(x=50, y=140)

            # canvas5.create_image(150, 200, image=photo_image4)
            image5 = Image.open("Pictures/Physical-Therapy_Icon.png")
            image5 = image5.resize((170, 170), Image.ANTIALIAS)
            photo_image5 = ImageTk.PhotoImage(image5)
            # canvas5.create_image(400, 200, image=photo_image5)
            # button2 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image5,
            #                       borderwidth=0, command=gamepage, cursor="hand2")
            # button2.place(x=250, y=140)

            image5 = Image.open("Pictures/admin.png")
            image5 = image5.resize((170, 170), Image.ANTIALIAS)
            photo_image5 = ImageTk.PhotoImage(image5)
            # canvas5.create_image(400, 200, image=photo_image5)
            # button3 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white",activebackground="white", image=photo_image5,
            #                       borderwidth=0, command=gamepage, cursor="hand2")
            # button3.place(x=450, y=140)

            # image13 = Image.open("Pictures/admin.png")
            # image13 = image6.resize((50, 50), Image.ANTIALIAS)
            # photo_image13 = ImageTk.PhotoImage(image13)
            # button3 = Button(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image13,
            #                       borderwidth=0, command=admin(), cursor="hand2")
            # button3.place(x=250, y=140)



        else:


            # =====================
            print("in non admin pannel")
            canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                             highlightthickness=5)
            canvas1.place(x=0, y=0)
            canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold",
                                text="Home")

            canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40,
                             height=root.winfo_screenheight() - 165,
                             highlightbackground="blue", highlightthickness=20)
            canvas2.place(x=0, y=30)

            # Images
            photo_image2 = ImageTk.PhotoImage(image2)
            canvas2.create_image(150, 100, image=photo_image2)
            photo_image3 = ImageTk.PhotoImage(image3)
            canvas2.create_image(300, 100, image=photo_image3)

            canvas4 = Canvas(root, bg="white", width=230, height=200,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            canvas4.create_text(80, 25, fill="black", font="Times 13 bold", text="Login : ")
            canvas4.create_text(140, 25, fill="blue", font="Times 13 bold ", text=str(username.get()).title())
            image6 = Image.open("Pictures/signout.png")
            image6 = image6.resize((30, 30), Image.ANTIALIAS)
            photo_image6 = ImageTk.PhotoImage(image6)
            # button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
            #                       command=initialmiddlepart, activebackground='blue', cursor="hand2")
            #
            # button1.place(x=185, y=7)
            # canvas4.create_text(140, 70, fill="black", font="Times 12 bold", text="Sign Out ")Button(canvas5, text="Log in", font=('Helvetica', '15'), command=initialmiddlepart)

            canvas5 = Canvas(root, bg="white", width=550, height=350, bd=0, relief='ridge',
                             highlightthickness=0)  # , highlightbackground="black", highlightthickness=5)# highlightthickness=0)
            canvas5.place(x=400, y=200)
            canvas5.create_text(170, 90, fill="black", font="Times 20 italic bold", text="Run Report")
            canvas5.create_text(410, 90, fill="black", font="Times 20 italic bold", text="Run Game", )
            image4 = Image.open("Pictures/reports-png-1.png")
            image4 = image4.resize((170, 170), Image.ANTIALIAS)
            photo_image4 = ImageTk.PhotoImage(image4)
            # button1 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image4,
            #                       borderwidth=0, command=runreport, cursor="hand2")
            # button1.place(x=80, y=140)

            # canvas5.create_image(150, 200, image=photo_image4)
            image5 = Image.open("Pictures/Physical-Therapy_Icon.png")
            image5 = image5.resize((170, 170), Image.ANTIALIAS)
            photo_image5 = ImageTk.PhotoImage(image5)
            # canvas5.create_image(400, 200, image=photo_image5)
            # button2 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image5,
            #                       borderwidth=0, command=gamepage, cursor="hand2")
            # button2.place(x=320, y=140)
            # ========================

    except:
        # log_except()
        pass
def admin():
    print("entered into admin screen")
    pass



root = tk.Tk()
root.resizable(width=True, height=True)
# root.wm_attributes("-topmost", 1)

imgpath = "Pictures/Login2.png"
img = Image.open(imgpath)
# img=img.resize((1390, 770), Image.ANTIALIAS)

photo = ImageTk.PhotoImage(img)
screenheight = root.winfo_screenheight()
screenWidgth = root.winfo_screenwidth()
canvas = tk.Canvas(root,width=screenWidgth, height=screenheight , bd=0, highlightthickness=0)
canvas.pack()
canvas.create_image(screenWidgth/2, screenheight/2, image=photo)

CanvasButton(canvas)
# create a clickable button on the canvas
root.state('zoomed')
root.mainloop()