import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import platform
import time
import os

import logging
import json
from PIL import Image, ImageTk
import database_Server as db
import commonFunction
from utilities import write_log_file,log_except
from tkinter.messagebox import showinfo
import csv

TITLE_FONT = ("Helvetica", 18, "bold")
l=0
LABEL_BG = "white"  # Light gray.
ROWS, COLS = 8, 5  # Size of grid.
ROWS_DISP = 8  # Number of rows to display.
COLS_DISP = 5  # Number of columns to display.
reg_text_size="Times 15 italic bold"
name=""
username=""
password=""
username2=""
password2=""
password3=""
access=""
patientid=""
patientids=""
reportStart=""
reportEnd=""
back=[]
imageList = []
patient_entry=""
button2=None
numberChoosen=None
key=None
numberChoosen1=None
entry1=None;entry2=None;entry3=None;entry4=None;entry5=None;entry_config=None;license_entry=None;disorder_entry=None;report_entry=None
canvas1=None;canvas2=None;canvas3=None;canvas4=None;canvas5=None; canvas6=None;canvas=None; master=None; canvas7=None; canvas8=None; canvas_img=None
vsb=None;hsb=None
login=0
font_size = ('Verdana', 15)
root = Tk()
root.title('Maritime Doctor')
catQuestion = []
entries = {}
entrises = {}
Txtentries = {}
symptom_entry = None
# imageList = []
content=[]
with open('Const/ports.csv', encoding="utf8") as f:
    reader = csv.reader(f, skipinitialspace=True)
    # print((reader))

    rows = list(reader)
    for row in rows:
        # print(row[1])
        content.append(row[1]) #list(row[0] for i in row)


if platform.system()=="Linux":
    root.attributes('-zoomed', True)
    backButton_height = 90
else:
    root.state('zoomed')
    backButton_height = 50
s = ttk.Style(root)
dialog_button_font="Calibri 13 bold"
dialog_body_font="calibri 16"
status=""
excategory=""
optionChoosen=''
text=""
lable_font="Times 20 italic bold"

ExerciseName=''
info="                                                Information       "
warn = "                                   Warning       "
error="                                                Error"


image3 = Image.open("Pictures/company_logo.jpg")
image3 = image3.resize((200, 140), Image.ANTIALIAS)
photo_image3 = ImageTk.PhotoImage(image3)
image4 = Image.open("Pictures/reports-png-1.png")
image4 = image4.resize((170, 200), Image.ANTIALIAS)
report_image = ImageTk.PhotoImage(image4)
image7 = Image.open("Pictures/homeicon.jpg")
image7 = image7.resize((150, 150), Image.ANTIALIAS)
photo_image7 = ImageTk.PhotoImage(image7)
image9 = Image.open("Pictures/backbuttonicon.png")
image9 = image9.resize((90, 90), Image.ANTIALIAS)
photo_image9 = ImageTk.PhotoImage(image9)
image17 = Image.open("Pictures/patient_reg.png")
image17 = image17.resize((170, 200), Image.ANTIALIAS)
doctor_image = ImageTk.PhotoImage(image17)

canvas_image = Image.open("Pictures/home_page.jpg")

canvas_bg = ImageTk.PhotoImage(canvas_image)
canvas_Alimage = Image.open("Pictures/home_page_2.jpg")
canvas_Alimage = canvas_Alimage.resize((root.winfo_screenwidth(),root.winfo_screenheight()), Image.ANTIALIAS)
canvas_Albg = ImageTk.PhotoImage(canvas_Alimage)

def create_shes_logs ():
    from pathlib import Path
    cdir = os.path.abspath(os.path.dirname(__file__))
    if (platform.system() == "Linux"):
        dirnew = cdir + '/Log'
    else:
        dirnew = cdir + '\\Log'
    p = Path(dirnew)

    if not ( p.exists() and p.is_dir()): # create Log dir if one does not exist
        os.makedirs(dirnew)

    # Log Initilization
    write_log_file()
    logging.info("========================================================")
    logging.info('                   Session Started                      ')
    logging.info("========================================================")
create_shes_logs()
#++++++++++++backbutton functionality+++++++++++
def backpage():
    global back,root,username
    if len(back)>0 :
        v=back[-1]
        back=back[:-1]
        if v==1:
            #homemiddlepart(user)
        #     initialmiddlepart()
            seafearsRecords()
            pass
        elif v==2:
            homemiddlepart(username)

        elif v==3:

          loginPage()
        elif v ==5:
            homemiddlepart(username)
        # elif v==4:
        #     if canvas5 is not None:
        #         canvas5.config(height=0, width=0)
        #         canvas5.delete("all")
        #     gamepage()
        # elif v==5:
        #     reportGameGraph.destroy()
        #     runreport()

    else:
        # if messagebox.askyesno("Verify", "Do you want to exit?")==True :
            root.quit()


# +++++++++++++++++Custom Dialog box changes++++++++++++++++++++++
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

        self.message = Message(self.root, text=text,aspect=700,font=dialog_body_font,bg="white")
        self.message.pack(expand=True, fill=BOTH)
        self.frame =tk.Frame(self.root)
        self.frame.pack(fill='both',expand=0)
        self.num = default
        self.cancel = cancel
        self.default = default
        self.root.bind('<Return>', self.return_event)
        for num in range(len(buttons)):
            s = buttons[num]
            b =Button(self.frame, text=s,command=(lambda self=self, num=num: self.done(num)),bg="#007ED9",fg="white",borderwidth=1,width=10,font=dialog_button_font,activebackground='blue',
                                         cursor="hand2")

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
        # self.root.mainloop()
        self.root.wait_window()
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
        self.root.destroy()
# ++++++++++++++++++++++Custom Dialog box ended+++++++++++++++++++++++



# +++++++++++++++++++++HoverButton +++++++++++++++++++
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# +++++++++++++++++HoverButton Ended+++++++++++++++++++++++
def toprightmostpart(val=None) :
    try:

        global canvas4, username, photo_image6, photo_image7, photo_image8, login
        if val== 1:
            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
            canvas4 = Canvas(root, bg="white", width=230, height=100,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
            profile_button = Button(canvas4, anchor=W, padx=2, text=str(username).title(), bg="white",fg="blue", font=('Times', 14, 'underline italic'), highlightthickness=0, bd=0,
                                    command=profile)
            profile_button.place(x=110, y=12)
            image6 = Image.open("Pictures/signout.png")
            image6 = image6.resize((30, 30), Image.ANTIALIAS)
            photo_image6 = ImageTk.PhotoImage(image6)
            image7 = Image.open("Pictures/homeicon.jpg")
            image7 = image7.resize((30, 30), Image.ANTIALIAS)
            photo_image7 = ImageTk.PhotoImage(image7)
            button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
                                  command=lambda: loginPage(),activebackground='blue', cursor="hand2")
            button1.place(x=120, y=50)
            #
            # image7 = Image.open("Pictures/homeicon.jpg")
            # image7 = image7.resize((30, 30), Image.ANTIALIAS)
            # photo_image7 = ImageTk.PhotoImage(image7)
            # print("im innnn")
            button2 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image7, borderwidth=0,
                                  command=lambda: homemiddlepart(username),activebackground='blue', cursor="hand2")
            button2.place(x=60, y=50)
        elif login == 1 or val== 1:

            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
            canvas4 = Canvas(root, bg="white", width=230, height=100,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
            profile_button = Button(canvas4, anchor=W, padx=2, text=str(username).title(), bg="white", fg="blue",
                                    font=('Times', 14, 'underline italic'), highlightthickness=0, bd=0,
                                    command=profile)
            profile_button.place(x=110, y=12)
            image6 = Image.open("Pictures/signout.png")
            image6 = image6.resize((30, 30), Image.ANTIALIAS)
            photo_image6 = ImageTk.PhotoImage(image6)
            button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
                                  command=lambda: loginPage(),activebackground='blue', cursor="hand2")
            button1.place(x=120, y=50)

            image7 = Image.open("Pictures/homeicon.jpg")
            image7 = image7.resize((30, 30), Image.ANTIALIAS)
            photo_image7 = ImageTk.PhotoImage(image7)
            button2 = HoverButton(canvas4, compound=TOP, fg="white", bg="black", image=photo_image7, borderwidth=0, activebackground='blue', cursor="hand2",command=lambda: homemiddlepart(username),)
            button2.place(x=60, y=50)
        elif login == 2:

            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
            canvas4 = Canvas(root, bg="white", width=230, height=100,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            link1 = Label(canvas4, font=('Verdana', 12), text="Login", fg="blue", bg="white", cursor="hand2")
            link1.place(x=120, y=50)
            link1.bind("<Button-1>", lambda e: loginPage())
    except:
        log_except()

def loginPage():
    try:
        global canvas5, username, reportGameGraph, password, entry1, entry2, font_size, canvas1, login, back, canvas2, photo_image9, roll, numberChoosen1, canvas2, photo_image2, photo_image3

        back.append(5)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if canvas2 is not None:
            canvas2.config(height=0, width=0)
            canvas2.delete("all")
        if canvas is not None:
            canvas.destroy()
        if entry3 is not None:
            entry3.destroy()

        login = 0
        username = StringVar()
        password = StringVar()

        # canvas_bgg = Canvas(root, bg="blue", width=200, height=200, highlightbackground="black",
        #                  highlightthickness=5)
        # #canvas_bgg.place(x=0, y=0)
        # canvas_bgg.pack(expand = tk.YES , fill = tk.BOTH)
        # #bg_image= ImageTk.PhotoImage(file=report_image)
        # canvas_bgg.create_image(10,10,image=canvas_bg,anchor= 'nw')
        #
        #
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth()-0.5, height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Login")


        canvas_img = Canvas(root, bg="white", width=root.winfo_screenwidth() - 0.5, height=root.winfo_screenheight() - 105,
                         highlightbackground="white", highlightthickness=0)
        canvas_img.place(x=0, y=30)
        canvas_img.create_image(550,100, image=canvas_bg)

        canvas2 = Canvas(root, width=250, height=200)
        canvas2.place(x=10, y=30)
        image3 = Image.open("Pictures/company_logo.jpg")
        image3 = image3.resize((260, 210), Image.ANTIALIAS)

        photo_image3 = ImageTk.PhotoImage(image3)
        canvas2.create_image(128, 100, image=photo_image3)

        canvas3 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=22, highlightbackground="black",
                         highlightthickness=5)
        canvas3.place(x=0, y=root.winfo_screenheight() - 95)
        canvas3.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 10 italic bold",
                            text="2019 © Maritime Doctor")
        # Images
        # photo_image2 = ImageTk.PhotoImage(image2)
        # canvas2.create_image(150, 100, image=photo_image2)

        canvas5 = Canvas(root, bg="white", width=600, height=350, bd=0, relief='ridge',
                         highlightthickness=0)  # , highlightbackground="black", highlightthickness=5)
        canvas5.place(x=400, y=190)  # int(root.winfo_screenheight()/2)),

        # canv = Canvas(root, width=600, height=500, bg='white')
        # canv.grid(row=2, column=3)
        #
        # img = ImageTk.PhotoImage(Image.open("D:\shes\Pictures\home_page.jpg"))  # PIL solution
        # canv.create_image(20, 20, anchor=NW, image=img)
        #
        canvas5.create_text(310, 40, fill="black", font="Times 25 italic bold", text="Ship Login")
        canvas5.create_text(150, 120, fill="black", font="Times 20 italic bold", text="Username    : ")
        canvas5.create_text(150, 190, fill="black", font="Times 20 italic bold", text="Password : ")

        entry1 = Entry(canvas5, textvariable=username, bd=3, width=20, font=font_size)
        entry1.place(x=250, y=110)
        entry1.focus()
        entry1.delete(0, END)

        entry2 = Entry(canvas5, show="*", textvariable=password, bd=3, width=20, font=font_size)
        entry2.place(x=250, y=180)
        entry2.delete(0, END)

        button1 = HoverButton(canvas5, text="Login", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                              width=15, activebackground='blue',command=checkLogIn, cursor="hand2")# command=checkLogIn,
        button1.place(x=250, y=250)

        # canvas5.create_text(410, 300, fill="black", font="Times 10 italic bold", text="New user? Create an account. ")
        if db._userCount():
            link1=Label(canvas5,text="New user? Create an account. ",fg="blue",bg="white",cursor="hand2")
            link1.place(x=250,y=300)
            link1.bind("<Button-1>",lambda e:registration())


        # button2 = HoverButton(canvas5, text="Register", bg="#007ED9", fg="white", font=('Helvetica', '15'),
        #                       command=lambda:registration(), width=15, activebackground='blue', cursor="hand2")
        # button2.place(x=320, y=250)

        # toprightmostpart()
    except:
        log_except()
def checkLogIn() :
    global username, password, login,entry3,entry4

    username=actNum = entry1.get()
    pinNum = entry2.get()

    if db._logincheck({'ship_username' : username,'sys_pwd' : commonFunction.computeMD5hash(pinNum)}):
        logging.info("Valid Login Credentials - " + str(time.strftime('%d %b %Y %X')) )

        homemiddlepart(user=actNum)
    elif actNum == "":
        logging.info(str(time.time()) + " " + "Please enter username")
        d = dialoguebox(root, text="Please enter a valid Username", buttons=["OK"], default=0, cancel=2,
                        title='warn',
                        icon='Pictures/warn.png')
        d.go()
    elif pinNum == "":
        logging.info(str(time.time()) + " " + "Please enter password")

        d = dialoguebox(root, text="Please enter password.", buttons=["OK"], default=0, cancel=2, title='warn',
                        icon='Pictures/warn.png')
        d.go()
    else:
        d = dialoguebox(root, text="Username or Password is incorrect", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()

def homemiddlepart(user) :
    try:

        global canvas5, report_image,image2, canvas4, canvas1, \
            login, back, photo_image6, reportGameGraph, canvas2,canvas_img
        # back.append(1)
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
        canvas2.create_image(150, 100, image=photo_image3)
        # Images

        canvas_img = Canvas(root, bg="white", width=root.winfo_screenwidth() * 0.975,
                            height=root.winfo_screenheight() * 0.790,
                            highlightbackground="white", highlightthickness=0)
        canvas_img.place(x=root.winfo_screenwidth() * 0.013, y=root.winfo_screenheight() * 0.065)
        canvas_img.create_image(root.winfo_screenwidth() *0.5, root.winfo_screenheight() * 0.42, image=canvas_Albg)
        canvas_img.create_image(150, 100, image=photo_image3)


        canvas4 = Canvas(root, bg="white", width=230, height=100,
                         highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
        canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
        canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
        profile_button = Button(canvas4,anchor=W,padx=2,text=str(user).title(),bg="white",\
                                fg="blue",font=('Times', 14, 'underline italic'),highlightthickness = 0, bd = 0, command=profile)
        profile_button.place(x=110, y=12)
        #canvas4.create_text(140, 25, fill="blue", font="Times 14 bold ", text=str(user).title())
        image6 = Image.open("Pictures/signout.png")
        image6 = image6.resize((30, 30), Image.ANTIALIAS)
        photo_image6 = ImageTk.PhotoImage(image6)
        button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,command=loginPage)
        button1.place(x=120, y=50)



        canvas5 = Canvas(root, bg="white", width=1100, height=350, bd=0, relief='ridge',highlightthickness=0)
        canvas5.place(x=150, y=280)

        canvas5.create_text(250, 100, fill="black", font="Times 20 italic bold", text="Add seafarer")
        canvas5.create_text(530, 100, fill="black", font="Times 20 italic bold", text="Seafarers List")
        canvas5.create_text(830, 100, fill="black", font="Times 20 italic bold", text="MDR List")

        doctor_img = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=doctor_image,
                              borderwidth=0,  cursor="hand2",activebackground="white",command=patientRegistration)#command=records,
        doctor_img.place(x=170, y=140)
        report_img = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=report_image,
                              borderwidth=0, cursor="hand2",activebackground="white",command=seafearsRecords)  # command=lambda:runreport()
        report_img.place(x=440, y=140)
        report_img = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=report_image,
                                 borderwidth=0, cursor="hand2", activebackground="white",
                                 command=MedicalRequestRecords)  # command=lambda:runreport()
        report_img.place(x=740, y=140)
        # x=790, y=140
        # ========================
    except:
        log_except()

def patientRegistration():

    try:
        #db.questionSync()
        global canvas5,canvas2, canvas4,canvas1, back,pat_entry,pat_sur_entry,\
            pat_age_entry,pat_gender,pat_dob_entry,pat_nationality_entry,pat_rank_entry,login,canvas_img
        back.append(2)
        login = 1
        # doctor_img.config(state="disabled", cursor="wait")


        # if canvas1 is not None:
        #     canvas1.config(height=0, width=0)
        #     canvas1.delete("all")
        if canvas_img is not None:
            canvas_img.config(height=0, width=0)
            canvas_img.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        # if canvas2 is not None:
        #     canvas2.config(height=0, width=0)
        #     canvas2.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas is not None:
            canvas.destroy()

        patient_name = StringVar()
        pat_surname = StringVar()
        pat_age = StringVar()
        pat_gender = StringVar()
        pat_gender.set(0)
        pat_dob = StringVar()
        pat_nationality = StringVar()
        pat_rank = StringVar()

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="seafarers Registration Form")
        canvas5 = Canvas(root, width=700, height=500,bg="white", bd=0, relief='ridge',highlightthickness=0)
        canvas5.place(x=400, y=100)
        canvas6 = Canvas(root, bg="white", width=100, height=100, bd=0, relief='ridge', highlightthickness=0)
        canvas6.place(x=100, y=475)

        label_msg = Label(canvas5, font="Times 13", text="", bg="white",fg="blue", width=50)
        label_msg.place(x=180, y=35)
        canvas5.create_text(180, 80, fill="black", font=reg_text_size, text="   Name                      : ")
        canvas5.create_text(180, 130, fill="black", font=reg_text_size, text="  Surname                 : ")
        canvas5.create_text(180, 180, fill="black", font=reg_text_size, text=" Age                          : ")
        canvas5.create_text(180, 230, fill="black", font=reg_text_size, text=" Sex                          : ")
        canvas5.create_text(180, 280, fill="black", font=reg_text_size, text="Date of Birth          : ")
        canvas5.create_text(180, 330, fill="black", font=reg_text_size, text="Nationality              : ")
        canvas5.create_text(180, 380, fill="black", font=reg_text_size, text="Rank                      : ")
        pat_entry = Entry(canvas5, textvariable=patient_name, bd=3, width=11, font=font_size, validate="key")
        pat_entry.place(x=360, y=65)
        pat_sur_entry = Entry(canvas5, textvariable=pat_surname, bd=3, width=11, font=font_size, validate="key")
        pat_sur_entry.place(x=360, y=115)
        pat_age_entry = Entry(canvas5, textvariable=pat_age, bd=3, width=11, font=font_size, validate="key")
        pat_age_entry.place(x=360, y=165)
        R1 = Radiobutton(canvas5, text="MALE", value="male", var=pat_gender,bg="white")
        R2 = Radiobutton(canvas5, text="FEMALE", value="female",bg="white", var=pat_gender)
        R2.deselect()
        R1.place(x=360, y=215)
        R2.place(x=440, y=215)

        pat_dob_entry = Entry(canvas5, textvariable=pat_dob, bd=3, width=11, font=font_size,
                                 validate="key")
        pat_dob_entry.place(x=360, y=265)

        # nationality=["INDIA","coiuntry","ednhbfd"]
        pat_nationality_entry = Entry(canvas5,textvariable=pat_nationality, bd=3, width=12, font=font_size)
        #ttk.Combobox(canvas5, values=nationality, textvariable=pat_nationality, width=21, height=4, font="Verdana 12" )
        pat_nationality_entry.place(x=360, y=315)


        rank = ['MASTER/CAPTAIN','CHIEF MATE/ FIRST OFFICER','SECOND MATE/ SECOND OFFICER ','THIRD MATE/ THIRD OFFICER','DECK CREW ','DECK TRAINEE',
            'DECK BOY ','CHIEF ENGINEER','1ST ENGINEER ','2ND ENGINEER','3RD ENGINEER','4TH ENGINEER','ENGINE CREW ','ENGINEE TRAINEE','ENGINE BOY OILER',
            'ABLE SEAMAN ','ORDINARY SEAMAN','BOSUN/BOATSWAIN WIPER','FITTER ','PUMPMAN','ELECTRICIAN ','MESSMAN','COOK ','STOWAWAYS','CASTAWAY ','SUPERNUMERARY']
        pat_rank_entry = ttk.Combobox(canvas5, values=rank, textvariable=pat_rank, width=21,height=4, font="Verdana 12")
        pat_rank_entry.place(x=360, y=365)




        # pat_rank_entry= Entry(canvas5,textvariable=pat_rank, bd=3, width=11, font=font_size,
        #                         validate="key")
        # pat_rank_entry.place()

        back_button = HoverButton(canvas6, image=photo_image9, width=80, height=backButton_height, bg="white",
                                  borderwidth=0,
                                  font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=10, y=25)

        save_button = HoverButton(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                  width=15, activebackground='blue', cursor="hand2", command=lambda: savePatientDetails()) #, command=lambda: saveDetails()
        save_button.place(x=180, y=420)
        toprightmostpart()


    except:
        log_except()


def registration():
    try:

        global canvas5,canvas2, canvas4,canvas1, back,ship_entry,\
            cap_phone_entry,ship_email_entry, ship_email_pwd_entry,login_pwd_entry,label_msg,login
        back.append(3)
        # if canvas1 is not None:
        #     canvas1.config(height=0, width=0)
        #     canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        # if canvas2 is not None:
        #     canvas2.config(height=0, width=0)
        #     canvas2.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas is not None:
            canvas.destroy()

        # if canvas5 is not None:
        #     canvas5.destroy()
        login = 2
        ship_name = StringVar()
        cap_phone = StringVar()
        ship_email = StringVar()
        ship_email_pwd = StringVar()
        login_pwd = StringVar()

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="SHES Registration Form")



        canvas5 = Canvas(root, width=1000, height=500,bg="white", bd=0, relief='ridge',highlightthickness=0)

        canvas5.place(x=300, y=100)

        label_msg = Label(canvas5, font="Times 13", text="", bg="white",fg="blue", width=50)
        label_msg.place(x=180, y=35)
        canvas5.create_text(180, 80, fill="black", font=reg_text_size, text="Ship Name*           : ")
        canvas5.create_text(180, 160, fill="black", font=reg_text_size, text="Phone            : ")
        canvas5.create_text(180, 240, fill="black", font=reg_text_size, text="Email ID*            : ")
        canvas5.create_text(180, 300, fill="black", font=reg_text_size, text="Email Password*      : ")
        canvas5.create_text(180, 380, fill="black", font=reg_text_size, text="Login Password*      : ")

        ship_entry = Entry(canvas5, textvariable=ship_name, bd=3, width=11, font=font_size, validate="key")
        ship_entry.place(x=360, y=70)
        cap_phone_entry = Entry(canvas5, textvariable=cap_phone, bd=3, width=11, font=font_size, validate="key")
        cap_phone_entry.place(x=360, y=140)
        ship_email_entry = Entry(canvas5, textvariable=ship_email, bd=3, width=11, font=font_size, validate="key")
        ship_email_entry.place(x=360, y=210)
        ship_email_pwd_entry = Entry(canvas5,show="*", textvariable=ship_email_pwd, bd=3, width=11, font=font_size,
                                     validate="key")
        ship_email_pwd_entry.place(x=360, y=280)
        login_pwd_entry = Entry(canvas5,show="*", textvariable=login_pwd, bd=3, width=11, font=font_size,
                                     validate="key")
        login_pwd_entry.place(x=360, y=350)
        save_button = HoverButton(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                  width=15, command=lambda: saveDetails(), activebackground='blue', cursor="hand2")
        save_button.place(x=180, y=420)

        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white",
                                  borderwidth=0,
                                  font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)

        toprightmostpart()
    except:
        log_except()

def saveDetails():
    # print("in save method")
    ship_name= ship_entry.get()
    cap_phone= cap_phone_entry.get()
    ship_email= ship_email_entry.get()
    ship_email_pwd= ship_email_pwd_entry.get()
    lpgin_pwd= login_pwd_entry.get()

    if ship_name and ship_email and ship_email_pwd and lpgin_pwd:
        if db._detailscheck(ship_name, ship_email):
            email_content = {
                'ship_name': ship_name,
                'cap_phone': cap_phone,
                'ship_email': ship_email,
                'ship_email_pwd': ship_email_pwd,
                'lpgin_pwd': lpgin_pwd
            }
            # email send
            SuccessMsg = commonFunction._sendregemail(email_content)
            if type(SuccessMsg) is bool:
                label_msg.config(text="Registration Done")
                loginPage()
            else:
                label_msg.config(text=SuccessMsg)
        else:
            label_msg.config(text="Ship Name/Email Already Exist")

    elif ship_name == "":
        logging.info(str(time.time()) + " " + "Please Enter Ship Name")
        d = dialoguebox(root, text="Please enter Ship Name", buttons=["OK"], default=0, cancel=2,
                        title='warn',
                        icon='Pictures/warn.png')
        d.go()
    elif ship_email == "":
        logging.info(str(time.time()) + " " + "Please Enter Ship Email")

        d = dialoguebox(root, text="Please Enter Ship Email.", buttons=["OK"], default=0, cancel=2, title='warn',
                        icon='Pictures/warn.png')
        d.go()
    elif ship_email_pwd =="":
        d = dialoguebox(root, text="Please Enter Ship Email Password", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()
    elif lpgin_pwd == "":
        d = dialoguebox(root, text="Please Enter Password", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()

def savePatientDetails():
    # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa:::::',pat_nationality_entry.get())
    # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa:::::',pat_rank_entry.get())
    seafear_details = {
    "seafer_id" : username,
    "pat_name": pat_entry.get(),
    "sur_name": pat_sur_entry.get(),
    "pat_nation": pat_nationality_entry.get(),
    "dob": pat_dob_entry.get(),
    "pat_age": pat_age_entry.get(),
    "pat_gender": pat_gender.get(),
    "pat_rank": pat_rank_entry.get(),
            }
    if db.saveSeafearsDetails(seafear_details):
        seafearsRecords()
    else:
        d = dialoguebox(root, text="Something Went Wrong. Try again ....", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()
def on_closing():
    try:
        logging.info("On closing ")
        d = dialoguebox(root, text="Do you want to exit the application?", buttons=["Yes", "No"], default=0,
                        cancel=2, title=warn, icon='Pictures/warn.png')
        if (d.go()) == 0:

            force_kill()
    except:
        log_except()
with open('Const/config.json') as i:
    json_const = json.load(i)
envMode = json_const["ENVIRONMENT"]
def force_kill():
    try:
        logging.info("In force kill... ")
        if envMode == "development":
            os.system("taskkill /f /im database_Server.py 1>nul")
            os._exit(0)
        else:
            if (platform.system()=="Windows"):

                os.system("taskkill /f /im database_Server.exe 1>nul 2>nul")
                os._exit(0)
            else:
                os.system("sudo pkill database_Server")
                os._exit(0)
    except:
        log_except()

class AutocompleteCombobox(ttk.Combobox):
    try:

        def set_completion_list(self, completion_list):
            """Use our completion list as our drop down selection menu, arrows move through menu."""
            self._completion_list = sorted(completion_list, key=str.lower)  # Work with a sorted list
            self._hits = []
            self._hit_index = 0
            self.position = 0
            self.bind('<KeyRelease>', self.handle_keyrelease)
            self['values'] = self._completion_list  # Setup our popup menu

        def autocomplete(self, delta=0):
            """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
            if delta:  # need to delete selection otherwise we would fix the current position
                self.delete(self.position, tk.END)
            else:  # set position to end so selection starts where textentry ended
                self.position = len(self.get())
            # collect hits
            _hits = []
            for element in self._completion_list:
                if element.lower().startswith(self.get().lower()):  # Match case insensitively
                    _hits.append(element)
            # if we have a new hit list, keep this in mind
            if _hits != self._hits:
                self._hit_index = 0
                self._hits = _hits
            # only allow cycling if we are in a known hit list
            if _hits == self._hits and self._hits:
                self._hit_index = (self._hit_index + delta) % len(self._hits)
            # now finally perform the auto completion
            if self._hits:
                self.delete(0, tk.END)
                self.insert(0, self._hits[self._hit_index])
                self.select_range(self.position, tk.END)

        def handle_keyrelease(self, event):
            """event handler for the keyrelease event on this widget"""
            if event.keysym == "BackSpace":
                self.delete(self.index(tk.INSERT), tk.END)
                self.position = self.index(tk.END)
            if event.keysym == "Left":
                if self.position < self.index(tk.END):  # delete the selection
                    self.delete(self.position, tk.END)
                else:
                    self.position = self.position - 1  # delete one character
                    self.delete(self.position, tk.END)
            if event.keysym == "Right":
                self.position = self.index(tk.END)  # go to end (no selection)
            if len(event.keysym) == 1:
                self.autocomplete()
            # No need for up/down, we'll jump to the popup
            # list at the position of the autocompletion
    except:
        log_except()

def profile():
    try:
        global canvas5,canvas2, canvas4,canvas1, back,login,username
        back.append(2)
        # if canvas1 is not None:
        #     canvas1.config(height=0, width=0)
        #     canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        # if canvas2 is not None:
        #     canvas2.config(height=0, width=0)
        #     canvas2.delete("all")
        # if canvas4 is not None:
        #     canvas4.config(height=0, width=0)
        #     canvas4.delete("all")
        if canvas is not None:
            canvas.destroy()

        # if canvas5 is not None:
        #     canvas5.destroy()
        login = 2

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Profile")
        canvas5 = Canvas(root, width=800, height=550,bg="white", bd=0, relief='ridge',highlightthickness=0)

        canvas5.place(x=350, y=100)
        canvas6 = Canvas(root, bg="white", width=200, height=150, bd=0, relief='ridge', highlightthickness=0)
        canvas6.place(x=50, y=500)
        login=1
        #toprightmostpart()

        canvas5.create_text(180, 80, fill="black", font=reg_text_size, text="Ship Name                 : ")
        canvas5.create_text(180, 140, fill="black", font=reg_text_size, text="Call Sign                : ")
        canvas5.create_text(180, 200, fill="black", font=reg_text_size, text="IMO Number         : ")
        canvas5.create_text(180, 260, fill="black", font=reg_text_size, text="Username                 : ")
        canvas5.create_text(180, 320, fill="black", font=reg_text_size, text="Email ID             : ")
        canvas5.create_text(180, 380, fill="black", font=reg_text_size, text="Country               : ")

        result = {}
        result = db._getuserDetail(username)
        canvas5.create_text(360, 80, fill="black", font=reg_text_size, text=result['ship_name'] if result['ship_name'] else "-")
        canvas5.create_text(360, 140, fill="black", font=reg_text_size, text=result['call_sign'] if result['call_sign'] else "-")
        canvas5.create_text(360, 200, fill="black", font=reg_text_size, text=result['imo_number'] if result['imo_number'] else "-")
        canvas5.create_text(360, 260, fill="black", font=reg_text_size, text=result['ship_username'] if result['ship_username'] else "-")
        canvas5.create_text(380, 320, fill="black", font=reg_text_size, text=result['ship_email'] if result['ship_email'] else "-")
        canvas5.create_text(360, 380, fill="black", font=reg_text_size, text=result['country'] if result['country'] else "-")

        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white",
                                  borderwidth=0,
                                  font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=50)

    except:
        log_except()


# setting up the user details to a table
def seafearsRecords():

    global canvas6,login,canvas4,doctor_image,master,canvas_img
    if canvas_img is not None:
        canvas_img.config(height=0, width=0)
        canvas_img.delete("all")
    if canvas5 is not None:
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
    if canvas4 is not None:
        canvas4.config(height=0, width=0)
        canvas4.delete("all")
    # if canvas6 is not None:
    #     canvas6.config(height=0, width=0)
    #     canvas6.delete("all")
    back.append(2)
    login=1
    #doctor_img.config(state="disabled", cursor="wait")
    toprightmostpart()
    canvas6 = Canvas(root, bg="white", width=100, height=100, bd=0, relief='ridge', highlightthickness=0)
    canvas6.place(x=100, y=475)
    canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                     highlightthickness=5)
    canvas1.place(x=0, y=0)
    canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text=" SHEFEAR Details")
    master = Canvas(root, bg="black", width=500, height=200, bd=0, relief='ridge')
    master.place(x=350, y=200)
    # Create a frame for the canvas and scrollbar(s).
    frame2 = tk.Frame(master)
    frame2.grid(row=3, column=1, sticky=tk.NW)
           # Add a canvas in that frame.
    canvas = tk.Canvas(frame2)
    canvas.grid(row=0, column=0)

    # Create a vertical scrollbar linked to the canvas.
    vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
    vsbar.grid(row=0, column=1, sticky=tk.NS)
    canvas.configure(yscrollcommand=vsbar.set)

    # Create a horizontal scrollbar linked to the canvas.
    hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
    hsbar.grid(row=1, column=0, sticky=tk.EW)
    canvas.configure(xscrollcommand=hsbar.set)

    # Create a frame on the canvas to contain the buttons.
    shipdetails_frame = tk.Frame(canvas, bg="Black", bd=2)

    # Add the buttons to the frame.
    showallrecords(shipdetails_frame)
    # Create canvas window to hold the shipdetails_frame.
    canvas.create_window((0,0), window=shipdetails_frame, anchor=tk.NW)

    shipdetails_frame.update_idletasks()  # Needed to make bbox info available.
    bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
    # print('canvas.bbox(tk.ALL): {}'.format(bbox))

    # Define the scrollable region as entire canvas with only the desired
    # number of rows and columns displayed.
    w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]

    dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
    canvas.configure(scrollregion=bbox, width=dw, height=dh)

    back_button = HoverButton(canvas6, image=photo_image9, width=80, height=backButton_height, bg="white",
                              borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
    back_button.place(x=10, y=25)
    #
    # label3 = tk.Label(root, text="Frame3 Contents", bg=LABEL_BG)
    # label3.grid(row=4, column=0, pady=5, sticky=tk.NW)
    #
    # frame3 = tk.Frame(master, bg="Blue", bd=2, relief=tk.GROOVE)
    # frame3.grid(row=5, column=0, sticky=tk.NW)

# table ended

def medicalRequest(seafar_id):

    try:
        db.questionSync()
        global canvas5,canvas2, canvas4,canvas1, back,deprt_port_entry,arrival_port_entry,temp_entry,symptom_entry, \
        present_location_entry,arrival_time_entry,latitide_entry,longitute_entry,bp_entry,pulse_rate_entry,weight_entry,\
        login,canvas7,canvas8,textBox_entry,back_button,allQuestions,symptomVariable,symptomType,symptom_type_entry,sym_type_id
        back.append(1)

        login=1

        if canvas7 is not None:
            canvas7.config(height=0, width=0)
            canvas7.delete("all")
        if canvas8 is not None:
            canvas8.config(height=0, width=0)
            canvas8.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        # if canvas2 is not None:
        #     canvas2.config(height=0, width=0)
        #     canvas2.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas is not None:
            canvas.config(height=0, width=0)
            canvas.delete("all")
            canvas.destroy()
        if master is not None:
            master.config(height=0, width=0)
            master.delete("all")
            master.destroy()

        login = 1
        # doctor_img.config(state="disabled", cursor="wait")
        toprightmostpart()
        deprt_port = StringVar()
        arrival_port = StringVar()
        present_location = StringVar()
        arrival_time = StringVar()
        longitute = StringVar()
        latitide = StringVar()
        temperature = StringVar()
        bp = StringVar()
        pulse_rate = StringVar()
        weight = StringVar()


        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="seafarers Medical Form-"+str(seafar_id))
        canvas5 = Canvas(root, width=1100, height=430,bg="white", bd=0, relief='ridge',highlightthickness=0)
        canvas5.place(x=200, y=220)
        canvas6 = Canvas(root, bg="white", width=100, height=100, bd=0, relief='ridge', highlightthickness=0)
        canvas6.place(x=100, y=475)

        canvas8 = Canvas(root, width=1000, height=430, bg="white", bd=0, relief='ridge', highlightthickness=0)
        # canvas7.place(x=200, y=200)

        label_msg = Label(canvas5, font="Times 13", text="", bg="white",fg="blue", width=50)
        label_msg.place(x=250, y=5)

        canvas5.create_text(280, 40, fill="black", font=('Times', 18, 'underline bold'), text="Vessel Position")
        canvas5.create_text(700, 40, fill="black", font=('Times', 18, 'underline bold'), text="Vital Sign")
        canvas5.create_text(180, 80, fill="black", font=reg_text_size, text="   Departure Port                      : ")
        canvas5.create_text(650, 80, fill="black", font=reg_text_size, text="   Temperature                      : ")
        canvas5.create_text(180, 130, fill="black", font=reg_text_size, text="  Arrival Port                          : ")
        canvas5.create_text(650, 130, fill="black", font=reg_text_size, text="  Blood Pressure(mmHg)     : ")
        canvas5.create_text(180, 180, fill="black", font=reg_text_size, text=" Arrival Time                          : ")
        canvas5.create_text(650, 180, fill="black", font=reg_text_size, text=" Pulse Rate (Bits/min)       : ")
        canvas5.create_text(180, 230, fill="black", font=reg_text_size, text=" Present Position                  : ")
        canvas5.create_text(650, 230, fill="black", font=reg_text_size, text=" Weight(Kg)                     : ")
        canvas5.create_text(180, 280, fill="black", font=reg_text_size, text="Latitude                                : ")
        canvas5.create_text(650, 280, fill="black", font=reg_text_size, text="Symptom Type                : ")
        canvas5.create_text(180, 330, fill="black", font=reg_text_size, text=" Longitude                              : ")
        canvas5.create_text(650, 330, fill="black", font=reg_text_size, text="Symptom                : ")
        deprt_port_entry =  AutocompleteCombobox(canvas5, textvariable=deprt_port, width=10, font=font_size, height=8) #Entry(canvas5, textvariable=deprt_port, bd=3, width=11, font=font_size, validate="key")
        deprt_port_entry.set_completion_list(content)
        deprt_port_entry.place(x=360, y=65)
        temp_entry = Entry(canvas5, textvariable=temperature, bd=3, width=11, font=font_size, validate="key")
        temp_entry.place(x=800, y=65)
        arrival_port_entry = AutocompleteCombobox(canvas5, textvariable=arrival_port, width=10, font=font_size, height=8)#Entry(canvas5, textvariable=arrival_port, bd=3, width=11, font=font_size, validate="key")
        arrival_port_entry.set_completion_list(content)
        arrival_port_entry.place(x=360, y=115)
        bp_entry = Entry(canvas5, textvariable=bp, bd=3, width=11, font=font_size, validate="key")
        bp_entry.place(x=800, y=115)

        arrival_time_entry = Entry(canvas5, textvariable=arrival_time, bd=3, width=11, font=font_size, validate="key")
        arrival_time_entry.place(x=360, y=165)
        pulse_rate_entry = Entry(canvas5, textvariable=pulse_rate, bd=3, width=11, font=font_size, validate="key")
        pulse_rate_entry.place(x=800, y=165)
        present_location_entry = Entry(canvas5, textvariable=present_location, bd=3, width=11, font=font_size, validate="key")
        present_location_entry.place(x=360, y=215)
        weight_entry = Entry(canvas5, textvariable=weight, bd=3, width=11, font=font_size, validate="key")
        weight_entry.place(x=800, y=215)
        latitide_entry = Entry(canvas5, textvariable=latitide, bd=3, width=11, font=font_size,
                                 validate="key")
        latitide_entry.place(x=360, y=265)

        # symptom_entry = Entry(canvas5, textvariable=symptom, bd=3, width=11, font=font_size,
        #                       validate="key")
        # symptom_entry.place(x=800, y=265)
        #symptomType
        symptomType = StringVar()
        allQuestions = db.getQuestions()
        symptomsType = [ "Diseases", "Accidents" ]
        #symptomsType = [ value for key,value in allType]
        symptom_type_entry = AutocompleteCombobox(canvas5, textvariable=symptomType, width=20, font=font_size,
                                                height=8)  # Entry(canvas5, textvariable=deprt_port, bd=3, width=11, font=font_size, validate="key")
        symptom_type_entry.set_completion_list(symptomsType)
        symptom_type_entry.place(x=800, y=265)

        symptom_type_entry.bind("<<ComboboxSelected>>", lambda event: getCategeries(symptomType.get()))

        longitute_entry = Entry(canvas5, textvariable=longitute, bd=3, width=11, font=font_size,
                                 validate="key")
        longitute_entry.place(x=360, y=315)

        symptomVariable = StringVar()
        symptom_entry = AutocompleteCombobox(canvas5, textvariable=symptomVariable, width=20, font=font_size,
                                             height=8)  # Entry(canvas5, textvariable=deprt_port, bd=3, width=11, font=font_size, validate="key")
        #symptoms = [i.cat_name for i in allQuestions if i.sym_type == sym_type_id]
        #symptom_entry.set_completion_list(symptoms)
        symptom_entry.place(x=800, y=315)

        def getCategeries(sym_type):
            sym_type_id = 1
            if sym_type == 'Diseases':
                sym_type_id = 1
            if sym_type == 'Accidents':
                sym_type_id = 2

            print(sym_type)
            print(sym_type_id)
            allQuestions = db.getQuestions()
            symptoms = [i.cat_name for i in allQuestions if i.sym_type == sym_type_id]
            symptom_entry.set_completion_list(symptoms)


        back_button = HoverButton(canvas6, image=photo_image9, width=80, height=backButton_height, bg="white",
                                  borderwidth=0,
                                  font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=10, y=25)
        canvas7 = Canvas(root, width=1000, height=430, bg="white", bd=0, relief='ridge', highlightthickness=0)
        
        next_button = HoverButton(canvas5, text="Next>>", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                  width=15, activebackground='blue', cursor="hand2",
                                  command=lambda: showCanvas(canvas7, canvas5,1,1))  # , command=lambda: saveDetails()
        next_button.place(x=600, y=385)

            #canvas7.place(x=200, y=200)
        previous_button7 = HoverButton(canvas7, text="<<Previous", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                   width=15, activebackground='blue', cursor="hand2",
                                   command=lambda: showCanvas(canvas5, canvas7,2))  # , command=lambda: saveDetails()
        previous_button7.place(x=8, y=385)
        next_button7 = HoverButton(canvas7, text="Next>>", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                 width=15, activebackground='blue', cursor="hand2",
                                 command=lambda: showCanvas(canvas8, canvas7,1))  # , command=lambda: saveDetails()
        next_button7.place(x=600, y=385)
        #Canvas 7 end Canvas 8 start
        Label(canvas8, font="Times 13", text="Upload if any images", bg="white", fg="blue", width=50).place(x=200, y=100)
        button = tk.Button(canvas8, text='Upload Image', command=UploadAction)
        button.place(x=500,y=100)
        Label(canvas8, font="Times 13", text="Other Information", bg="white", fg="blue", width=50).place(x=200, y=150)
        # OtherVariable = StringVar()
        textBox_entry = Text(canvas8, bd=3, width=30,height=6, font=font_size)
        textBox_entry.place(x=500, y=150)
        previous_button8 = HoverButton(canvas8, text="<<Previous", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                       width=15, activebackground='blue', cursor="hand2",
                                       command=lambda: showCanvas(canvas7, canvas8,1,1))  # , command=lambda: saveDetails()
        previous_button8.place(x=8, y=385)
        next_button7 = HoverButton(canvas8, text="Submit", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                   width=15, activebackground='blue', cursor="hand2",
                                   command= lambda :SaveMedicalReq(seafar_id))  # , command=lambda: saveDetails()
        next_button7.place(x=600, y=385)
        #Canvas 8 end a


        #canvas 9 end


    except Exception as e:
        print(e)
        # print(repr(e))
        # print(e.args)

        log_except()

def UploadAction(event=None):
    global imageList
    imageList = []
    filez = filedialog.askopenfilenames()
    imageList = list(filez)


def SaveMedicalReq(seafar_id):
    global Txtentries, entries
    answers  = []
    answerrs = []
    answerss = []
    inputValue = ''
    #print(Txtentries)

    answerrs = [(Ingre, var) for Ingre, var in entries.items()]
    answerss = [(Ingre, var.get()) for Ingre, var in Txtentries.items()]
    answers = answerrs + answerss
    #print(answers)
    if deprt_port_entry.get() and arrival_port_entry.get() and temp_entry.get() and symptom_entry.get() and \
        present_location_entry.get() and arrival_time_entry.get() and latitide_entry.get() and longitute_entry.get() \
        and bp_entry.get() and pulse_rate_entry.get() and weight_entry.get():
        if textBox_entry.get("1.0", "end-1c") is not None:
            inputValue = textBox_entry.get("1.0", "end-1c")
        else:
            inputValue = ''
        resultDict = []
        resultDict = [seafar_id,'MDR-10001',deprt_port_entry.get(),arrival_port_entry.get(),arrival_time_entry.get(), \
                      present_location_entry.get(),latitide_entry.get(),longitute_entry.get(),temp_entry.get(),bp_entry.get(), \
                      pulse_rate_entry.get(),weight_entry.get(),symptom_entry.get(),inputValue,answers]
        SuccessMessage = db.SaveMedicalDetials(resultDict,imageList)
        d = dialoguebox(root, text=SuccessMessage, buttons=["OK"], default=0, cancel=2, title='warn',
                        icon='Pictures/info.png')
        Txtentries.clear()
        entries.clear()
        resultDict.clear()

        MedicalRequestRecords()
        d.go()
    else:
        d = dialoguebox(root, text="Please enter all details", buttons=["OK"], default=0, cancel=2, title='warn',
                        icon='Pictures/warn.png')
        d.go()

    #print(answers)


def getQuestions():
    global canvas7
    canvas7 = Canvas(root, bg="black", width=500, height=100, bd=0, relief='ridge')
    # master.place(x=200, y=200)
    # Create a frame for the canvas and scrollbar(s).
    frame2 = tk.Frame(canvas7)
    frame2.grid(row=3, column=1, sticky=tk.NW)
    # Add a canvas in that frame.
    canvas = tk.Canvas(frame2)
    canvas.grid(row=0, column=0)

    # Create a vertical scrollbar linked to the canvas.
    vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
    vsbar.grid(row=0, column=1, sticky=tk.NS)
    canvas.configure(yscrollcommand=vsbar.set)

    # Create a horizontal scrollbar linked to the canvas.
    hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
    hsbar.grid(row=1, column=0, sticky=tk.EW)
    canvas.configure(xscrollcommand=hsbar.set)

    # Create a frame on the canvas to contain the buttons.
    shipdetails_frame = tk.Frame(canvas, bg="white", bd=2)

    # Add the buttons to the frame.
    showallquestions(shipdetails_frame)

    # Create canvas window to hold the shipdetails_frame.
    canvas.create_window((0, 0), window=shipdetails_frame, anchor=tk.NW)

    shipdetails_frame.update_idletasks()  # Needed to make bbox info available.
    bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
    # print('canvas.bbox(tk.ALL): {}'.format(bbox))

    # Define the scrollable region as entire canvas with only the desired
    # number of rows and columns displayed.
    w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]

    dw, dh = int((w / COLS) * COLS_DISP), int((h / ROWS) * ROWS_DISP)
    canvas.configure(scrollregion=bbox, width=dw, height=410)

    # if canvas7 is not None:
    #     canvas7.config(height=0, width=0)
    #     canvas7.delete("all")
    #     canvas7.destroy()
    #
    # canvas7 = Canvas(root, width=1000, height=430, bg="white", bd=0, relief='ridge', highlightthickness=0)
    # # canvas7.place(x=200, y=200)
    # # ============================
    #
    # # ============================
    # catQuestion = [i.questionaries for i in allQuestions if i.cat_name == symptomVariable.get()]
    # i = 10
    # if len(catQuestion[0]) > 0:
    #     for ques in catQuestion[0]:
    #         # for ques in quest:
    #         Label(canvas7, font="Times 13", text=ques.name, bg="white", fg="blue", width=70, anchor="w").place(x=100,
    #                                                                                                            y=i)
    #         # print(ques.qus_type)
    #         if ques.qus_type == 1:
    #             var = StringVar()
    #             Entry(canvas7, textvariable=var, bd=3, width=11, font=font_size).place(x=700, y=i)
    #
    #             entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(ques.ques_answers[0].ans_id) + "-" + str(
    #                 ques.qus_type)] = var
    #         elif ques.qus_type == 2:
    #             a = 700
    #             varRad = StringVar()
    #             varRad.set(0)
    #             for radPick in ques.ques_answers:
    #                 Radiobutton(canvas7, text=radPick.name, variable=varRad, value=radPick.ans_id).place(x=a, y=i)
    #                 a = a + 100
    #                 entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(radPick.name) + "-" + str(
    #                     ques.qus_type)] = varRad
    #
    #         i = i + 40
    #     # Label(canvas7, font="Times 13", text="Other Information", bg="white", fg="blue", width=50).place(x=100, y=i)
    #     # OtherVariable = StringVar()
    #     # Text(canvas7, bd=3, width=11,height=2, font=font_size).place(x=500, y=i)

def showCanvas(canvasShow, canvasHide,status=None,datashow=None):
    global symptom_entry,symptom_type_entry

    if datashow!=None:
        print("hello")
    else:
        print("no hello")

    if status==1:
        if symptom_entry.get()=="":
            d = dialoguebox(root, text='please select the main symptom !!!', buttons=["OK"], default=0, cancel=2,
                            title='warn',
                            icon='Pictures/warn.png')

            if(d.go())==0:
                # canvasHide.place(x=200, y=200)
                # canvasShow.place_forget()
                back_button.place(x=10, y=25)

        else:
            if datashow != None:

                getQuestions()
                canvas7.place(x=200, y=200)
                canvasHide.place_forget()
                back_button.place_forget()
            else:

                canvasShow.place(x=200, y=200)
                canvasHide.place_forget()
                back_button.place_forget()
    else:
        if datashow != None:

            canvasShow.place(x=200, y=200)
            getQuestions()
            canvasHide.place_forget()
            back_button.place_forget()
        else:

            canvasShow.place(x=200, y=200)
            canvasHide.place_forget()
            back_button.place(x=10, y=25)

def MedicalRequestRecords():

    global canvas6,login,canvas4,canvas8,doctor_image,master,back_button,canvas_img
    if canvas_img is not None:
        canvas_img.config(height=0, width=0)
        canvas_img.delete("all")
    if canvas5 is not None:
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
    if canvas4 is not None:
        canvas4.config(height=0, width=0)
        canvas4.delete("all")
    if canvas8 is not None:
        canvas8.config(height=0, width=0)
        canvas8.delete("all")
    # if canvas6 is not None:
    #     canvas6.config(height=0, width=0)
    #     canvas6.delete("all")
    back.append(5)
    login=1
    #doctor_img.config(state="disabled", cursor="wait")
    toprightmostpart()
    canvas6 = Canvas(root, bg="white", width=100, height=100, bd=0, relief='ridge', highlightthickness=0)
    canvas6.place(x=100, y=475)
    canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                     highlightthickness=5)
    canvas1.place(x=0, y=0)
    canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text=" Medical Request Details")
    master = Canvas(root, bg="black", width=500, height=200, bd=0, relief='ridge')
    master.place(x=200, y=200)
    # Create a frame for the canvas and scrollbar(s).
    frame2 = tk.Frame(master)
    frame2.grid(row=3, column=1, sticky=tk.NW)
           # Add a canvas in that frame.
    canvas = tk.Canvas(frame2)
    canvas.grid(row=0, column=0)

    # Create a vertical scrollbar linked to the canvas.
    vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
    vsbar.grid(row=0, column=1, sticky=tk.NS)
    canvas.configure(yscrollcommand=vsbar.set)

    # Create a horizontal scrollbar linked to the canvas.
    hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
    hsbar.grid(row=1, column=0, sticky=tk.EW)
    canvas.configure(xscrollcommand=hsbar.set)

    # Create a frame on the canvas to contain the buttons.
    shipdetails_frame = tk.Frame(canvas, bg="Black", bd=2)

    # Add the buttons to the frame.
    showallMedicalrecords(shipdetails_frame)
    # Create canvas window to hold the shipdetails_frame.
    canvas.create_window((0,0), window=shipdetails_frame, anchor=tk.NW)

    shipdetails_frame.update_idletasks()  # Needed to make bbox info available.
    bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
    # print('canvas.bbox(tk.ALL): {}'.format(bbox))

    # Define the scrollable region as entire canvas with only the desired
    # number of rows and columns displayed.
    w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]

    dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
    canvas.configure(scrollregion=bbox, width=dw, height=400)

    back_button = HoverButton(canvas6, image=photo_image9, width=80, height=backButton_height, bg="white",
                              borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
    back_button.place(x=10, y=25)
    #
    # label3 = tk.Label(root, text="Frame3 Contents", bg=LABEL_BG)
    # label3.grid(row=4, column=0, pady=5, sticky=tk.NW)
    #
    # frame3 = tk.Frame(master, bg="Blue", bd=2, relief=tk.GROOVE)
    # frame3.grid(row=5, column=0, sticky=tk.NW)


def radioSelection(b):
    newDict = {}
    newDict[str(b[0]) + "-" + str(b[1]) + "-" + str(b[3])] = str(b[4])+"-"+str(b[2])
    # print(varRad.get())
    # print(b)
    entries[str(b[0]) + "-" + str(b[1]) + "-" + str(b[3])] = str(b[4])+"-"+str(b[2])
    entries.update(newDict)
    #print(entries)

def showallquestions(master):
    global ROWS
    #Txtentries = {}
    entries = {}
    catQuestion = []
    # data = db.MedicalRecordDetails()
    # print(symptomVariable.get())
    catQuestion = [i.questionaries for i in allQuestions if i.cat_name == symptomVariable.get()]
    #print(catQuestion)
    # if len(catQuestion) > 8:
    #     ROWS = 11


    #===============================
    # catQuestion = [i.questionaries for i in allQuestions if i.cat_name == symptomVariable.get()]
    # i = 10
    if len(catQuestion[0]) > 0:
        #print(str(catQuestion[0]))
        # print(str(catQuestion[0]))
        indexer=1
        for ques in catQuestion[0]:
    #         # for ques in quest:
            Label(master, font="Times 13", text=ques.name, bg="white", fg="blue", width=70, anchor="w").grid(row=indexer,
                                                                                              column=1)
            # print(ques.qus_type)
            if ques.qus_type == 1:
                var = StringVar()
                Entry(master, textvariable=var, bd=3, width=20, font=font_size).grid(row=indexer,
                                                                                              column=2)

                Txtentries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(ques.ques_answers[0].ans_id) + "-" + str(
                    ques.qus_type)] = var
            elif ques.qus_type == 2:
                a = 700
                varRad = StringVar()
                a=2
                varRad.set(0)
                # print(varRad.set(0))
                # print(ques.ques_answers)

                for radPick in ques.ques_answers:
                    Radiobutton(master, text=radPick.name, variable=varRad, value=radPick.ans_id,
                                command =lambda b=[ques.q_id, ques.name, radPick.name, ques.qus_type,
                                                  radPick.ans_id]: radioSelection(b)
                                ).grid(row=indexer,column=a)

                    a = a + 1
                    # print(" in for loop" + str(varRad))
                    #
                    entrises[str(ques.q_id) + "-" + str(ques.name) + "-" + str(radPick.name) + "-" + str(
                        ques.qus_type)] = varRad
            indexer=indexer+1

    #
    #         i = i + 40
    #     # Label(canvas7, font="Times 13", text="Other Information", bg="white", fg="blue", width=50).place(x=100, y=i)
    #     # OtherVariable = StringVar()
    #     # Text(canvas7, bd=3, width=11,height=2, font=font_size).place(x=500, y=i)
        previous_button7 = HoverButton(master, text="<<Previous", bg="#007ED9", fg="white",
                                       font=('Helvetica', '15'),
                                       width=15, activebackground='blue', cursor="hand2",
                                       command=lambda: showCanvas(canvas5, canvas7,
                                                                  2)) .grid(row=indexer+2,
                                                                                              column=1) # , command=lambda: saveDetails()
        # previous_button7.place(x=8, y=385)
        next_button7 = HoverButton(master, text="Next>>", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                   width=15, activebackground='blue', cursor="hand2",
                                   command=lambda: showCanvas(canvas8, canvas7,
                                                              1)) .grid(row=indexer+2,column=2) # , command=lambda: saveDetails()
        # next_button7.place(x=600, y=385)
    #===============================


    #
    # dateLabel = Label(master, text="S.No", width=10, height=3, relief="ridge", bg="black", fg="white")
    # dateLabel.grid(row=0, column=0)
    # dateLabel = Label(master, text="Medical Request ID", width=20, height=3, relief="ridge", bg="black",
    #                   fg="white")
    # dateLabel.grid(row=0, column=1)
    # # BMILabel = Label(master, text="Nationality", width=40, height=3, relief="ridge", bg="black",
    # #                  fg="white")
    # # BMILabel.grid(row=0, column=2)
    # # usernameLabel = Label(master, text="DOB", width=20, height=3, relief="ridge", bg="black",
    # #                   fg="white")
    # # usernameLabel.grid(row=0, column=3)
    # stateLabel = Label(master, text="Departure Port", width=20, height=3, relief="ridge", bg="black",
    #                    fg="white")
    # stateLabel.grid(row=0, column=2)
    # stateLabel = Label(master, text="Arrival Port", width=20, height=3, relief="ridge", bg="black",
    #                    fg="white")
    # stateLabel.grid(row=0, column=3)
    # # countryLabel = Label(master, text="Rank", width=20, height=3, relief="ridge", bg="black",
    # #                    fg="white")
    # # countryLabel.grid(row=0, column=6)
    # countryLabel = Label(master, text="Present Position", width=20, height=3, relief="ridge", bg="black",
    #                      fg="white")
    # countryLabel.grid(row=0, column=4)
    # countryLabel = Label(master, text="Images", width=20, height=3, relief="ridge", bg="black",
    #                      fg="white")
    # countryLabel.grid(row=0, column=5)
    # countryLabel = Label(master, text="Replay", width=20, height=3, relief="ridge", bg="black",
    #                      fg="white")
    # countryLabel.grid(row=0, column=6)
    # for index, dat in catQuestion:
    #     i = dat[1]
    #     j = dat[2]
    #     tk.Label(master, text=index + 1, relief="ridge", width=10, bg="white", height=2).grid(row=index + 1,
    #                                                                                           column=0)
    #     tk.Label(master, text=dat[2], relief="ridge", width=20, bg="white", height=2).grid(
    #         row=index + 1, column=1)
    #     # tk.Label(master, text=dat[4],relief="ridge",width=40,bg="white",height=2).grid(row=index + 1, column=2)
    #     # tk.Label(master, text=dat[5],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=3)
    #     tk.Label(master, text=dat[3], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=2)
    #     tk.Label(master, text=dat[4], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=3)
    #     # tk.Label(master, text=dat[8], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=6)
    #     tk.Label(master, text=dat[6], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=4)
    #     #tk.Label(master, text=dat[-2], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=5)
    #
    #     MDR_button = Button(master, anchor=W, padx=2, text="View Images", width=20, height=2, relief="ridge",
    #                         bg="white", \
    #                         fg="blue", font=('Times', 10, 'underline'), highlightthickness=0, bd=1,
    #                         command=lambda j=dat[-1]: medicalReqImages(j,master))
    #     MDR_button.grid(row=index + 1, column=5)
    #
    #     MDR_button = Button(master, anchor=W, padx=2, text="View Doctor Replay", width=20, height=2, relief="ridge",
    #                         bg="white", \
    #                         fg="blue", font=('Times', 10, 'underline'), highlightthickness=0, bd=1,
    #                         command=lambda i=[dat[-5],dat[-3],dat[-2]]: medicalReplay(i))
    #     MDR_button.grid(row=index + 1, column=6)
def showallMedicalrecords(master):
    global ROWS
    ROWS = 5
    data = db.MedicalRecordDetails()
    if len(data) > 8:
        ROWS = 11
    dateLabel = Label(master, text="S.No", width=10, height=3, relief="ridge", bg="black", fg="white")
    dateLabel.grid(row=0, column=0)
    dateLabel = Label(master, text="Medical Request ID", width=20, height=3, relief="ridge", bg="black",
                      fg="white")
    dateLabel.grid(row=0, column=1)
    # BMILabel = Label(master, text="Nationality", width=40, height=3, relief="ridge", bg="black",
    #                  fg="white")
    # BMILabel.grid(row=0, column=2)
    # usernameLabel = Label(master, text="DOB", width=20, height=3, relief="ridge", bg="black",
    #                   fg="white")
    # usernameLabel.grid(row=0, column=3)
    stateLabel = Label(master, text="Departure Port", width=20, height=3, relief="ridge", bg="black",
                       fg="white")
    stateLabel.grid(row=0, column=2)
    stateLabel = Label(master, text="Arrival Port", width=20, height=3, relief="ridge", bg="black",
                       fg="white")
    stateLabel.grid(row=0, column=3)
    # countryLabel = Label(master, text="Rank", width=20, height=3, relief="ridge", bg="black",
    #                    fg="white")
    # countryLabel.grid(row=0, column=6)
    countryLabel = Label(master, text="Present Position", width=20, height=3, relief="ridge", bg="black",
                         fg="white")
    countryLabel.grid(row=0, column=4)
    countryLabel = Label(master, text="Images", width=20, height=3, relief="ridge", bg="black",
                         fg="white")
    countryLabel.grid(row=0, column=5)
    countryLabel = Label(master, text="Replay", width=20, height=3, relief="ridge", bg="black",
                         fg="white")
    countryLabel.grid(row=0, column=6)
    countryLabel = Label(master, text="More Info", width=20, height=3, relief="ridge", bg="black",
                         fg="white")
    countryLabel.grid(row=0, column=7)
    for index, dat in enumerate(data):
        i = dat[1]
        j = dat[2]
        tk.Label(master, text=index + 1, relief="ridge", width=10, bg="white", height=2).grid(row=index + 1,
                                                                                              column=0)
        tk.Label(master, text=dat[2], relief="ridge", width=20, bg="white", height=2).grid(
            row=index + 1, column=1)
        # tk.Label(master, text=dat[4],relief="ridge",width=40,bg="white",height=2).grid(row=index + 1, column=2)
        # tk.Label(master, text=dat[5],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=3)
        tk.Label(master, text=dat[3], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=2)
        tk.Label(master, text=dat[4], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=3)
        # tk.Label(master, text=dat[8], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=6)
        tk.Label(master, text=dat[6], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=4)
        #tk.Label(master, text=dat[-2], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=5)

        MDR_button = Button(master, anchor=W, padx=2, text="View Images", width=20, height=2, relief="ridge",
                            bg="white", \
                            fg="blue", font=('Times', 10, 'underline'), highlightthickness=0, bd=1,
                            command=lambda j=dat[-1]: medicalReqImages(j,master))
        MDR_button.grid(row=index + 1, column=5)

        MDR_button = Button(master, anchor=W, padx=2, text="View Doctor Replay", width=20, height=2, relief="ridge",
                            bg="white", \
                            fg="blue", font=('Times', 10, 'underline'), highlightthickness=0, bd=1,
                            command=lambda i=[dat[-5],dat[-3],dat[-2]]: medicalReplay(i))
        MDR_button.grid(row=index + 1, column=6)
        MDR_button = Button(master, anchor=W, padx=2, text="View More info", width=20, height=2, relief="ridge",
                            bg="white", \
                            fg="blue", font=('Times', 10, 'underline'), highlightthickness=0, bd=1,
                            command=lambda i=dat[-1]: moreMDRInfo(i))
        MDR_button.grid(row=index + 1, column=7)

def medicalReqImages(medical_summary,display):
    if medical_summary is not None:
        requestimages = eval(medical_summary)
        filenames = requestimages['images']
        columns = 5
        image_count = 0
        window = Toplevel(display)
        window.wm_geometry("1000x500")
        canvas = Canvas(window, width=2150, height=500)
        canvas.grid(row=0, column=0, sticky="news")
        # canvas.place(x=0, y=0)

        vsb = Scrollbar(window, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=0, sticky="ns")
        canvas.configure(yscrollcommand=vsb.set)

        frame_image = Frame(canvas)
        frame_image.pack(expand=True, fill="both")
        canvas.create_window((0, 0), window=frame_image, anchor="nw")

        for name in filenames:
            image_count += 1
            r, c = divmod(image_count - 1, columns)
            im = Image.open(name)
            resized = im.resize((200, 200), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized)
            myvar = Label(frame_image, image=tkimage)
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            # print "here"
        # window.mainloop()
    else:
        d = dialoguebox(root, text='no attachments added!!!', buttons=["OK"], default=0, cancel=2,
                        title='info',
                        icon='Pictures/info.png')

        d.go()

def medicalReplay(replayList):
    #print(replayList)
    if replayList[2] is None:
        replayText = commonFunction.read_email_from_gmail(replayList[0],replayList[1])

        if replayText:
            showinfo('Doctor Replay', replayText['text'])
        else:
            d = dialoguebox(root, text='Replay Not yet get. Please Try again!!!', buttons=["OK"], default=0, cancel=2, title='warn',
                            icon='Pictures/warn.png')

            d.go()
    else:
        showinfo('Doctor Replay',replayList[2])


def showallrecords(master):
    global ROWS
    ROWS = 5
    data = db.readSeaferDetails()
    if len(data)>8:
        ROWS=11
    dateLabel = Label(master, text="S.No", width=10, height=3, relief="ridge", bg="black", fg="white")
    dateLabel.grid(row=0, column=0)
    dateLabel = Label(master, text="Name", width=20, height=3, relief="ridge", bg="black",
                      fg="white")
    dateLabel.grid(row=0, column=1)
    # BMILabel = Label(master, text="Nationality", width=40, height=3, relief="ridge", bg="black",
    #                  fg="white")
    # BMILabel.grid(row=0, column=2)
    # usernameLabel = Label(master, text="DOB", width=20, height=3, relief="ridge", bg="black",
    #                   fg="white")
    # usernameLabel.grid(row=0, column=3)
    stateLabel = Label(master, text="age", width=20, height=3, relief="ridge", bg="black",
                       fg="white")
    stateLabel.grid(row=0, column=2)
    stateLabel = Label(master, text="Sex", width=20, height=3, relief="ridge", bg="black",
                       fg="white")
    stateLabel.grid(row=0, column=3)
    # countryLabel = Label(master, text="Rank", width=20, height=3, relief="ridge", bg="black",
    #                    fg="white")
    # countryLabel.grid(row=0, column=6)
    countryLabel = Label(master, text="Request", width=20, height=3, relief="ridge", bg="black",
                         fg="white")
    countryLabel.grid(row=0, column=4)
    countryLabel = Label(master, text="More Info", width=20, height=3, relief="ridge", bg="black",
                         fg="white")
    countryLabel.grid(row=0, column=5)
    for index, dat in enumerate(data):
            i = dat[1]
            j=dat[2]
            tk.Label(master, text=index+1,relief="ridge",width=10,bg="white",height=2).grid(row=index + 1, column=0)
            tk.Label(master, text=dat[2]+" "+dat[3],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=1)
            # tk.Label(master, text=dat[4],relief="ridge",width=40,bg="white",height=2).grid(row=index + 1, column=2)
            # tk.Label(master, text=dat[5],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=3)
            tk.Label(master, text=dat[6],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=2)
            tk.Label(master, text=dat[7], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=3)
            # tk.Label(master, text=dat[8], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=6)
            #tk.Label(master, text=dat[8], relief="ridge", width=20, bg="white", height=2).grid(row=index + 1, column=7)
            MDR_button = Button(master, anchor=W, padx=2, text="Medical Request", width=20,height=2,relief="ridge", bg="white", \
                                    fg="blue", font=('Times', 10, 'underline'), highlightthickness=0, bd=1,
                                 command= lambda i=i: medicalRequest(i))
            MDR_button.grid(row=index + 1, column=4)
            more_button = Button(master, anchor=W, padx=2, text="More", width=20, height=2, relief="ridge",
                                bg="white", \
                                fg="blue", font=('Times', 10, 'underline'), highlightthickness=0, bd=1,
                                command=lambda i=[dat[4],dat[5],dat[8]]: moreInfo(i))

            more_button.grid(row=index + 1, column=5)

def moreInfo(moreList):
    #print(moreList)
    morestr = 'Date of Birth : ' + moreList[1] + '\n\n' + 'Nationality : ' +  moreList[0] + '\n\n' + 'Rank : ' + moreList[2]
    showinfo('More Info', morestr)

def moreMDRInfo(moreMDRList):
    #print(moreMDRList)
    if moreMDRList is not None:
        moreMDRdetails = eval(moreMDRList)
        basicInfo = moreMDRdetails['basicInfo']
        #print(basicInfo)
        moreMDRstr = 'Excepected Arrival Time : ' + basicInfo[4] + '\n\n' + 'Latitude : ' +  basicInfo[6] + '\n\n' + \
                     'longitude : ' + basicInfo[7] + '\n\n' + 'Temparature : ' + basicInfo[8] + '\n\n' + 'B.P : ' + basicInfo[9] + \
                     '\n\n' + 'Pulse Rate : ' + basicInfo[10] + '\n\n' + 'Weight : ' + basicInfo[11] +  '\n\n' + 'Symptom : ' + basicInfo[12] +\
                     '\n\n' + 'Other Information : ' + basicInfo[13]
        showinfo('More Info', moreMDRstr)

loginPage()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
if (platform.system()=="Linux"):
    root.attributes('-zoomed', True)
else:
    root.state('zoomed')

root.protocol("WM_DELETE_WINDOW", on_closing)
img = PhotoImage(file='Pictures/icon2.png')
root.tk.call('wm', 'iconphoto', root._w, img)

root.mainloop()