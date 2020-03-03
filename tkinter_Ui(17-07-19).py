try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import tkinter as tk
import subprocess
import platform
import socket
import struct
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import spinningGIF
import pygatt
import datetime
from pygatt.backends import BLEAddressType
from utilities import write_log_file,log_except
from PIL import Image, ImageTk
import os
from tkinter import ttk
import logging
from subprocess import Popen
from ctypes import *
import json
import sqlite3
import time
import report_generator
if (platform.system()=="Linux"):
    backButton_height=90
else:
    backButton_height = 50










def create_soujhe_logs ():
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

def remove_soujhe_logs():
    import glob
    logging.info("Entered remove_soujhe_logs. ")
    with open('Const/config.json') as i:
        json_const = json.load(i)
        log_delete = json_const['LOG_DAYS']

    removed = 0
    #path = "desired path"
    # Check current working directory.
    dir_to_search = os.getcwd()

    if dir_to_search != "/Log/":  # compare current to desired directory
        # Now change the directory
        os.chdir('Log/')
        # Check current working directory.
        dir_to_search = os.getcwd()

    tifCounter = len(glob.glob1(dir_to_search, "*.log"))
    logging.info("Number of log files in directory : " + str(tifCounter))

    dataset_path = 'Log/'
    files = glob.glob(dir_to_search + "*.log")

    if tifCounter > log_delete:
        for dirpath, dirnames, filenames in os.walk(dir_to_search):
            filenames.sort(key=os.path.getmtime)

            for file in filenames[-len(filenames):-1]:

                curpath = os.path.join(dirpath, file)

                log_delete = json_const['LOG_DAYS']
                if len(glob.glob1(dir_to_search, "*.log")) > log_delete:

                    os.remove(curpath)
                    logging.info("Deleted log file : " + str(file))
                    removed += 1

    logging.info("Number of log files removed : " + str(removed))

l=0
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
exercise=""
duration=""
angle=0
roll=""
roll2=""
result1="2029-05-08"
errorval=0
key_value=None
fromfun=None
back=[]
patient_entry=""
button2=None
numberChoosen=None
key=None
numberChoosen1=None
entry1=None;entry2=None;entry3=None;entry4=None;entry5=None;entry_config=None;license_entry=None;disorder_entry=None;report_entry=None
canvas1=None;canvas2=None;canvas3=None;canvas4=None;canvas5=None; canvas6=None;canvas=None
login=0;
font_size = ('Verdana', 15)
root = Tk()
root.title('Soujhe Innovative Healthcare Devices Pvt. Ltd')

if (platform.system()=="Linux"):
    root.attributes('-zoomed', True)
else:
    root.state('zoomed')
s = ttk.Style(root)
# s.theme_use('clam')
reportGameGraph=None
exercise1=""
others=""
othersvalue=""
game_duration=""
dialog_button_font="Calibri 13 bold"
dialog_body_font="calibri 16"
exeType=""
exeValue=""
exercises=[]
duration_user=""
angle_value=""
othername=""
game=""
disorder=""
reg_disorder=""
status=""
excategory=""
optionChoosen=''
text=""
lable_font="Times 20 italic bold"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
game_ended = False
START_TIME = 0
END_TIME = 0
MAX_ANGLE_REACHED = 0
MIN_ANGLE_REACHED = 0
min_angle=""
NO_OF_REPS = 0
NO_OF_PERFECT_REPS = 0
ExerciseName=''
info="                                                Information       "
warn = "                                   Warning       "
error="                                                Error"

HAND_CHAR           = "00002004-0000-4d50-4320-5241454e494c"
MAX_ANGLE_CHAR      = "00002006-0000-4d50-4320-5241454e494c"
MIN_ANGLE_CHAR      = "00002007-0000-4d50-4320-5241454e494c"
GOTO_ANGLE_CHAR     = "00002008-0000-4d50-4320-5241454e494c"
HOME_ANGLE_CHAR     = "00002009-0000-4d50-4320-5241454e494c"
ONOFF_CHAR          = "0000200A-0000-4d50-4320-5241454e494c"
DURATION_CHAR       = "0000200B-0000-4d50-4320-5241454e494c"
CURR_ANGLE_CHAR     = "0000200C-0000-4d50-4320-5241454e494c"

currAngle = 0
onOffStatus = 0
duration = 0
minAngle=0
maxAngle=0

try:
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
    image13 = image13.resize((165,165), Image.ANTIALIAS)
    photo_image13 = ImageTk.PhotoImage(image13)
    image14 = Image.open("Pictures/calendar1.png")
    image14 = image14.resize((20, 20), Image.ANTIALIAS)
    photo_image14 = ImageTk.PhotoImage(image14)

    image15 = Image.open("Pictures/UpperLimb.png")
    image15 = image15.resize((210, 210), Image.ANTIALIAS)
    photo_image15 = ImageTk.PhotoImage(image15)

    image16 = Image.open("Pictures/lowerLimb.png")
    image16 = image16.resize((210, 210), Image.ANTIALIAS)
    photo_image16 = ImageTk.PhotoImage(image16)

    image17 = Image.open("Pictures/patient_reg.png")
    image17 = image17.resize((170, 170), Image.ANTIALIAS)
    photo_image17 = ImageTk.PhotoImage(image17)

    image18 = Image.open("Pictures/add_patient.png")
    image18 = image18.resize((210, 210), Image.ANTIALIAS)
    photo_image18 = ImageTk.PhotoImage(image18)

    image19 = Image.open("Pictures/edit_patient.png")
    image19 = image19.resize((210, 210), Image.ANTIALIAS)
    photo_image19 = ImageTk.PhotoImage(image19)

    image20 = Image.open("Pictures/calendar1.png")
    image20 = image14.resize((40, 40), Image.ANTIALIAS)
    photo_image20 = ImageTk.PhotoImage(image14)

    spinnerwheel = spinningGIF.Spinner(root, size=64)
    canvas2.create_window(int(root.winfo_screenwidth() / 2 - 50), int(root.winfo_screenheight() / 2 - 50),
                          window=spinnerwheel)
except:
    log_except()

with open('Const/config.json') as i:
    json_const = json.load(i)

serverStatus = False
device=json_const['DEVICE_FLAG']
DEV_ADDR    =json_const['RMATICS_MAC_ADD']
serverStatus = False
envMode = json_const["ENVIRONMENT"]
durationOfTheGame = 0
GameState = 'unopened'
from matplotlib import style
style.use('ggplot')

def check_dongle():
    from serial.tools import list_ports
    L = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3', '/dev/ttyACM4', '/dev/ttyACM5', '/dev/ttyACM6', '/dev/ttyACM7', '/dev/ttyACM8', '/dev/ttyACM9']
    flag = 0
    for i in L:
        if (os.path.exists(i)):
            flag = 1
            return True
        else:
            try:
                cdc = next(list_ports.grep('Bluegiga Bluetooth Low Energy'))
                flag = 1
                return True
            except:
                flag = 0

    if (flag==0):
        log_except()
        return False

def setExerciseResults(session, result, duration,steps=None):
    try:
        global ExerciseName, canvas1,canvas5,canvas, report_title_id, starttime, ExerciseDuration, MinAngleReached, MaxAngleReached, Reps, PerfectReps
        back.append(4)
        global device
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if (platform.system() == "Linux"): # Using a smaller font size for Linux so that we have the summary listing generated properly
            Fsize = 10
        else:
            Fsize = 12

        # logic to create the frame for summary page starts
        screenheight = root.winfo_screenheight()
        screenWidgth = root.winfo_screenwidth()
        canvas5 = Canvas(root, bg="white", width=900, height=300, bd=0, relief='ridge', highlightthickness=0)
        canvas5.place(x=250, y=210)

        canvas1 = tk.Canvas(root, bg="white", relief='ridge', width=screenWidgth, height=20,
                            highlightbackground="black", highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(screenWidgth / 2, 15, fill="black", font="Times 12 italic bold", text="Game Result")

        canvas5.create_rectangle(50, 70, 850, 110, fill="yellow")
        if ExerciseName == 3 or ExerciseName == 7 :  # Arm & Forearm - Horizontal movement or Pronation & Supination
            canvas5.create_rectangle(50, 110, 850, 150)
            canvas5.create_rectangle(50, 150, 850, 190)
        elif ExerciseName == 9 or ExerciseName == 6 or ExerciseName == 12 or ExerciseName == 11 :
            canvas5.create_rectangle(50, 110, 850, 150)
            canvas5.create_rectangle(50, 150, 850, 190)
        else:
            canvas5.create_rectangle(50, 110, 850, 150)
            canvas5.create_rectangle(50, 150, 850, 190)
            canvas5.create_rectangle(50, 190, 850, 230)
            canvas5.create_rectangle(50, 230, 850, 270)

        report_title_id = canvas5.create_text(450, 90, font=("Helvetica", Fsize),
                                             text="Summary Report for patient ID KN1283 performing Flexion on 19-JAN-2019 ")

        starttime = tk.StringVar()
        ExerciseDuration = "none"
        MinAngleReached = "none"
        MaxAngleReached = "none"
        Reps = "none"
        PerfectReps = "none"

        if ExerciseName == 9 :
                canvas5.create_text(300, 130, font=("Helvetica", Fsize),
                                    text="Exercise Duration                                : ")
                duration_id = canvas5.create_text(600, 130, font=("Helvetica", Fsize),
                                                  text="5 Minutes")
                canvas5.create_text(300, 170, font=("Helvetica", Fsize),
                                    text="Number of steps                                : ")
                no_steps = canvas5.create_text(600, 170, font=("Helvetica", Fsize),
                                                  text="0 Steps")
        elif ExerciseName == 6 or ExerciseName == 3 or ExerciseName == 7 or ExerciseName == 12 or ExerciseName == 11 :
                canvas5.create_text(300, 130, font=("Helvetica", Fsize),
                                    text="Exercise Duration                                : ")
                duration_id = canvas5.create_text(600, 130, font=("Helvetica", Fsize),
                                                  text="5 Minutes")
                canvas5.create_text(300, 170, font=("Helvetica", Fsize),
                                    text="Number of reps                                 : ")
                no_steps = canvas5.create_text(600, 170, font=("Helvetica", Fsize),
                                               text="0 reps")
        else:
            canvas5.create_text(300, 130, font=("Helvetica", Fsize),
                               text="Exercise Duration                                : ")
            duration_id = canvas5.create_text(600, 130, font=("Helvetica", Fsize),
                                             text="5 Minutes")

            canvas5.create_text(300, 170, font=("Helvetica", Fsize),
                               text="Maximum Angle reached                     : ")
            angle_travel_id = canvas5.create_text(600, 170, font=("Helvetica", Fsize),
                                                 text="93 Degrees")

            canvas5.create_text(300, 210, font=("Helvetica", Fsize),
                               text="No of Incomplete Cycle                      :")
            reps_id = canvas5.create_text(600, 210, font=("Helvetica", Fsize), text="0")

            canvas5.create_text(300, 250, font=("Helvetica", Fsize),
                               text=" No of Perfect Cycle                             : ")
            perfects_id = canvas5.create_text(600, 250, font=("Helvetica", Fsize),
                                             text="0")
        # logic to create the frame for summary page ends
        # config the items required for the frame

        exerciseid, patientid, ExerciseName, starttime, game_min_setting, game_max_setting = session
        logging.info("Entered setExerciseResults. ")
        conn = sqlite3.connect(json_const['DB_NAME'])
        c = conn.cursor()
        if device=="S":
            c.execute("SELECT Category,ExerciseName FROM S_ExerciseMaster WHERE ID= '" + str(ExerciseName) + "' LIMIT 1")
        else:
            c.execute(
                "SELECT Category,ExerciseName FROM R_ExerciseMaster WHERE ID= '" + str(ExerciseName) + "' LIMIT 1")
        for row in c.fetchall():
            exerciseType = row[0]
            exercisename = row[1]

        reps, perfects, min_hit, max_hit = result
        initialdate = starttime + 5 * 60 * 60
        finaltime = initialdate + 30 * 60
        if int(duration) <= 60:
            duration_min = 00
            duration_seconds = int(duration)
        else:
            from math import floor
            duration_min = floor(int(duration) / 60)
            duration_seconds = int(duration) % 60
        angle_travel = round((-1) * min_hit + max_hit)
        incomplete = reps - perfects
        logging.info("Duration Min and Sec : " + str(duration_min) + " " + str(duration_seconds).zfill(2))

        date = datetime.datetime.utcfromtimestamp(finaltime).strftime('%d-%m-%Y')
        #time = datetime.utcfromtimestamp(finaltime).strftime('%H:%M:%S')
        canvas5.itemconfigure(report_title_id,  text="Summary Report for patient " + str(patientid) + " performing " + str(
                                              exercisename) + " on " + str(date))
        # summary_page.canvas.itemconfigure(summary_page.start_time_id, text=str(time))
        x=list(range(60, (120+1)*60, 60))
        if duration_seconds in x:
            b = duration_seconds / 60
            canvas5.itemconfigure(duration_id, text=str(int(b))+":"+"00"+ " (mm:ss)")
        elif duration_seconds == 0 :
            canvas5.itemconfigure(duration_id, text=str((duration_min))+":"+"00"+ " (mm:ss)")
        else:
            canvas5.itemconfigure(duration_id,text=str(duration_min) + ":" + str(duration_seconds).zfill(2) + " (mm:ss)")

        logging.info("Exercise : " + exerciseType + " " + exercisename + " no of steps : " + str(steps) )
        if exerciseType == "Forearm Exercise" and exercisename == "Pronation & Supination" or exerciseType == "Hip Exercise" and exercisename == "Adduction & Abduction" \
                or exerciseType == "Ankle Exercise" and exercisename == "Flexion & Extension":
            logging.info("Number of reps in Forearm , Pronation & Supination or Hip or Ankle : " + str(steps))
            canvas5.itemconfigure(no_steps, text=str(steps))
        elif exercisename == "Horizontal Movement" :
            logging.info("Number of reps in Horizontal Movement : " + str(steps))
            canvas5.itemconfigure(no_steps, text=str(steps))
        elif  exercisename == "Walking" :
            logging.info("Number of steps : "+str(steps))
            canvas5.itemconfigure(no_steps, text=str(steps))
        else:
            canvas5.itemconfigure(reps_id, text=str(incomplete))
            canvas5.itemconfigure(perfects_id, text=str(perfects))
            canvas5.itemconfigure(angle_travel_id, text=str(angle_travel)+ " (Degrees)")
    except:
        log_except()

create_soujhe_logs ()

# +++++++++++++++++++++HoverButton +++++++++++++++++++
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
c
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# +++++++++++++++++HoverButton Ended+++++++++++++++++++++++

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

def encode_msg(msg):
    return msg.encode()

def splitMessage(msg):
    result = [x.strip() for x in msg.split(',')]
    return result

def backpage():
    global back,root,report_title,reportGameGraph,ax,GameStats
    if len(back)>0 :
        v=back[-1]
        back=back[:-1]
        if v==1:
            initialmiddlepart()
        elif v==2:
            homemiddlepart(username.get())
        elif v==3:
            registration()
        elif v==4:
            if canvas5 is not None:
                canvas5.config(height=0, width=0)
                canvas5.delete("all")
            gamepage()
        elif v==5:
            reportGameGraph.destroy()
            runreport()
        elif v==6:
            forearmexercise()
        elif v==7:
            wristexercise()
        elif v==8:
            armexercise()
        elif v==9 :
            # adminUser()
            pass
        elif v==10:
            gamepage()
        elif v==11:
            utilities(user=username.get())
        elif v==12:
            upperLimb()
        elif v==13:
            lowerLimb()
        elif v==14:
            utilities(user=username.get())
    else:
        # if messagebox.askyesno("Verify", "Do you want to exit?")==True :
            root.quit()

def saveExerciseResults(session, result, duration,steps=None):
    try:
        global ExerciseName

        ID, patientid, ExerciseName, Starttime, Game_min_setting, Game_max_settings = session
        reps, perfects, min_hit, max_hit = result
        logging.info("Entered saveExerciseResults. ")
        duration_min = int(duration) / 60
        if ExerciseName=="3" or ExerciseName=="7": # Horizontal Movement exercises
            incomplete=0
            perfects=0
        else:
            incomplete = reps - perfects
        conn = sqlite3.connect(json_const['DB_NAME'])
        c = conn.cursor()
        if steps is not None:
            logging.info("Step Count : " + str(steps) )
            c.execute( "UPDATE ExerciseSession SET reps = ?, perfectHits = ?, duration = ?, minAngle = ?, maxAngle= ? WHERE ID = ?",
                (0, 0, duration_min, 0, steps, ID))
        else:
            c.execute( "UPDATE ExerciseSession SET reps = ?, perfectHits = ?, duration = ?, minAngle = ?, maxAngle= ? WHERE ID = ?",
                (incomplete, perfects, duration_min, min_hit, max_hit, ID))
        conn.commit()
    except:
        log_except()

def receive():
    try:

        global game_ended, exercise_result, game_duration,device
        """Handles receiving of messages."""
        while True:
            try:
                msg = s.recv(1024).decode("utf8")
                message_array = splitMessage(msg)

                if message_array[0] == 'data_saved':
                    logging.info("Message in receive : " + str(msg))
                    game_ended = True
                    game_duration = message_array[2]
                    logging.info("Actual game duration : " + str(game_duration))

                    conn = sqlite3.connect(json_const['DB_NAME'])
                    c = conn.cursor()
                    c.execute(
                        "SELECT ID, PatientID, ExerciseID, StartTime, Game_Min_Setting, Game_Max_Setting FROM ExerciseSession WHERE ID=" +
                        message_array[1])
                    session = exerciseid, patientid, exerciseName, starttime, game_min_setting, game_max_setting = c.fetchone()
                    logging.info("Game min and max setting : " + str(game_min_setting) + " " + str(game_max_setting))
                    logging.info("Exercise id : " + str(exerciseid))
                    sensor_data = []
                    if device=="S":
                        c.execute("SELECT * FROM N_RawData WHERE ExerciseID = " + str(exerciseid))
                        if exerciseName == '12' :
                            logging.info("Collecting sensor data for Hip for id " + str(exerciseid))
                            for rawdata in c.fetchall():
                                sensor_data.append(rawdata[-2])
                            logging.info("Length of array is " + str(len(sensor_data)))
                        else:
                            logging.info("Collecting sensor data for others for id " + str(exerciseid))
                            for rawdata in c.fetchall():
                                sensor_data.append(rawdata[-3])
                            logging.info("Length of array is " + str(len(sensor_data)))
                    else:
                        c.execute("SELECT CurrAngle FROM R_RawData WHERE ExerciseID = " + str(exerciseid) +" order by TIME")
                        for rawdata in c.fetchall():
                            sensor_data.append(rawdata[0])  # tilt Y value is second from the end of the db columns
                    exname = ''
                    if device=="S":
                        c.execute("SELECT Category,ExerciseName FROM S_ExerciseMaster WHERE ID= '" + str(exerciseName) + "'")
                    else:
                        c.execute("SELECT Category,ExerciseName FROM R_ExerciseMaster WHERE ID= '" + str(exerciseName) + "'")

                    for row in c.fetchall():
                        extype = row[0]
                        exname = row[1]

                    logging.info("In receive , Exercise name & id : " + str(exname) + ' ' + str(exerciseName))

                    No_of_steps = 0
                    if (exname == 'Adduction & Abduction' and str(exerciseName) == '12') or \
                            (exname == 'Flexion & Extension' and str(exerciseName) == '11')  :
                        No_of_steps = message_array[3]
                    elif exname == 'Flexion & Extension' or exname == 'Adduction & Abduction' :
                        exercise_result = report_generator.arm_exercise_result(sensor_data, game_min_setting,game_max_setting)
                    elif exname == 'Pulley':
                        exercise_result = report_generator.shoulder_exercise_result(sensor_data, game_min_setting,
                                                                                    game_max_setting)
                    elif exname == 'Walking' or exname == 'Pronation & Supination' or exname == 'Horizontal Movement' :
                        No_of_steps=message_array[3]

                    if exname == 'Walking' or exname == 'Pronation & Supination' or exname == 'Horizontal Movement' \
                            or extype == "Hip Exercise" and exname == 'Adduction & Abduction' \
                            or extype == "Ankle Exercise" and exname == 'Flexion & Extension':
                        exercise_result = (0, 0, 0, 0)
                        logging.info("Exercise Result for  " + exname + " : " + str(exercise_result))
                        saveExerciseResults(session, exercise_result, game_duration,No_of_steps)
                        logging.info("Calling setExerciseResults : " + str(session) )
                        setExerciseResults(session, exercise_result, game_duration,No_of_steps)
                    else:
                        logging.info("Exercise Result : " + str(exercise_result))
                        saveExerciseResults(session, exercise_result, game_duration)
                        logging.info("Calling setExerciseResults : " + str(session))
                        setExerciseResults(session, exercise_result, game_duration)

            except OSError:  # Possibly client has left the chat.
                break
    except:
        log_except()

def openFile(filename):
    try:
        cmd = "nope"

        if envMode == "development":
            cmd = "python " + filename + ".py"
        else:
            if (platform.system() == "Windows"):
                cmd = filename + ".exe"
            else:
                cmd = filename

        subprocess.Popen(cmd, shell=True)
    except:
        log_except()

def on_closing():
    try:
        logging.info("On closing ")
        d = dialoguebox(root, text="Do you want to exit the application?", buttons=["Yes", "No"], default=0,
                        cancel=2, title=warn, icon='Pictures/warn.png')
        if (d.go()) == 0:
            logging.info("Sending closing to socket.")
            s.send(encode_msg("closing"))
            time.sleep(1)
            logging.info("Closing the UI socket.")
            s.shutdown(1)
            s.close()
            force_kill()
    except:
        log_except()

def progressKill():

    if (platform.system() == "Linux"):  # Using a smaller closing duration for Windows. Closing of Linux sockets seems to take close to a min.
        a=1.5
        b=60
    else:
        a=1.5
        b=15

    t3 = Toplevel(root)
    t3.transient(canvas5)

    t3.grab_set()
    t3.title("Closing Program.... (Do not close this window)")
    t3.geometry("400x100+500+300")
    t3.focus()
    img = PhotoImage(file="Pictures/info.png")
    t3.tk.call('wm', 'iconphoto', t3._w, img)
    auto_text = Message(t3, text="Closing dependent programs.....", aspect=700, font="Calibri 13 bold", bg="white")
    auto_text.pack(expand=True, fill=BOTH)
    progressBar = ttk.Progressbar(t3, orient="horizontal", length=300, mode="determinate")
    progressBar.pack(expand=False, pady=10)
    # global progressBar
    progressBar['maximum'] = b-1

    for i in range(0, b):
        time.sleep(a)
        progressBar["value"] = i
        progressBar.update()
        progressBar["value"] = 0
        progressBar.step(b-1)
        progressBar.stop()

    def wm_delete_window():
        progressBar["value"] = b-1
        progressBar.stop()
        t3.grab_release()
        t3.withdraw()

    t3.protocol('WM_DELETE_WINDOW', wm_delete_window)
    time.sleep(0.1)
    t3.grab_release()
    t3.withdraw()
    t3.transient(canvas5)

def force_kill():
    try:
        logging.info("In force kill... ")
        if envMode == "development":
            os.system("taskkill /f /im ble_manager.py 1>nul")
            os.system("taskkill /f /im r_ble_manager.py 1>nul")
            os.system("taskkill /f /im database_Server.py 1>nul")
            os.system("taskkill /f /im socket_manager.py 1>nul")
            progressKill()
            remove_soujhe_logs()
            os._exit(0)
        else:
            if (platform.system()=="Windows"):
                os.system("taskkill /f /im ble_manager.exe 1>nul 2>nul")
                os.system("taskkill /f /im r_ble_manager.exe 1>nul 2>nul")
                os.system("taskkill /f /im database_Server.exe 1>nul 2>nul")
                os.system("taskkill /f /im socket_manager.exe 1>nul 2>nul")
                progressKill()
                remove_soujhe_logs()
                os._exit(0)
            else:
                os.system("sudo pkill ble_manager")
                os.system("sudo pkill database_Server")
                os.system("sudo pkill socket_manager")
                progressKill()
                remove_soujhe_logs()
                os._exit(0)
    except:
        log_except()

def testVal(inStr, acttyp):

    try:
        if acttyp == '1':  # insert
            if not inStr.isdigit():
                return False
        return True
    except:
        log_except()

def on_enter(val):
    global auto_text,patient_entry

    if val==1:
        if entry3.get() == "":

            auto_text.configure(text="Enter Patient Id & Click to auto populate patient data.")
        else:
            if val == 1:

                auto_text.configure(text="Click to auto populate " + str(entry3.get()) + "\'s data.")
def on_leave( enter):
    global auto_text
    auto_text.configure(text="")

def checkState(val,type1):

    if val != "":
        result = []
        patientResult(2)  # p_id,bd=3,patientid
        for j in p_id:
            result.append(str(j))

        if val not in result:
            result = []
            patientResult(3)  # p_id,bd=3,patientid
            for j in p_id:
                result.append(str(j))
            # patientResult(3)
            if val in result:

                d = dialoguebox(root, text="      Patient inactive.Make active?", buttons=["Yes", "No"], default=0,
                                cancel=2, title=info, icon='Pictures/info.png')
                if (d.go()) == 0:
                    patientResult(4)
                    excercisetype(type1,val=val,ret=entry3.get())
                else:
                    entry3.focus()
                    return False
            else:
                d = dialoguebox(root, text="Do you want to register the patient ?", buttons=["Yes","No"],
                                default=0,
                                cancel=2, title=info, icon='Pictures/info.png')
                if (d.go()) == 0:
                    registrationUi(val=1,patient=entry3.get())
                else:
                    entry3.focus()

def excercisetype(type1,val=None,ret=None):
    try:

        global canvas5,device,game,auto_text,excategory,disordercombo,progressBar,test_conn,min_angle,clear_button, disorder,start_button, patientid, exercise, entry3, entry4, duration, list_of_items, font_size, canvas1, back, canvas4, angle, entry5, angle_text, duration_text, others, othersvalue, combo
        if val==2:
            back.append(13)
        elif val==2:
            back.append(12)

        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if entry3 is not None:
            entry3.destroy()
        if entry4 is not None:
            entry4.destroy()
        if entry5 is not None:
            entry5.destroy()
        if canvas5 is not None:
            canvas5.delete(text)

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text=type1)
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
        canvas5 = Canvas(root, bg="white", width=1150, height=460, bd=0, relief='ridge',
                         highlightthickness=0)
        canvas5.place(x=150, y=190)
        canvas5.create_text(600, 35, fill="black", font="Times 24 bold", text=type1)
        canvas5.create_text(200, 100, fill="black", font=lable_font, text="Patient ID                 : ")
        canvas5.create_text(750, 100, fill="black", font=lable_font, text="Patient Disorder        : ")
        canvas5.create_text(200, 155, fill="black", font=lable_font, text="Exercise                   : ")
        canvas5.create_text(750, 155, fill="black", font=lable_font, text="Game                         : ")
        duration_text = canvas5.create_text(200, 215, fill="black", font=lable_font,text="Duration (Min)        : ")
        canvas5.create_text(200, 265, fill="black", font=lable_font, text="Others                     : ")
        angle_text = canvas5.create_text(750, 215, fill="black", font=lable_font,text="Angle (Deg)                 : ")
        excategory=type1
        patientid = StringVar()
        duration = StringVar()
        exercise = StringVar()
        others = StringVar()
        othersvalue=StringVar()
        angle = StringVar()
        min_angle = StringVar()
        game=StringVar()
        disorder=StringVar()

        toprightmostpart()
        result=[]
        patientResult(2)#p_id,bd=3,patientid
        for j in p_id:
            result.append(str(j))
        entry3 =AutocompleteCombobox(canvas5,textvariable=patientid, width=10,font=font_size,height=1) #AutocompleteEntry(list_of_items1,canvas5, listboxLength=6,,bd=3, width=11, font=font_size)#Entry(canvas5, textvariable=patientid, bd=3, width=11, font=font_size)
        entry3.set_completion_list(result)
        entry3.grid(row=0, column=0)
        entry3.place(x=360, y=85)
        entry3.focus()
        entry3.delete(0, END)

        def autocapitalize(*arg):
            patientid.set(patientid.get().upper())

        patientid.trace("w", autocapitalize)
        if ret is not None:
            entry3.insert(0,ret)

        auto = HoverButton(canvas5, compound=LEFT, bg="white",
                                      activebackground="blue", image=photo_image12, width=25, height=26,
                                      borderwidth=1,
                                      command=lambda:ChangeKey(str(entry3.get())) , cursor="hand2")
        auto.place(x=515, y=85)

        auto_text = Label(canvas5, text="",bg="white",fg="blue",width=50)
        auto_text.place(x=270, y=118)

        auto.bind("<Enter>", lambda event: on_enter(1))
        auto.bind("<Leave>", on_leave)
        auto.bind("<FocusIn>", lambda event: on_enter(1))
        auto.bind("<FocusOut>", on_leave)
        auto.bind("<FocusIn>", lambda event: fill(entry3.get()))

        def fill(val):

            checkState(val, type1)
            if val!="":
                patientResult(7,val)
                if len(p_id)!=0:
                    disorderDetail=p_id[0][2]
                    disordercombo.set(disorderDetail)
                else:
                    disordercombo.delete(0, END)
                    return False

        patientResult(val=7,val1=entry3.get())
        disordercombo = ttk.Combobox(canvas5, textvariable=disorder, width=10, font=font_size, height=4,state="readonly")#state="readonly"
        disordercombo['values'] = p_id
        disordercombo.delete(0, END)
        disordercombo.place(x=900, y=85)
        disordercombo.focus_set()
        #disordercombo.bind("<Leave>", lambda event: fill(entry3.get()))
        disordercombo.bind("<Enter>", lambda event: fill(entry3.get()))
        disordercombo.bind("<FocusIn>", lambda event: fill(entry3.get()))
        disordercombo.bind("<FocusOut>", lambda event: fill(entry3.get()))

        conn = sqlite3.connect(json_const['DB_NAME'])
        c = conn.cursor()
        if device == "S":
            c.execute("SELECT ExerciseName FROM S_ExerciseMaster WHERE Category= "+"'"+str(type1)+"'")
        else:
            c.execute("SELECT ExerciseName FROM R_ExerciseMaster WHERE Category="+"'"+str(type1)+"'")
        result = []
        for row in c.fetchall():
            result.append(row[0])
        list_of_items = result

        combo = AutocompleteCombobox(canvas5, textvariable=exercise, width=10, font=font_size, height=4)
        combo.set_completion_list(list_of_items)
        combo.place(x=360, y=140)
        combo.focus_set()
        combo.delete(0, END)
        combo.bind("<Enter>", lambda event: fill(entry3.get()))

        gameChoosen = ttk.Combobox(canvas5, textvariable=game, width=10, font=font_size, height=4)
        gameChoosen['values'] = []
        gameChoosen.place(x=900, y=140)
        gameChoosen.bind('<FocusIn>', lambda event: combo_change(exercise.get()))

        entry4 = Entry(canvas5, textvariable=duration, bd=3, width=11, font=font_size, validate="key")
        entry4['validatecommand'] = (entry4.register(testVal), '%P', '%d')
        entry4.place(x=360, y=200)
        entry4.focus()
        entry4.delete(0, END)

        entry5 = Entry(canvas5, textvariable=angle, bd=3, width=11, font=font_size, validate="key")
        entry5['validatecommand'] = (entry5.register(testVal), '%P', '%d')
        entry5.place(x=900, y=200)
        entry5.focus()
        entry5.delete(0, END)

        optionChoosen = ttk.Combobox(canvas5, width=10, textvariable=others, font=font_size, height=2,state="readonly")
        optionChoosen['values'] = optionChoosen_input()
        optionChoosen.bind('<<ComboboxSelected>>', option_change)
        optionChoosen.pack()
        optionChoosen.place(x=360, y=250)
        optionChoosen.set("Select")
        optionChoosen.delete(0, END)
        minangle = canvas5.create_text(200, 320, fill="black", font=lable_font, text="Minimum Angle      : ")

        entry_minangle = ttk.Combobox(canvas5, width=10, textvariable=min_angle, font=font_size, height=2,
                                      state="readonly")

        if device=="S":
            entry_minangle['values'] = ['0','15','30','45','60']
        else:
            entry_minangle['values'] = ['-45','-40','-35','-30','-25','-20','-15','-10','-5','0']

        entry_minangle.place(x=360, y=310)
        entry_minangle.current(0)
        entry_minangle.delete(0, END)

        if type1 == "Arm Exercise" or type1 == "Forearm Exercise" or type1=="Knee Exercise" :# or type1 !="Walking Exercise" or type1 !="Ankle Exercise" or type1 !="Hip Exercise"
            entry_minangle["state"] = "readonly"
            # entry_minangle.config(state="readonly",)
        else:
            entry_minangle["state"] = "disabled"

        start_button = HoverButton(canvas5, text="START GAME", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                             command=lambda: getSelectedOption(type1,key), activebackground='blue', cursor="hand2",width=15)
        start_button.place(x=350, y=360)

        def clearData():

            d = dialoguebox(root, text="Do you want to clear the data?", buttons=["Yes", "No"], default=0,
                            cancel=2, title=warn, icon='Pictures/warn.png')
            if (d.go()) == 0:
                excercisetype(type1)

        clear_button = HoverButton(canvas5, text="CLEAR DATA", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                             command=lambda: clearData(), activebackground='blue', cursor="hand2",width=15)
        clear_button.place(x=550, y=360)
        button3_report = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white", borderwidth=0,
                                     command=backpage, cursor="hand2")
        button3_report.place(x=50, y=580)

        def test():
            if platform.system() == "Windows":
                test_conn.config(cursor="wait")
            else:
                test_conn.config(cursor="xterm red green")
            if (check_dongle()):
                with open('Const/config.json') as i:
                    json_const = json.load(i)
                    mac = json_const['BLE_DEVICE_MAC_ADD']
                try:
                    logging.info('Testing connection to device : ' + mac)
                    adapter = pygatt.BGAPIBackend()
                    adapter.start()
                    dev = adapter.connect(address=mac, address_type=BLEAddressType.random)
                    #dev.subscribe("00001003-0000-5053-4d20-5241454e494c")
                    logging.info('Testing connection - successfully connected to device : ' + mac)
                    # test_conn.config(cursor="")
                    value = dev.char_read("00001003-0000-5053-4d20-5241454e494c")
                    Bat = str(value[0]) + "%"

                    if value[0]>=25:
                        d = dialoguebox(root, text=('Connected to Device : ' + mac), buttons=["OK"], default=0,
                                        cancel=2, title=info, icon='Pictures/info.png')
                        if (d.go()) == 0:
                            start_button["state"] = "normal"
                            test_conn.config(cursor="hand2")
                            entry3.focus()
                            adapter.stop()
                    else:
                        logging.info("Please charge the device. Charge currently at " + str(Bat))
                        d = dialoguebox(root, text="Battery charge is low.\n Please charge the device",
                                        buttons=["OK"],  default=0,  cancel=2, title=warn, icon='Pictures/warn.png')
                        if (d.go()) == 0:
                            start_button["state"] = "disabled"
                            test_conn.config(cursor="hand2")
                            adapter.stop()

                except ( pygatt.exceptions.NotConnectedError, pygatt.backends.bgapi.exceptions.ExpectedResponseTimeout) :
                    logging.info("Testing connection - Unable to connect to Device.Please contact your administrator.")
                    adapter.stop()
                    d = dialoguebox(root, text="Unable to connect to Device.Please \n Contact your administrator.", buttons=["OK"],
                                    default=0, cancel=2, title=error, icon='Pictures/error.png')
                    if (d.go())==0:
                        start_button["state"]="disabled"
                        test_conn.config(cursor="hand2")

            else:
                logging.info("Testing connection - No BLE Dongle found")
                d = dialoguebox(root, text="No BLE Dongle found", buttons=["OK"], default=0,
                                cancel=2, title=error, icon='Pictures/error.png')
                if (d.go()) == 0:
                    start_button["state"] = "disabled"
                    test_conn.config(cursor="hand2")

        def notifOnOff(handle, value):
            global onOffStatus
            # Here B = unsigned int 8 bit data type and < = little-endian byte order.
            onOffStatus = struct.unpack('<B', value)
            onOffStatus = onOffStatus[0]

        # Callback function triggered when CURR_ANGLE_CHAR is updated by RMatic machine.
        def notifCurrAngle(handle, value):
            global currAngle
            # Here B = unsigned int 16 bit and < = little-endian byte order.
            currAngle = struct.unpack('<h', value)
            currAngle = currAngle[0]

        def GotoAngleMode(a,h):
            global dev
            global onOffStatus
            global currAngle
            adapter = pygatt.BGAPIBackend()
            logging.info("Reached angle : "+ str(a) )
            logging.info('Connecting : ' + DEV_ADDR)
            adapter.start()
            dev = adapter.connect(address=DEV_ADDR, address_type=BLEAddressType.random)
            dev.subscribe(ONOFF_CHAR, callback=notifOnOff)
            dev.subscribe(CURR_ANGLE_CHAR, callback=notifCurrAngle)
            logging.info('Connected...')
            while True:
                if h=="Left":
                    hand = 1
                else:
                    hand=0
                dev.char_write(HAND_CHAR, bytearray([int(hand)]))
                angle = a
                angleArr = bytearray(struct.pack("<h", int(angle)))
                dev.char_write(GOTO_ANGLE_CHAR, angleArr)
                # Wait for onOffStatus notification
                time.sleep(0.5)
                # Wait till device is busy, display current angle
                while onOffStatus == 1:
                    logging.info(" Curr Angle " + str(currAngle) )
                    sys.stdout.flush()
                    time.sleep(0.3)

                logging.info("\nTarget angle reached.")
                s.send(encode_msg("Target angle reached"))
                break
            adapter.stop()

        def set_systemdetails(x,y,s):
            global hand,homeangle

            conn = sqlite3.connect(json_const['DB_NAME'])
            c = conn.cursor()
            c.execute("SELECT * FROM SystemDetails ")
            if len(c.fetchall()) >= 1:
                c.execute("DELETE FROM SystemDetails")
                conn.commit()
            c.execute("INSERT INTO SystemDetails (Key, Value) VALUES (?,?)",(y,x))
            conn.commit()
            s.destroy()

        def Cancle(s):
            s.destroy()

        def reset():
            global dev
            global onOffStatus
            global currAngle
            hand=''
            a=''
            reset_window = Toplevel(root)
            reset_window.transient(canvas5)
            reset_window.grab_set()
            reset_window.title("In Progress (Do not close this window)")
            reset_window.geometry("400x100+500+300")
            reset_window.focus()
            img = PhotoImage(file="Pictures/info.png")
            reset_window.tk.call('wm', 'iconphoto', reset_window._w, img)

            adapter = pygatt.BGAPIBackend()
            logging.info('Connecting to : ' + DEV_ADDR)
            adapter.start()
            dev = adapter.connect(address=DEV_ADDR, address_type=BLEAddressType.random)
            dev.subscribe(ONOFF_CHAR, callback=notifOnOff)
            dev.subscribe(CURR_ANGLE_CHAR, callback=notifCurrAngle)
            conn = sqlite3.connect(json_const['DB_NAME'])
            c = conn.cursor()
            c.execute("SELECT * FROM SystemDetails ")
            for row in c.fetchall():
                hand = row[0]
                a = row[1]
            if hand=="Left":
                hand=1
            else:
                hand=0
            dev.char_write(HAND_CHAR, bytearray([int(hand)]))
            angle = a
            angleArr = bytearray(struct.pack("<h", int(angle)))
            dev.char_write(GOTO_ANGLE_CHAR, angleArr)
            logging.info("Curr Angle : " + str(currAngle) )
            if currAngle != int(a):
                while onOffStatus == 1:
                    sys.stdout.write("\r               ")
                    sys.stdout.write("\rCurr Angle %i" % currAngle)
                    s.send(encode_msg(str(currAngle)))
                    sys.stdout.flush()
                    time.sleep(0.3)
            else:
                print("Already in home angle")
            adapter.stop()
            reset_window.grab_release()
            reset_window.withdraw()
            reset_window.transient(canvas5)

        def home():
            global hand,homeangle,radio
            entry4=None
            # entry2=None
            hand = StringVar()
            hand_db=''
            value_db=''

            conn = sqlite3.connect(json_const['DB_NAME'])
            c = conn.cursor()
            c.execute("SELECT Key, Value FROM SystemDetails LIMIT 1")

            for row in c.fetchall():
                hand_db = row[0]
                value_db=str(row[1])
            application_window = Tk()
            application_window.geometry("500x200+400+150")
            application_window.resizable(0,0)

            homeangle=StringVar()
            goangle=StringVar()

            canvas1=Canvas(application_window, highlightthickness=0, width=500, height=200, bd=0, bg="white", relief='ridge')
            canvas1.place(x=5, y=5)
            canvas1.create_text(100, 20, fill="black", font=lable_font, text="Hand              : ")

            handChoosen = ttk.Combobox(canvas1, width=10, textvariable=hand, font=font_size, height=2, state="readonly")

            handChoosen['values'] = ["Right","Left"]
            handChoosen.pack()
            handChoosen.place(x=220, y=5)
            handChoosen.set(hand_db)

            canvas1.create_text(110, 80, fill="black", font=lable_font, text="Current Angle  : ")
            entry4 = Entry(canvas1, textvariable=goangle, bd=3, width=15, font=font_size)
            entry4.insert(0,value_db)
            entry4.place(x=220, y=80)

            set_button = HoverButton(canvas1, text="SET", bg="#007ED9", fg="white", font=('Helvetica', '12'),
                                    command=lambda: GotoAngleMode(entry4.get(),handChoosen.get()), activebackground='blue', cursor="hand2", width=6)
            set_button.place(x=430, y=80)

            ok_button = HoverButton(canvas1, text="SAVE", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                       command=lambda: set_systemdetails(entry4.get(),handChoosen.get(), application_window), activebackground='blue', cursor="hand2", width=8)
            ok_button.place(x=50, y=150)
            go_button = HoverButton(canvas1, text="CANCEL", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                    command=lambda: Cancle(application_window),activebackground='blue', cursor="hand2", width=13)
            go_button.place(x=300, y=150)

        if device == "S":
            global  test_conn
            test_conn = HoverButton(canvas5, text="CHECK CONNECTION", bg="#007ED9", fg="white",font=('Helvetica', '15'),command = lambda: test(), activebackground = 'blue', cursor = "hand2", width = 20)
            test_conn.place(x=750, y=360)
        else:
            home_conn = HoverButton(canvas5, text="SETTINGS", bg="#007ED9", fg="white",
            font = ('Helvetica', '15'),
            command = lambda: home(), activebackground = 'blue', cursor = "hand2", width = 12)
            home_conn.place(x=750, y=360)
            reset_conn = HoverButton(canvas5, text="RESET", bg="#007ED9", fg="white",
                                    font=('Helvetica', '15'),
                                    command=lambda: reset(), activebackground='blue', cursor="hand2", width=12)
            reset_conn.place(x=920, y=360)

        def ChangeKey(event):
            global entry5, angle_text, duration_user, angle_value, othername,start_button
            # exerciseType = ''
            exercisename = ''
            othername = ''
            if entry5 is not None:
                canvas5.delete(text)
            cid = []  # Category Names
            exid = []  # Exercise Names

            #patient_result = []
            conn = sqlite3.connect(json_const['DB_NAME'])
            c = conn.cursor()
            if device=="S":
                c.execute("select * from S_ExerciseMaster where Category='" + str(type1) + "'")
            else:
                c.execute("select * from R_ExerciseMaster where Category='" + str(type1) + "'")
            for row in c.fetchall():
                cid.append(row[0])

            for id in cid:
                c.execute(
                    "select ID,ExerciseID,Exercise_Duration ,Angle,ExerciseCategory_ID,PatientDisorder_ID,Input_Min_Angle from ExerciseSession "
                    "where id= (select max(id) from ExerciseSession where PatientID=" + "'" + event + "' and ExerciseID ='" + str(id) + "' )  ")

                for row in c.fetchall():
                    exid.append(row[0])
            if exid== []:
                d = dialoguebox(root, text="No previous records found.", buttons=["OK"], default=0, cancel=2, title=info, icon='Pictures/info.png')
                d.go()
                # disordercombo.focus_set()
                logging.info("No previous records found for PatientID " + str(event) + " ExerciseID " + str(id) )
            else:
                if canvas5 is not None:
                    canvas5.delete(text)
                maxid = max(exid)
                c.execute("select ExerciseID,Exercise_Duration ,Angle,ExerciseCategory_ID,ID,PatientDisorder_ID,Input_Min_Angle from ExerciseSession where id= '" + str(
                    maxid) + "'")
                patient_result = c.fetchall()
                logging.info("Patient Result : " + str(patient_result))
                angle_value = 0
                #weightvalue = 0

                if len(patient_result) > 0:
                    pid = str(patient_result[0][0])
                    esid=str(patient_result[0][4])

                    if device=="S":
                        c.execute("SELECT Category,ExerciseName FROM S_ExerciseMaster WHERE ID= '" + pid + "' LIMIT 1")
                    else:
                        c.execute("SELECT Category,ExerciseName FROM R_ExerciseMaster WHERE ID= '" + pid + "' LIMIT 1")

                    for row in c.fetchall():
                        #exerciseType = row[0]
                        exercisename = row[1]

                    if exercisename in str(list_of_items):
                        combo.set(exercisename)
                        combo.focus_set()
                        game_change(exercisename)
                    else:
                        combo.set('')
                    db_disorder = patient_result[0][5]
                    c.execute("SELECT ID,Disorder FROM PatientDisorder WHERE ID= '" + str(db_disorder) + "' LIMIT 1")

                    for row in c.fetchall():
                        diorder_db = row[1]
                        disordercombo.set(diorder_db)
                        disordercombo.focus_set()

                    duration_user = patient_result[0][1]

                    entry4.delete(0, END)
                    entry4.insert(0, duration_user)
                    entry4.focus()
                    if type1=="Arm Exercise":
                        min_angleinput = patient_result[0][6]
                        entry_minangle.set(min_angleinput)
                        entry_minangle.focus_set()

                    exercisecat_id = str(patient_result[0][3])
                    c.execute("SELECT CategoryName,CategoryValue FROM ExerciseCategory WHERE ID= '" + exercisecat_id + "' LIMIT 1")
                    for row in c.fetchall():
                        othername = row[0]
                        othervalue = row[1]
                    optionChoosen.set(othername)
                    optionChoosen.focus_set()

                    if canvas5 is not None:
                        canvas5.delete(text)
                    canvas5.create_text(750, 265, fill="black", font=lable_font,text="Others Value              : ")
                    if others.get() == "Weight(kg)":
                        conn = sqlite3.connect(json_const['DB_NAME'])
                        c = conn.cursor()
                        c.execute("SELECT Weight_Value FROM ExerciseSession WHERE ID= '" + str(esid) + "' LIMIT 1")
                        logging.info("SELECT Weight_Value FROM ExerciseSession WHERE ID= '" + str(esid) + "' LIMIT 1")
                        weightvalue = c.fetchall()

                        weightChoosen = ttk.Combobox(canvas5, width=10,textvariable=othersvalue, state='readonly',
                                                 font=font_size, height=3)
                        weightChoosen['values'] = ["0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5", "5.5", "6"]
                        weightChoosen.place(x=900, y=250)
                        weightChoosen.set(weightvalue)

                    elif others.get() == "None" or others.get() == "":
                        suboptionChoosen = ttk.Combobox(canvas5, width=10, textvariable=othersvalue, state='readonly',
                                                    font=font_size, height=2)
                        suboptionChoosen['values'] = ''
                        suboptionChoosen.place(x=900, y=250)
                    else:
                        conn = sqlite3.connect(json_const['DB_NAME'])
                        c = conn.cursor()
                        c.execute("SELECT CategoryValue FROM ExerciseCategory WHERE CategoryName='" + othername + "' ")
                        result = []
                        for row in c.fetchall():
                            result.append(row[0])

                        suboptionChoosen = ttk.Combobox(canvas5, width=10, textvariable=othersvalue, state='readonly', font=font_size, height=2)
                        suboptionChoosen['values'] = result
                        suboptionChoosen.place(x=900, y=250)
                        suboptionChoosen.set(othervalue)

                    if exercise.get() == 'Pulley' or exercise.get() == "Horizontal Movement" or exercise.get() == "Pronation & Supination" or \
                            type1=="Walking Exercise" or type1=="Hip Exercise" or (type1 == "Wrist Exercise" and exercise.get() == "Flexion & Extension"):
                        entry5.insert(END, "Not Required")
                        entry5.config(state='disabled')
                    else:
                        angle_value = patient_result[0][2]
                        entry5.destroy()

                        entry5 = Entry(canvas5, textvariable=angle, bd=3, width=11, font=font_size, validate="key")
                        entry5['validatecommand'] = (entry5.register(testVal), '%P', '%d')
                        entry5.place(x=900, y=200)
                        entry5.delete(0, END)

                    if entry5.winfo_exists():
                        entry5.insert(0, angle_value)
                else:
                    combo.set('')
                    entry4.delete(0, END)
                    if entry5.winfo_exists():
                        entry5.delete(0, END)

        def combo_change(event):
            game_change(exercise.get())
            global entry5, entry4, angle, angle_text, armexercise, duration_text,duration,optionChoosen,start_button
            text_exercise="Please select a valid exercise."
            warn="                                                    Warning"
            if exercise.get() in str(list_of_items):
                global duration_user, angle_value, othername,entry5
                if exercise.get() == 'Pulley' or exercise.get() =="Horizontal Movement" or exercise.get() =="Pronation & Supination" or \
                        type1=="Walking Exercise" or type1=="Hip Exercise" or  (type1 == "Wrist Exercise" and exercise.get() =="Flexion & Extension") \
                        or (type1 == "Ankle Exercise" and exercise.get() =="Flexion & Extension"):
                    if entry5 is not None:
                        entry5.delete(0,END)
                    if  exercise.get() =="Horizontal Movement"  or exercise.get() =="Pronation & Supination"  or  exercise.get() =="Pulley"  or \
                            (type1=="Hip Exercise" and  exercise.get() == "Adduction & Abduction") or \
                            (type1 == "Ankle Exercise" and exercise.get() == "Flexion & Extension") or \
                            (type1 == "Walking Exercise" and exercise.get() == "Walking") :
                        entry_minangle["state"] = 'disabled'
                    else:
                        entry_minangle["state"] = 'readonly'

                    entry5.insert(END, "Not Required")
                    entry5.config(state='disabled')
                    entry4.destroy()

                    entry4 = Entry(canvas5, textvariable=duration, bd=3, width=11, font=font_size, validate="key")
                    entry4['validatecommand'] = (entry4.register(testVal), '%P', '%d')
                    entry4.place(x=360, y=200)
                    entry4.focus()

                    optionChoosen = ttk.Combobox(canvas5, width=10, textvariable=others, font=font_size, height=2,state="readonly")
                    optionChoosen['values'] = optionChoosen_input()
                    optionChoosen.bind('<<ComboboxSelected>>', option_change)
                    optionChoosen.pack()
                    optionChoosen.place(x=360, y=250)
                    optionChoosen.focus_set()
                    optionChoosen.delete(0, END)

                    start_button = HoverButton(canvas5, text="START GAME", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                         command=lambda: getSelectedOption(type1,key), activebackground='blue',  cursor="hand2",width=15)
                    start_button.place(x=350, y=360)
                else:
                    entry_minangle["state"] = "readonly"
                    entry5.destroy()
                    entry4 = Entry(canvas5, textvariable=duration, bd=3, width=11, font=font_size, validate="key")
                    entry4['validatecommand'] = (entry4.register(testVal), '%P', '%d')
                    entry4.place(x=360, y=200)
                    entry4.focus()

                    angle = StringVar()

                    entry5 = Entry(canvas5, textvariable=angle, bd=3, width=11, font=font_size, validate="key")
                    entry5['validatecommand'] = (entry5.register(testVal), '%P', '%d')
                    entry5.place(x=900, y=200)
                    entry5.focus()
                    entry5.delete(0, END)

                    optionChoosen = ttk.Combobox(canvas5, width=10, textvariable=others, font=font_size, height=2,state="readonly")

                    optionChoosen['values'] = optionChoosen_input()
                    optionChoosen.bind('<<ComboboxSelected>>', option_change)
                    optionChoosen.pack()
                    optionChoosen.place(x=360, y=250)
                    optionChoosen.focus_set()
                    optionChoosen.delete(0, END)

                    start_button = HoverButton(canvas5, text="START GAME", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                         command=lambda: getSelectedOption(type1,key), activebackground='blue',  cursor="hand2",width=15)
                    start_button.place(x=350, y=360)
            else:
                d = dialoguebox(root, text=text_exercise, buttons=["OK"], default=0, cancel=2, title=warn, icon='Pictures/warn.png')
                d.go()
                combo.focus_set()

                return False
        combo.bind('<<ComboboxSelected>>', lambda event: combo_change(exercise.get()))
        optionChoosen.bind('<<ComboboxSelected>>', option_change)
    except:
        log_except()

def notifOnOff(handle, value):
    global onOffStatus
    #Here B = unsigned int 8 bit data type and < = little-endian byte order.
    onOffStatus = struct.unpack('<B', value)
    onOffStatus = onOffStatus[0]

#Callback function triggered when CURR_ANGLE_CHAR is updated by machine.
def notifCurrAngle(handle, value):
    global currAngle
    #Here B = unsigned int 16 bit and < = little-endian byte order.
    currAngle = struct.unpack('<h', value)
    currAngle = currAngle[0]

def checkAngle():
    global dev
    global onOffStatus
    global currAngle
    hand = ''
    a = ''
    adapter = pygatt.BGAPIBackend()
    logging.info(' Connecting to : ' + str(DEV_ADDR) )
    adapter.start()
    dev = adapter.connect(address=DEV_ADDR, address_type=BLEAddressType.random)
    dev.subscribe(ONOFF_CHAR, callback=notifOnOff)
    dev.subscribe(CURR_ANGLE_CHAR, callback=notifCurrAngle)
    conn = sqlite3.connect(json_const['DB_NAME'])
    c = conn.cursor()
    c.execute("SELECT * FROM SystemDetails ")
    for row in c.fetchall():
        hand = row[0]
        a = row[1]
    if hand == "Left":
        hand = 1
    else:
        hand = 0
    dev.char_write(HAND_CHAR, bytearray([int(hand)]))
    angle = a
    angleArr = bytearray(struct.pack("<h", int(angle)))
    dev.char_write(GOTO_ANGLE_CHAR, angleArr)
    sys.stdout.write("\rCurr Angle %i" % currAngle)
    if currAngle != int(a):
        while onOffStatus == 1:
            sys.stdout.write("\r               ")
            sys.stdout.write("\rCurr Angle %i" % currAngle)
            s.send(encode_msg(str(currAngle)))
            sys.stdout.flush()
            time.sleep(0.3)
    else:
        logging.info("Already at home angle.")
    adapter.stop()

def getSelectedOption(type1,flager=None):
    try:
        global combo, start_button, progressBar, test_conn, clear_button, t2
        #patientResult(3)
        result = []
        patientResult(3)
        for j in p_id:
            result.append(str(j))
        if entry3.get() not in result:
            logging.info("Patient is not registered.")
            d = dialoguebox(root, text="             Patient id not found.\n Do you want to register the patient ?",
                            buttons=["Yes", "No"], default=0, cancel=2,
                            title=info, icon='Pictures/info.png')
            if (d.go()) == 0:
                registrationUi(1, patient=str(entry3.get()))
            return False

        with open('Const/license.json') as i:
            json_const = json.load(i)
            data = json_const["6645463761731833437447950861006883695971924"]  # 237007384299206171504696
            mBytes2 = data.to_bytes(((data.bit_length() + 7) // 8), byteorder="big")
            json_CurCount1 = mBytes2.decode("utf-8")
            json_CurCount=int(json_CurCount1)

        if json_CurCount>0:
            if platform.system() == "Windows":
                start_button.config(state="disabled", cursor="wait")
                clear_button.config(state="disabled", cursor="wait")
            else:
                start_button.config(state="disabled", cursor="xterm red green")
                clear_button.config(state="disabled", cursor="xterm red green")
            if device == "S":
                if platform.system() == "Windows":
                    test_conn.config(state="disabled", cursor="wait")
                else:
                    test_conn.config(state="disabled", cursor="xterm red green")
            # checkState(str(entry3.get()),type1)
            if flager==1:
                patientResult(5)
            def StartGameCheck(type1):
                global flag
                flag = False
                if device=="S":
                    if type1 == "Arm Exercise" or type1 == "Forearm Exercise" or type1 == "Wrist Exercise" or type1 == "Knee Exercise" or type1 == "Walking Exercise"or type1 == "Hip Exercise" or type1 == "Ankle Exercise":
                        flag = armcheck(type1)
                else:
                    if type1 == "Arm Exercise" or type1 == "Forearm Exercise" :
                        flag = armcheck(type1)
                return flag

            def armcheck(type1):

                global patientid, duration, exercise, angle, combo,min_angle,device
                start_button.config(state="normal", cursor="hand2")
                if device=="S":
                    test_conn.config(state="normal", cursor="hand2")
                clear_button.config(state="normal", cursor="hand2")
                db_patient_name = str(entry3.get())
                db_duration = duration.get()
                db_exercise_name = exercise.get()
                db_angle = angle.get()

                text_pdetails="Please enter valid patient details."
                text_pid="Please enter a valid patient ID."
                text_duration="Enter duration for the exercise."
                text_duration_less_than_hour = "Enter duration less than an hour."
                text_angle="Please enter angle for the exercise. "
                text_exercise="Please select a valid exercise."
                text_angle_less_than_180 = "Enter angle less than 180."
                text_angle_greater_than_0 = "Enter angle greater than 0."
                text_duration_greater_than_0 = "Enter duration greater than 0."

                if db_exercise_name is not None and db_exercise_name != "Select" and db_exercise_name == "Pulley" or \
                        db_exercise_name == "Horizontal Movement" or db_exercise_name == "Pronation & Supination" or \
                        (type1 == "Wrist Exercise" and db_exercise_name == "Flexion & Extension") or \
                        (type1 == "Walking Exercise" and db_exercise_name == "Walking") or \
                        (type1 == "Hip Exercise" and db_exercise_name == "Adduction & Abduction" ) or \
                        (type1 == "Ankle Exercise" and db_exercise_name == "Flexion & Extension") :
                    if db_patient_name is '' and db_duration is '':

                        d = dialoguebox(root, text=text_pdetails, buttons=["OK"], default=0, cancel=2,
                                        title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry3.focus()

                    elif db_patient_name is '':
                        d = dialoguebox(root, text=text_pid, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry3.focus()

                    elif db_duration is '':
                        d = dialoguebox(root, text=text_duration, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry4.focus()
                    elif int(db_duration) == 0:
                        d = dialoguebox(root, text=text_duration_greater_than_0, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry4.focus()
                    elif int(db_duration) > 60:
                        d = dialoguebox(root, text=text_duration_less_than_hour, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry4.focus()
                    else:
                        durationOfTheGame = db_duration
                        return True
                else:
                    if db_patient_name is '' and db_duration is '' and db_exercise_name == "Select":
                        d = dialoguebox(root, text=text_pdetails, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry3.focus()

                    elif db_patient_name is '':
                        d = dialoguebox(root, text=text_pid, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry3.focus()
                    elif db_exercise_name == "Select" or db_exercise_name == "":
                        d = dialoguebox(root, text=text_exercise, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        combo.focus_set()
                    elif db_duration is '':
                        d = dialoguebox(root, text=text_duration, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry4.focus()
                    elif int(db_duration) == 0:
                        d = dialoguebox(root, text=text_duration_greater_than_0, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry4.focus()
                    elif int(db_duration) > 60:
                        d = dialoguebox(root, text=text_duration_less_than_hour, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry4.focus()
                    elif db_angle is '':
                        d = dialoguebox(root, text=text_angle, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry5.focus()
                    elif int(db_angle) == 0:
                        d = dialoguebox(root, text=text_angle_greater_than_0, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry5.focus()
                    elif int(db_angle) > 180:
                        d = dialoguebox(root, text=text_angle_less_than_180, buttons=["OK"], default=0,
                                        cancel=2, title=warn, icon='Pictures/warn.png')
                        d.go()
                        entry5.focus()
                    else:
                        durationOfTheGame = db_duration
                        logging.info("Duration of the game : " + str(durationOfTheGame))
                        return True

            if StartGameCheck(type1):
                global t2,errorval,adapter
                if (check_dongle()):
                    if device == "S":
                        t2 = Toplevel(root)
                        t2.transient(canvas5)

                        t2.grab_set()
                        t2.title("Progress Bar (Do not close this window)")
                        t2.geometry("400x100+500+300")
                        t2.focus()
                        img = PhotoImage(file="Pictures/info.png")
                        t2.tk.call('wm', 'iconphoto', t2._w, img)

                        logging.info("Starting the game checks.")

                        if platform.system() == "Windows":
                            start_button.config(state="disabled", cursor="wait")
                            test_conn.config(state="disabled", cursor="wait")
                            clear_button.config(state="disabled", cursor="wait")
                        else:
                            start_button.config(state="disabled", cursor="xterm red green")
                            test_conn.config(state="disabled", cursor="xterm red green")
                            clear_button.config(state="disabled", cursor="xterm red green")

                        auto_text = Message(t2, text="Checking Device status", aspect=700, font="Calibri 13 bold", bg="white")
                        auto_text.pack(expand=True, fill=BOTH)
                        progressBar = ttk.Progressbar(t2, orient="horizontal", length=300, mode="determinate")
                        progressBar.pack(expand=False,pady=10)
                        # global progressBar
                        progressBar['maximum'] = 100

                        for i in range(0,6):
                            time.sleep(0.05)
                            progressBar["value"] = i
                            progressBar.update()
                            progressBar["value"] = 0
                            progressBar.step(5)
                        auto_text.destroy()
                        auto_text = Message(t2, text="Checking for BLE Dongle", aspect=700, font="Calibri 13 bold", bg="white")
                        auto_text.pack(expand=True, fill=BOTH)
                        progressBar.place(y=80)
                        progressBar.pack(pady=10)

                        for i in range(5, 51):
                            # auto_text["text"]=""
                            time.sleep(0.15)
                            progressBar["value"] = i
                            progressBar.update()
                            progressBar["value"] = 0
                            progressBar.step(50)

                        with open('Const/config.json') as i:
                            json_const = json.load(i)
                            mac = json_const['BLE_DEVICE_MAC_ADD']

                        auto_text.destroy()
                        auto_text = Message(t2, text="Checking Device Connection", aspect=700, font="Calibri 13 bold",   bg="white")
                        auto_text.pack(expand=True, fill=BOTH)
                        try:
                            progressBar.place(y=80)
                            progressBar.pack(pady=10)
                            for i in range(50, 76):
                                time.sleep(0.35)
                                progressBar["value"] = i
                                progressBar.update()
                                progressBar["value"] = 0
                                progressBar.step(75)

                            logging.info('Testing connection to device : ' + mac)
                            def startDevice():
                                global errorval,t2,auto_text,adapter
                                try:
                                    adapter = pygatt.BGAPIBackend()
                                    adapter.start()
                                    dev = adapter.connect(address=mac, address_type=BLEAddressType.random,timeout=1)
                                    #dev.subscribe("00001003-0000-5053-4d20-5241454e494c")
                                    logging.info('Testing connection - successfully connected to device : ' + mac)
                                    value = dev.char_read("00001003-0000-5053-4d20-5241454e494c")
                                    Bat = str(value[0]) + "%"
                                    if value[0] >= 25:
                                        auto_text.destroy()
                                        auto_text = Message(t2, text=('Connected to Device : '+str(mac)), aspect=700, font="Calibri 13 bold",
                                                            bg="white")
                                        auto_text.pack(expand=True, fill=BOTH)
                                        time.sleep(2)
                                        progressBar.place(y=80)
                                        progressBar.pack(pady=10)
                                        for i in range(76, 81):
                                            time.sleep(0.8)
                                            progressBar["value"] =i
                                            progressBar.update()
                                            progressBar["value"] = 0
                                            progressBar.step(80)
                                        adapter.stop()
                                        if exercise.get() in str(list_of_items):
                                            auto_text.destroy()
                                            auto_text = Message(t2, text="Launching The Game",   aspect=700, font="Calibri 13 bold", bg="white")
                                            auto_text.pack(expand=True, fill=BOTH)
                                            time.sleep(1)
                                            progressBar.place(y=80)
                                            progressBar.pack(pady=10)

                                            for i in range(81, 91):
                                                time.sleep(0.15)
                                                progressBar["value"] = i
                                                progressBar.update()
                                                progressBar["value"] = 0
                                                progressBar.step(90)
                                            SocketPatientID = patientid.get()
                                            SocketExerciseType = type1
                                            SocketExerciseName = exercise.get()
                                            Socketdisordervalue = disorder.get()
                                            Socketgamepath = game.get()
                                            if type1=="Arm Exercise":
                                                socketminangle = min_angle.get()
                                            else:
                                                socketminangle = 0

                                            conn = sqlite3.connect(json_const['DB_NAME'])
                                            c = conn.cursor()
                                            if device == "S":
                                                c.execute( "SELECT ID FROM S_ExerciseMaster WHERE Category= '" + SocketExerciseType + "' AND ExerciseName= '" + SocketExerciseName + "'")
                                            else:
                                                c.execute( "SELECT ID FROM R_ExerciseMaster WHERE Category= '" + SocketExerciseType + "' AND ExerciseName= '" + SocketExerciseName + "'")

                                            for row in c.fetchall():
                                                exerciseType = row[0]

                                            logging.info('Selecting ID for : ' + str(SocketExerciseType) + ' and ' + str(
                                                    SocketExerciseName))
                                            SocketDuration = duration.get()
                                            if SocketExerciseName == "Pulley":
                                                SocketAngle = str(0)
                                            else:
                                                SocketAngle = angle.get() if angle.get() else str(0)

                                            logging.info("Exercise selected : " + SocketExerciseName)
                                            logging.info("Sent details to Socket Manager.")
                                            if others.get() == '' or others.get() == 'None':
                                                Socketothers = ''
                                                Socketothersvalue = ''
                                            else:
                                                Socketothers = others.get()
                                                Socketothersvalue = othersvalue.get()
                                                if Socketothers == "Select":
                                                    Socketothers = "None"

                                            if SocketExerciseName == 'Horizontal Movement':
                                                socket_manager_msg = "set_apple_details," + SocketPatientID + "," + str(
                                                    exerciseType) + "," + SocketDuration + "," + Socketothers + "," + str(
                                                    Socketothersvalue) + "," + str(Socketdisordervalue) + "," + str(
                                                    Socketgamepath)
                                                logging.info("Set Apple Details : " + socket_manager_msg)
                                                s.send(socket_manager_msg.encode())

                                            else:
                                                socket_manager_msg = "set_game_details," + SocketPatientID + "," + str(
                                                    exerciseType) + "," + SocketDuration + "," + SocketAngle + "," + Socketothers + "," + str(
                                                    Socketothersvalue) + "," + str(Socketdisordervalue) + "," + str(
                                                    Socketgamepath)+"," + str(socketminangle)
                                                logging.info("Set Game Details : " + socket_manager_msg)
                                                s.send(socket_manager_msg.encode())
                                            time.sleep(3)  # Sleep for 3 seconds before checking the process table
                                        else:
                                            text_exercise = "Please select a valid exercise."

                                            d = dialoguebox(root, text=text_exercise, buttons=["OK"],
                                                            default=0,  cancel=2, title=warn, icon='Pictures/warn.png')
                                            d.go()
                                            combo.focus_set()
                                            return False

                                        time.sleep(6)
                                        procObjList = [procObj for procObj in psutil.process_iter() if
                                                       'game' in procObj.name().lower()] or [procObj for procObj in psutil.process_iter() if'apple' in procObj.name().lower()]

                                        if procObjList != []:
                                            logging.info("Details of Processes : " + str(procObjList))
                                            for i in range(91, 101):
                                                time.sleep(0.15)
                                                progressBar["value"] = i
                                                progressBar.update()
                                                progressBar["value"] = 0
                                                progressBar.step(100)
                                                progressBar.stop()

                                            start_button.config(state="normal", cursor="hand2")
                                            test_conn.config(state="normal", cursor="hand2")
                                            clear_button.config(state="normal", cursor="hand2")
                                            p = canvas5.delete("auto_text")
                                            t2.grab_release()
                                        else:
                                            d = dialoguebox(root,
                                                            text="Game not launched. Please \ncontact your Administrator.",
                                                            buttons=["OK"],  default=0,
                                                            cancel=2, title=error, icon='Pictures/error.png')
                                            if d.go() == 0:
                                                logging.info("Failed to launch the game.")
                                                # progressBar.stop()
                                                start_button.config(state="normal", cursor="hand2")
                                                test_conn.config(state="normal", cursor="hand2")
                                                clear_button.config(state="normal", cursor="hand2")
                                                auto_text.destroy()
                                                auto_text = Message(t2, text="Failed to launch the game.",
                                                                    aspect=700, font="Calibri 13 bold",    bg="white")
                                                auto_text.pack(expand=True, fill=BOTH)
                                                adapter.stop()
                                                time.sleep(0.1)
                                                t2.grab_release()
                                                t2.withdraw()
                                    else:
                                        logging.info("Device needs charging.")
                                        d = dialoguebox(root, text="Battery charge is low.\n Please charge the device",
                                                        buttons=["OK"],   default=0,
                                                        cancel=2, title=warn, icon='Pictures/warn.png')
                                        if (d.go()) == 0:
                                            adapter.stop()
                                            start_button.config(state="normal", cursor="hand2")
                                            test_conn.config(state="normal", cursor="hand2")
                                            clear_button.config(state="normal", cursor="hand2")
                                            p = canvas5.delete("auto_text")
                                            progressBar.stop()
                                            t2.grab_release()
                                            t2.withdraw()
                                except:
                                    log_except()
                                    errorval=errorval+1
                                    if errorval>5:
                                        adapter.stop()
                                        progressBar.stop()
                                        d = dialoguebox(root,text="Unable to connect to Device.Please \n Contact your administrator.",
                                                        buttons=["OK"],
                                                        default=0, cancel=2, title=error, icon='Pictures/error.png')
                                        if (d.go()) == 0:
                                            start_button.config(state="normal", cursor="hand2")
                                            test_conn.config(state="normal", cursor="hand2")
                                            clear_button.config(state="normal", cursor="hand2")
                                    else:
                                        adapter.stop()
                                        startDevice()

                                    adapter.stop()
                            startDevice()
                        except ( pygatt.exceptions.NotConnectedError, pygatt.backends.bgapi.exceptions.ExpectedResponseTimeout) :
                                logging.info("During Start game - Unable to connect to Device.Please contact your administrator.")
                                adapter.stop()
                                progressBar.stop()

                                d = dialoguebox(root, text="Unable to connect to Device.Please \n Contact your administrator.", buttons=["OK"],
                                            default=0, cancel=2, title=error, icon='Pictures/error.png')
                                if (d.go())==0:
                                    start_button.config(state="normal", cursor="hand2")
                                    test_conn.config(state="normal", cursor="hand2")
                                    clear_button.config(state="normal", cursor="hand2")

                                    t2.grab_release()
                                    t2.withdraw()

                        def wm_delete_window():
                            progressBar["value"] = 100
                            progressBar.stop()
                            t2.grab_release()
                            t2.withdraw()

                        t2.protocol('WM_DELETE_WINDOW', wm_delete_window)
                        time.sleep(0.1)
                        t2.grab_release()
                        t2.withdraw()
                        t2.transient(canvas5)
                    else:
                        checkAngle()
                        SocketPatientID = patientid.get()
                        SocketExerciseType = type1
                        SocketExerciseName = exercise.get()
                        Socketdisordervalue = disorder.get()
                        Socketgamepath = game.get()
                        socketminangle = min_angle.get()
                        SocketDuration = duration.get()
                        SocketAngle = angle.get() if angle.get() else str(0)
                        with open('Const/config.json') as i:
                            json_const = json.load(i)
                        conn = sqlite3.connect(json_const['DB_NAME'])
                        c = conn.cursor()
                        c.execute( "SELECT ID FROM R_ExerciseMaster WHERE Category= '" + SocketExerciseType + "' AND ExerciseName= '" + SocketExerciseName + "'")

                        for row in c.fetchall():
                            exerciseType = row[0]

                        logging.info('Selecting ID for : ' + str(SocketExerciseType) + ' and ' + str(
                            SocketExerciseName))

                        if others.get() == '' or others.get() == 'None':
                            Socketothers = ''
                            Socketothersvalue = ''
                        else:
                            Socketothers = others.get()
                            Socketothersvalue = othersvalue.get()
                            if Socketothers == "Select":
                                Socketothers = "None"

                        socket_manager_msg = "set_game_details," + SocketPatientID + "," + str(
                            exerciseType) + "," + SocketDuration + "," + SocketAngle + "," + Socketothers + "," + str(
                            Socketothersvalue) + "," + str(Socketdisordervalue) + "," + str(
                            Socketgamepath) + "," + str(socketminangle)

                        logging.info("Set Game Details : " + socket_manager_msg)
                        s.send(socket_manager_msg.encode())
                else:
                    logging.info("Testing connection - No BLE Dongle found")

                    d = dialoguebox(root, text="No BLE Dongle found", buttons=["OK"], default=0,
                                    cancel=2, title=error, icon='Pictures/error.png')
                    if (d.go())==0:
                        start_button.config(state="normal",cursor="hand2")
                        test_conn.config(state="normal", cursor="hand2")
                        clear_button.config(state="normal", cursor="hand2")
        else: # License Count greater than 0
            d = dialoguebox(root, text=" All sessions have been exhausted.", buttons=["OK"],
                            default=0, cancel=2, title=error, icon='Pictures/error.png')
            d.go()
            logging.info("All sessions have been exhausted.")
            force_kill()
    except:
        log_except()

def disorder_input():
    try:
        conn = sqlite3.connect(json_const['DB_NAME'])
        c = conn.cursor()
        c.execute("SELECT Disorder FROM PatientDisorder ")
        result = []

        for row in c.fetchall():
            result.append(row[0])
        result_disorder = list(dict.fromkeys(result))
        del result_disorder[result_disorder.index("Add Disorder")]
        lengtgh=int(len(result_disorder))
        result_disorder.insert(lengtgh+1,"Add Disorder")

        return (result_disorder)
    except:
        log_except()

def optionChoosen_input():
    try:
        conn = sqlite3.connect(json_const['DB_NAME'])
        c = conn.cursor()
        c.execute("SELECT CategoryName FROM ExerciseCategory ")
        result = []
        result.append("None")
        for row in c.fetchall():
            result.append(row[0])
        result = list(dict.fromkeys(result))

        return (result)
    except:
        log_except()

def game_change(e):
    global excategory,device

    t=excategory
    ex_id = ''
    array=[]
    game_list=[]

    conn = sqlite3.connect(json_const['DB_NAME'])
    c = conn.cursor()
    if device=="S":
        c.execute("SELECT ID FROM S_ExerciseMaster WHERE Category= '" + str(t) + "'AND ExerciseName='" + str(e) + "' ")
    else:
        c.execute("SELECT ID FROM R_ExerciseMaster WHERE Category= '" + str(t) + "'AND ExerciseName='" + str(e) + "' ")

    for row in c.fetchall():
        ex_id = str(row[0])

    with open('Const/game.json') as i:
        game_const = json.load(i)

    for key in game_const:
        if key == ex_id:
            array=(game_const[key])
    for k in array:
        game_list.append(k)

    gameChoosen = ttk.Combobox(canvas5,textvariable=game, width=10, font=font_size, height=4,state="readonly")
    gameChoosen['values'] = game_list
    gameChoosen.place(x=900, y=140)
    gameChoosen.focus_set()

    if len(game_list) >0:
        gameChoosen.current(0)
    else:
        logging.info("Enter valid exercise")

def option_change(optionChoosen):
    try:
        global others,othersvalue,canvas5,text

        if canvas5 is not None:
            canvas5.delete(text)
        othersvalue = StringVar()
        text=canvas5.create_text(750, 265, fill="black", font=lable_font, text="Others Value              : ")
        if others.get() == "Weight(kg)":
            weightChoosen = ttk.Combobox(canvas5, width=10, textvariable=othersvalue, state='readonly', font=font_size,height=3)
            weightChoosen['values'] = ["0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5", "5.5", "6"]
            weightChoosen.place(x=900, y=250)
            weightChoosen.current(0)
        elif others.get() == "None":
            suboptionChoosen = ttk.Combobox(canvas5, width=10, textvariable=othersvalue, state='readonly',font=font_size,height=2)
            suboptionChoosen['values'] = ''
            suboptionChoosen.place(x=900, y=250)
        else:
            conn = sqlite3.connect(json_const['DB_NAME'])
            c = conn.cursor()
            c.execute("SELECT CategoryValue FROM ExerciseCategory WHERE CategoryName='" + others.get() + "' ")
            result = []
            for row in c.fetchall():
                result.append(row[0])
            suboptionChoosen = ttk.Combobox(canvas5, width=10, textvariable=othersvalue, state='readonly',
                                            font=font_size, height=2)
            suboptionChoosen['values'] = result
            suboptionChoosen.place(x=900, y=250)
            suboptionChoosen.current(0)
    except:
        log_except()

def armexercise(val=None) :
    excercisetype("Arm Exercise",val)

def forearmexercise(val=None) :
    excercisetype("Forearm Exercise",val)

def wristexercise(val=None) :
    excercisetype("Wrist Exercise",val)
def kneeExercise(val=None) :
    excercisetype("Knee Exercise",val)
def ankleExercise(val=None) :
    excercisetype("Ankle Exercise",val)
def hipExercise(val=None) :
    excercisetype("Hip Exercise",val)
def walkingExercise(val=None) :
    excercisetype("Walking Exercise",val)

def runreport() :
    try:
        global canvas5, patientid, exercise1, entry3, font_size, canvas1, back, canvas4, entry5,exeType,exeValue,result1,result2
        back.append(2)
        patientid = StringVar()
        exeType = StringVar()
        exeValue = StringVar()
        reportStart = StringVar()
        reportEnd = StringVar()
        exercise=""
        result1=""
        result2=""
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if entry5 is not None:
            entry5.destroy()
            canvas5.delete(angle_text)

        canvas5.config(height=0, width=0)
        canvas5.delete("all")

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",  highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Reports")

        canvas5 = Canvas(root, bg="white", width=750, height=400, bd=0, relief='ridge',
                         highlightthickness=0)  # , highlightbackground="black", highlightthickness=5)# highlightthickness=0)
        canvas5.place(x=350, y=190)
        canvas5.create_text(270, 20, fill="black", font="Times 25 italic bold", text="Patient Reports")
        canvas5.create_text(150, 110, fill="black", font="Times 20 italic bold", text="Patient ID : ")
        canvas5.create_text(140, 180, fill="black", font="Times 20 italic bold", text=" Exercise     : ")
        canvas5.create_text(70, 245, fill="black", font="Times 20 italic bold", text=" Start Date  : ")
        canvas5.create_text(420, 245, fill="black", font="Times 20 italic bold", text=" End Date  : ")

        entry3 = Entry(canvas5, textvariable=patientid, bd=3, width=19, font=font_size)

        entry3.place(x=250, y=95)
        entry3.delete(0, END)
        entry3.focus()

        def autocapitalize(*arg):
            patientid.set(patientid.get().upper())

        patientid.trace("w", autocapitalize)

        numberChoosen1 = ttk.Combobox(canvas5, width=20, textvariable=exeType, state='readonly', font=font_size, )
        numberChoosen1.place(x=250, y=165)  # 5
        numberChoosen1.delete(0,END)
        excersie_results = numberChoosen1.bind("<FocusIn>", (lambda event: KeyChange(str(entry3.get()))))

        def report_calendar_focus(helpval):
            if helpval == 1:
                cal_wid1.focus_set()

            if helpval == 2:
                cal_wid2.focus_set()

        license_entry = Entry(canvas5, textvariable=reportStart, bd=3, width=11, font=font_size)
        license_entry.place(x=160, y=230)
        license_entry.bind('<FocusIn>', lambda event: report_calendar_focus(1))

        result2 = license_entry.get()

        cal_wid1 = HoverButton(canvas5, compound=LEFT, bg="white",
                               activebackground="blue", image=photo_image20, width=20, height=20,
                               borderwidth=1,
                               command=lambda: cal_widget(value=1,fromfun=1), cursor="hand2")
        cal_wid1.place(x=315, y=235)

        license_endentry = Entry(canvas5, textvariable=reportEnd, bd=3, width=11, font=font_size)
        license_endentry.place(x=500, y=230)

        license_endentry.bind('<FocusIn>', lambda event: report_calendar_focus(2))

        result1 = license_endentry.get()

        cal_wid2 = HoverButton(canvas5, compound=LEFT, bg="white",
                               activebackground="blue", image=photo_image20, width=20, height=20,
                               borderwidth=1, command=lambda: cal_widget(value=2,fromfun=1), cursor="hand2")
        cal_wid2.place(x=655, y=235)
        # Passing 1 to processGraph is Speed Graph
        button_report = HoverButton(canvas5, text="Speed Report", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                    command=lambda: processGraph(1), width=15, activebackground='blue', cursor="hand2")
        button_report.place(x=100, y=330)

        # Passing 2 to processGraph is Angle Graph
        button4_report = HoverButton(canvas5, text="Angle Report", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                     command=lambda: processGraph(2), width=15, activebackground='blue', cursor="hand2")

        button4_report.place(x=300, y=330)

        button5_report = HoverButton(canvas5, text="Table Report", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                     command=lambda: tableGraph(), width=15, activebackground='blue', cursor="hand2")
        button5_report.place(x=500, y=330)

        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white", borderwidth=0,
                                     command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)

        toprightmostpart()
    except:
        log_except()


def KeyChange(event,data=None):
    if event is not None:

        try:
            global button4_report, license_entry
            logging.info("Key change called.")
            conn = sqlite3.connect(json_const['DB_NAME'])
            c = conn.cursor()

            global exercises, device
            type = ""
            name = ""
            count = 0
            suboption_value = []
            item = ""
            s = ""

            c.execute("SELECT ExerciseID FROM ExerciseSession WHERE PatientID=" + "'" + event + "' and reps is not null GROUP BY ExerciseID")
            exercises_data = []
            for row in c.fetchall():
                exercises_data.append(row[0])
                count = count + 1
            logging.info(exercises_data)
            suboption_value = []

            for data in exercises_data:
                if device == "S":
                    c.execute(
                        "SELECT Category,ExerciseName FROM S_ExerciseMaster WHERE ID= '" + str(data) + "' LIMIT 1")
                else:
                    c.execute(
                        "SELECT Category,ExerciseName FROM R_ExerciseMaster WHERE ID= '" + str(data) + "' LIMIT 1")
                for row in c.fetchall():
                    type = row[0]
                    name = row[1]
                    suboption_value.append(type + '-' + name)

            suboption_value = list(dict.fromkeys(suboption_value))
            logging.info("Suboptions chosen value : " + str(suboption_value))

            numberChoosen1 = ttk.Combobox(canvas5, width=20, textvariable=exeType, state='readonly', font=font_size, )
            numberChoosen1.delete(0, END)
            numberChoosen1.set('')
            numberChoosen1['values'] = ['No Records Found'] if not suboption_value else suboption_value

            numberChoosen1.place(x=250, y=165)  # 5

            numberChoosen1.current(0)
            numberChoosen1.focus()

            cal_wid1 = HoverButton(canvas5, compound=LEFT, bg="white",
                                   activebackground="blue", image=photo_image20, width=20, height=20,
                                   borderwidth=1,
                                   command=lambda: cal_widget(value=1, fromfun=1), cursor="hand2")
            cal_wid1.place(x=315, y=235)

            cal_wid2 = HoverButton(canvas5, compound=LEFT, bg="white",
                                   activebackground="blue", image=photo_image20, width=20, height=20,
                                   borderwidth=1, command=lambda: cal_widget(value=2, fromfun=1), cursor="hand2")
            cal_wid2.place(x=655, y=235)
            # license_entry.focus()
            text = "Angle Report"

            def buttontext(choosen):
                global button4_report
                if choosen == "Walking Exercise-Walking":
                    text = "Steps Report"
                    button4_report.config(text="Steps Report", command=lambda: processGraph(2, reporttype=3))
                    button_report.config(command=lambda: processGraph(1, reporttype=3))
                    button5_report.config(command=lambda: tableGraph(1))
                elif numberChoosen1.get() == "Forearm Exercise-Horizontal Movement" or numberChoosen1.get() == "Arm Exercise-Horizontal Movement" \
                        or numberChoosen1.get() =="Forearm Exercise-Pronation & Supination" or numberChoosen1.get() =="Hip Exercise-Adduction & Abduction" \
                        or numberChoosen1.get() =="Ankle Exercise-Flexion & Extension" :
                    # text = "Steps Report"
                    logging.info("Report type : " + str(numberChoosen1.get()))

                    button4_report.config(text="Reps Report", command=lambda: processGraph(2, reporttype=4))
                    button_report.config(command=lambda: processGraph(1, reporttype=4))
                    button5_report.config(command=lambda: tableGraph(2))
                elif numberChoosen1.get() == "Arm Exercise-Pulley":
                    # text = "Steps Report"
                    logging.info("report type : " + str(numberChoosen1.get()))

                    button4_report.config(text="Reps Report", command=lambda: processGraph(2, reporttype=5))
                    button_report.config(command=lambda: processGraph(1, reporttype=5))
                    button5_report.config(command=lambda: tableGraph(3))
                else:
                    text = "Angle Report"
                    button4_report.config(text="Angle Report", command=lambda: processGraph(2))
                    button_report.config(command=lambda: processGraph(1))
                    button5_report.config(command=lambda: tableGraph())

            numberChoosen1.bind("<FocusOut>", lambda event: buttontext(numberChoosen1.get()))
            numberChoosen1.bind("<Enter>", lambda event: buttontext(numberChoosen1.get()))
            numberChoosen1.bind("<Leave>", lambda event: buttontext(numberChoosen1.get()))
            numberChoosen1.bind("<<ComboboxSelected>>", lambda event: buttontext(numberChoosen1.get()))

            # Passing 1 to processGraph is Speed Graph
            button_report = HoverButton(canvas5, text="Speed Report", bg="#007ED9", fg="white",
                                        font=('Helvetica', '15'),
                                        command=lambda: processGraph(1), width=15, activebackground='blue',
                                        cursor="hand2")
            button_report.place(x=100, y=330)

            # Passing 2 to processGraph is Angle Graph
            button4_report = HoverButton(canvas5, text=text, bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                         command=lambda: processGraph(2),
                                         width=15, activebackground='blue', cursor="hand2")

            button4_report.place(x=300, y=330)
            button5_report = HoverButton(canvas5, text="Table Report", bg="#007ED9", fg="white",
                                         font=('Helvetica', '15'),
                                         command=lambda: tableGraph(),
                                         width=15, activebackground='blue', cursor="hand2")
            button5_report.place(x=500, y=330)

            if numberChoosen1.get() == "Walking Exercise-Walking":
                # text = "Reps Report"
                logging.info("Report type : " + str(numberChoosen1.get()))
                button4_report.config(text="Steps Report", command=lambda: processGraph(2, reporttype=3))
                button_report.config(command=lambda: processGraph(1, reporttype=3))
                button5_report.config(command=lambda: tableGraph(1))
            elif numberChoosen1.get() == "Forearm Exercise-Horizontal Movement" or numberChoosen1.get() == "Arm Exercise-Horizontal Movement" \
                    or numberChoosen1.get() == "Forearm Exercise-Pronation & Supination" or numberChoosen1.get() =="Ankle Exercise-Flexion & Extension" :
                # text = "Steps Report"
                logging.info("Report type : " + str(numberChoosen1.get()))
                button4_report.config(text="Reps Report", command=lambda: processGraph(2, reporttype=4))
                button_report.config(command=lambda: processGraph(1, reporttype=4))
                button5_report.config(command=lambda: tableGraph(2))
            elif numberChoosen1.get() =="Arm Exercise-Pulley":
                # text = "Steps Report"
                logging.info("Report type : " + str(numberChoosen1.get()))
                button4_report.config(text="Reps Report", command=lambda: processGraph(2, reporttype=5))
                button_report.config(command=lambda: processGraph(1, reporttype=5))
                button5_report.config(command=lambda: tableGraph(3))
            else:
                text = "Angle Report"
                logging.info("Report type : " + str(numberChoosen1.get()))
                button4_report.config(text="Angle Report", command=lambda: processGraph(2))
                button_report.config(command=lambda: processGraph(1))
                button5_report.config(command=lambda: tableGraph())
        except:
            log_except()

def processGraph(p,reporttype=None):
    #report type: if walking exericse is selected report will change accordingly
    try:
        global game_for_report_CV, patient_for_report_CV, report_title, reportGameGraph, ax,device,result,result1,result2
        back.append(2)
        if  reportGameGraph is not None:
            reportGameGraph.destroy()
        logging.info("Report type : "+str(reporttype))
        def datetime_to_float(d):
            return d.timestamp()

        exlist = []
        combineex = ''
        if result2!="":
            start_date = result2
        else:
            start_date = "2018-07-10"

        a = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        start_conv=datetime_to_float(a)
        if result1!="":
            end_date = str(result1)+" "+"23:59:00"
        else:
            end_date = "2100-07-10 23:59:00"

        b = datetime.datetime.strptime(end_date, "%Y-%m-%d %X")
        end_conv = datetime_to_float(b)
        logging.info("Start date & Conv date : " + str(result2) + " "+str(start_conv))
        logging.info("End date & Conv date : "+ str(result1) + " " + str(end_conv))
        if StartReportCheck():
            db_patient_name = patientid.get()
            combineex = exeType.get()
            exlist = combineex.split('-')
            if len(exlist) == 1:
                if p == 1:
                    logging.info('No Records found for Speed graph. ')
                elif p == 2:
                    logging.info('No Records found for Angle graph. ')

                d = dialoguebox(root, text="No data found for the patient.", buttons=["OK"],
                                default=0, cancel=2, title=info, icon='Pictures/info.png')
                d.go()
                entry3.focus()
                return False
            else:
                extype = exlist[0]
                exname = exlist[1]

                conn = sqlite3.connect(json_const['DB_NAME'])
                c = conn.cursor()
                if device=="S":
                    c.execute("SELECT ID FROM S_ExerciseMaster WHERE Category= '" + str(extype) + "' AND ExerciseName='" + str(
                    exname) + "' LIMIT 1")
                else:
                    c.execute(
                        "SELECT ID FROM R_ExerciseMaster WHERE Category= '" + str(extype) + "' AND ExerciseName='" + str(
                            exname) + "' LIMIT 1")
                for row in c.fetchall():
                    id = row[0]

                c.execute(
                    "SELECT * FROM ExerciseSession WHERE PatientID='" + db_patient_name + "' and ExerciseID='" + str(id) + \
                    "'and StartTime>='"+str(start_conv)+"'and StartTime<='"+str(end_conv)+"'"+'and reps is not NULL')

                if len(c.fetchall()) != 0:

                    logging.info("Processing the graph " + str(p) + " for : " + str(db_patient_name) + " " + str(exname))
                    patient_reps = []
                    patient_perfect_reps = []

                    xDates = []

                    xDates2 = ['31-01-2019', '01-02-2019', '02-02-2019', '03-02-2019', '04-02-2019']

                    xList = []
                    yList = []

                    x1List = []
                    y1List = []
                    y2List = []
                    speed = []
                    slist = []
                    AngleReached = []
                    totalAngle = []

                    conn = sqlite3.connect(json_const['DB_NAME'])
                    c = conn.cursor()

                    c.execute("SELECT perfectHits, reps, StartTime, duration, minAngle, maxAngle FROM ExerciseSession \
                    WHERE PatientID='" + db_patient_name + "' and ExerciseID='" + str(id) + "'and StartTime>='"+str(start_conv)+ \
                              "'and StartTime<='"+str(end_conv)+"'"+'and reps is not NULL and duration > 0 ')
                    i = 1
                    count = 0

                    for row in c.fetchall():
                        yList.append(row[0])
                        slist.append('S' + str(i))

                        xList.append(i)
                        y1List.append(row[1])
                        initialdate = float(row[2]) + 5 * 60 * 60
                        y2List.append(row[3])

                        if reporttype==3 or reporttype==4:
                            logging.info("Walking Exercise or Horizontal Movement or Pronation Supination process graph")
                            speed.append(float(row[5]) / float(row[3]))
                            totalAngle.append(row[5])
                        elif reporttype==5:
                            logging.info("Arm Exercise-Pulley process graph")
                            speed.append(float(row[5]) / float(row[3]))
                            totalAngle.append(row[0])
                        else:
                            speed.append(round(float(row[0]) / float(row[3])))

                            totalAngle.append(((-1) * row[4] + row[5]))

                        finaltime = initialdate + 30 * 60
                        xDates.append(datetime.datetime.utcfromtimestamp(finaltime).strftime('%d-%m-%Y %H:%M:%S'))
                        x1List.append(i)

                        i = i + 1
                        count=count+1
                        logging.info("Selected Row : " + str(row))

                    logging.info("Dates are : " + str(xDates))

                    reportGameGraph = GameGraph()
                    reportGameGraph.game_for_report_CV.set(str(db_patient_name))
                    reportGameGraph.patient_for_report_CV.set(str(exname))

                    reportGameGraph.graph = tk.Frame(reportGameGraph)
                    reportGameGraph.graph.pack()

                    LOGPIXELSX = 88
                    LOGPIXELSY = 90

                    if platform.system() == "Windows":

                        dc = windll.user32.GetDC(0)
                        y = int(windll.gdi32.GetDeviceCaps(dc, LOGPIXELSY))
                        x = int(windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX))
                        windll.user32.ReleaseDC(0, dc)
                    else:
                        x = 100
                        y = 100

                    incheswidth = root.winfo_screenwidth() / y
                    inchesheight = root.winfo_screenheight() / x

                    lasty = incheswidth % 12
                    lastx = inchesheight % 4
                    from matplotlib.figure import Figure
                    import matplotlib.pyplot as plt

                    fig = Figure()

                    height = fig.dpi
                    width = fig.dpi

                    ax = fig.add_subplot(111)

                    fig.set_size_inches(11, 4.2, forward=True)

                    ax.clear()
                    ename = extype.split(' ', 1)[0]
                    if p==1:
                        if count == 1:
                            line = ax.plot(slist, speed, 'ro')
                        else:
                            line = ax.plot(slist, speed)
                        if reporttype==3:
                            ax.legend(['SPEED'], loc='upper left')
                            ax.set_ylabel('Steps / Minute', fontsize=12)
                        else:
                            ax.legend(['SPEED'], loc='upper left')
                            ax.set_ylabel('Reps / Minute', fontsize=12)

                        ax.set_xlabel('Sessions', fontsize=12)
                        locs, labels = plt.xticks()
                        logging.info("In Sessions list size " + str(len(slist)) )
                        if (len(slist) > 20):
                            num = int(len(slist) / 10)
                            ax.set_xticks(ax.get_xticks()[::num])
                        else:
                            ax.set_xticks(ax.get_xticks())
                        ax.xaxis.set_label_coords(1.05, 0)
                        plt.setp(ax.get_xticklabels(), rotation=60, horizontalalignment='right')

                        fig.suptitle("    Speed Report " + "\n\n        Patient ID: " + str(
                            db_patient_name) + "                                                                    " + "Exercise : " + str(
                            exname) + " (" + str(ename) + ")", y=1, fontsize=12)
                    elif p==2:
                        if reporttype is None:
                            if count == 1:
                                line = ax.plot(slist, totalAngle, 'ro')
                            else:
                                line = ax.plot(slist, totalAngle)
                                logging.info(slist)
                                logging.info(totalAngle)
                            ax.legend(['ANGLE'], loc='upper left')
                            ax.set_xlabel('Sessions', fontsize=12)
                            ax.set_ylabel('Degrees', fontsize=12)

                            locs, labels = plt.xticks()
                            logging.info("In Angle list size " + str(len(slist)))
                            if (len(slist) > 20):
                                num = int(len(slist) / 10)
                                ax.set_xticks(ax.get_xticks()[::num])
                            else:
                                ax.set_xticks(ax.get_xticks())
                            ax.xaxis.set_label_coords(1.05, 0)
                            plt.setp(ax.get_xticklabels(), rotation=60, horizontalalignment='right')
                            fig.suptitle("Angle Report \n\n  Patient ID: " + str(
                                db_patient_name) + "                                                                    " + "Exercise : " + str(
                                exname) + " (" + str(ename) + ")", y=1, fontsize=12)
                        elif reporttype==3:
                            if count == 1:
                                line = ax.plot(slist, totalAngle, 'ro')
                            else:
                                line = ax.plot(slist, totalAngle)
                                logging.info(slist)
                                logging.info(totalAngle)
                            ax.legend(['Steps'], loc='upper left')
                            ax.set_xlabel('Sessions', fontsize=12)
                            ax.set_ylabel('Steps', fontsize=12)
                            locs, labels = plt.xticks()
                            logging.info("In Steps list size " + str(len(slist)))
                            if (len(slist) > 20):
                                num = int(len(slist) / 10)
                                ax.set_xticks(ax.get_xticks()[::num])
                            else:
                                ax.set_xticks(ax.get_xticks())
                            ax.xaxis.set_label_coords(1.05, 0)
                            plt.setp(ax.get_xticklabels(), rotation=60, horizontalalignment='right')
                            fig.suptitle("Steps Report \n\n  Patient ID: " + str(
                                db_patient_name) + "                                                                    " + "Exercise : " + str(
                                exname) + " (" + str(ename) + ")", y=1, fontsize=12)
                        elif reporttype==4 or reporttype==5:
                            if count == 1:
                                line = ax.plot(slist, totalAngle, 'ro')
                            else:
                                line = ax.plot(slist, totalAngle)
                                logging.info(slist)
                                logging.info(totalAngle)
                            ax.legend(['Reps'], loc='upper left')
                            ax.set_xlabel('Sessions', fontsize=12)
                            ax.set_ylabel('Reps', fontsize=12)
                            locs, labels = plt.xticks()
                            logging.info("In Reps list size " + str(len(slist)))
                            if (len(slist) > 20):
                                num = int(len(slist) / 10)
                                ax.set_xticks(ax.get_xticks()[::num])
                            else:
                                ax.set_xticks(ax.get_xticks())
                            ax.xaxis.set_label_coords(1.05, 0)
                            plt.setp(ax.get_xticklabels(), rotation=60, horizontalalignment='right')
                            fig.suptitle("Reps Report \n\n  Patient ID: " + str(
                                db_patient_name) + "                                                                    " + "Exercise : " + str(
                                exname) + " (" + str(ename) + ")", y=1, fontsize=12)
                    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

                    canvas = FigureCanvasTkAgg(fig, master=reportGameGraph.graph)

                    canvas.draw()
                    if p==1:
                        filename = db_patient_name + '-' + str(exname) + '-SpeedReport'
                    elif p==2:
                        if reporttype is None:
                            filename = db_patient_name + '-' + str(exname) + '-AngleReport'
                        elif reporttype==3:
                            filename = db_patient_name + '-' + str(exname) + '-StepsReport'
                        else:
                            filename = db_patient_name + '-' + str(exname) + '-RepsReport'

                    download_button = HoverButton(reportGameGraph, compound=LEFT, bg="white",
                                                  activebackground="#5DADE2", image=photo_image11, width=40, height=40,
                                                  borderwidth=2,
                                                  command=lambda: ask_download(), cursor="hand2")
                    download_button.place(x=1000, y=50)

                    def ask_download():

                        fig.savefig('Reports/' + filename + '.png')
                        from fpdf import FPDF
                        class PDF(FPDF):
                            def header(self):
                                # Logo
                                self.image("Pictures/soujhe_logo.png", 35, 8, 33)
                                self.image("Pictures/company_logo.png", 235, 8, 33)
                                # Arial bold 15
                                self.set_font('Arial', 'B', 15)
                                # Move to the right
                                self.cell(80)
                                # Title
                                # self.cell(30, 10, 'P1-Flexion & Extension-SpeedReport', 1, 0, 'C')
                                # Line break
                                self.ln(20)

                            # Page footer
                            def footer(self):
                                # Position at 1.5 cm from bottom
                                self.set_y(-15)
                                # Arial italic 8
                                self.set_font('Arial', 'I', 8)
                                # Page number

                                self.cell(0, 0, "2019 © Soujhe Innovative Healthcare Devices Pvt. Ltd.", 0, 0, 'C')
                                self.cell(0, 20, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'R')

                        # Instantiation of inherited class
                        pdf = PDF(orientation='L', unit='mm', format='A4')
                        pdf.alias_nb_pages()
                        pdf.add_page()
                        pdf.set_font('Times', '', 12)
                        pdf.cell(0, 22, " ", 0, 2, 'C')
                        pdf.cell(-30)
                        pdf.image("Reports/"+filename+'.png', x=0, y=None, w=300, h=0, type='', link='')
                        if (platform.system() == "Linux"):
                            a = asksaveasfilename(initialdir="Reports/", initialfile=filename, filetypes=(("PDF file", "*.pdf"), ("All Files", "*.*")),
                                                  defaultextension='.pdf', title="Save Report")
                        else:
                            a = asksaveasfilename(initialdir="Reports\\", initialfile=filename, filetypes=(("PDF file", "*.pdf"), ("All Files", "*.*")),
                                              defaultextension='.pdf', title="Save Report")
                        if a:
                            pdf.output(a, 'F')
                            remove_png()

                    reportGameGraph.pack(expand=True)
                    canvas.get_tk_widget().pack(expand=True)
                else:
                    d = dialoguebox(root, text="No data found for the patient.", buttons=["OK"],
                                    default=0,
                                    cancel=2, title=info, icon='Pictures/info.png')
                    d.go()
                    entry3.focus()
                    return False
        else:
            return False

        def mainMenuSelectionPage(root):

            root.report_title.destroy()
            root.graph.destroy()
            root.controller.show_frame(GameGraph)
            reportGameGraph.destroy()

        GameGraph()
    except:
        log_except()

def tableGraph(exerciseval=None):
    #exercise: if exercise is not none then the exercise is walking and disply steps and steps/min in table graph else angle and reps/min
    global game_for_report_CV, patient_for_report_CV, report_title, reportGameGraph, ax, canvas5, canvas1,device, result1,result2
    back.append(2)
    logging.info("Arugument value : "+str(exercise))
    exname = ''
    extype = ''
    id = ''
    exlist = []
    combineex = ''
    tlen=0

    def datetime_to_float(d):
        return d.timestamp()

    if result2 != "":
        start_date = result2
    else:
        start_date = "2018-07-10"

    a = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    start_conv = datetime_to_float(a)
    if result1 != "":
        end_date = str(result1) + " " + "23:59:00"
        # b = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    else:
        logging.info("in endtime null session")
        end_date = result1 = "2100-07-10 23:59:00"

    b = datetime.datetime.strptime(end_date, "%Y-%m-%d %X")
    end_conv = datetime_to_float(b)
    logging.info("Tablegraph Start date & conv date : " + str(result2) + ";" + str(start_conv))
    logging.info("Tablegraph End date & conv date : " + str(result1) + ";" + str(end_conv))

    if StartReportCheck():
        db_patient_name = patientid.get()
        combineex = exeType.get()
        exlist = combineex.split('-')
        if len(exlist ) == 1:
            logging.info('No Records found for table graph. ')
            d = dialoguebox(root, text="No data found for the patient.", buttons=["OK"],
                            default=0, cancel=2, title=info, icon='Pictures/info.png')
            d.go()
            entry3.focus()
        else:
            extype = exlist[0]
            exname = exlist[1]

            conn = sqlite3.connect(json_const['DB_NAME'])
            c = conn.cursor()
            if device == "S":
                c.execute(
                    "SELECT ID FROM S_ExerciseMaster WHERE Category= '" + str(extype) + "' AND ExerciseName='" + str(
                        exname) + "' LIMIT 1")
            else:
                c.execute(
                    "SELECT ID FROM R_ExerciseMaster WHERE Category= '" + str(extype) + "' AND ExerciseName='" + str(
                        exname) + "' LIMIT 1")
            for row in c.fetchall():
                id = row[0]
            c.execute(
                "SELECT * FROM ExerciseSession WHERE PatientID='" + db_patient_name + "' and ExerciseID='" + str(
                    id) + "'and StartTime>='" + str(start_conv) + "'and StartTime<='" + str(
                    end_conv) + "'" + 'and reps is not NULL')

            if len(c.fetchall()) != 0:
                logging.info("Processing the table graph : " + str(db_patient_name) + " " + str(exname))

                exerciseName = []
                ldata = []
                plist = []
                totalAngle = []

                date = []
                speed = []
                ex = []
                value = []
                finaldata = []
                t = time.strftime('%X')
                fname=exname.replace(" ","_")
                f1=fname.replace("&","and")
                if (platform.system() == "Linux"):
                    filename = 'Reports/' +db_patient_name + '-' + str(f1) + '-TableReport' + '.csv'
                    cmd1 = "sudo chmod 777 " + filename
                    subprocess.Popen(cmd1, shell=True)
                    cmd2 = "libreoffice --view " + filename
                    subprocess.Popen(cmd2, shell=True)
                else:
                    filename = 'Reports\\' + db_patient_name + '-' + str(f1) + '-TableReport' + '.csv'
                import csv
                def writeFirstHeader(iList):
                    try:
                        with open(filename, "w", newline='\n') as f:
                            writer = csv.writer(f)
                            writer.writerow(iList)
                    except PermissionError:
                        d = dialoguebox(root, text="Report is already open.\nPlease close it to re-generate.", buttons=["OK"],
                                        default=0, cancel=2, title=info, icon='Pictures/info.png')
                        d.go()
                        entry3.focus()
                        log_except()
                        return False

                def writeSecondHeader(iList):
                    try:
                        with open(filename, "a", newline='\n') as f:
                            writer = csv.writer(f)
                            writer.writerow(iList)
                    except:
                        log_except()

                def writeCSV(iList):
                    try:
                        with open(filename, "a", newline='\n') as f:
                            writer = csv.writer(f)
                            writer.writerow(iList)
                    except:
                        log_except()
                if exerciseval==1 :

                    writeFirstHeader(
                        ['', '', 'Session 1', '', '', 'Session 2', '', '', 'Session 3', '', '', 'Session 4', '', '',
                         'Session 5', '', '', 'Session 6', '', '', 'Session 7'])

                    writeSecondHeader(
                        ['Date', 'Steps', 'Speed(steps/min)', 'Others', 'Steps', 'Speed(steps/min)',
                         'Others','Steps', 'Speed(steps/min)', 'Others', 'Steps', 'Speed(steps/min)',
                         'Others', 'Steps', 'Speed(steps/min)', 'Others', 'Steps', 'Speed(steps/min)',
                         'Others', 'Steps', 'Speed(steps/min)', 'Others'])
                elif exerciseval==2 or exerciseval==3:
                    writeFirstHeader(
                        ['', '', 'Session 1', '', '', 'Session 2', '', '', 'Session 3', '', '', 'Session 4', '', '',
                         'Session 5', '', '', 'Session 6', '', '', 'Session 7'])

                    writeSecondHeader(
                        ['Date', 'Reps', 'Reps_Min(Reps/min)', 'Others', 'Reps', 'Reps_Min(Reps/min)',
                         'Others', 'Reps', 'Reps_Min(Reps/min)', 'Others', 'Reps', 'Reps_Min(Reps/min)',
                         'Others', 'Reps', 'Reps_Min(Reps/min)', 'Others', 'Reps', 'Reps_Min(Reps/min)',
                         'Others', 'Reps', 'Reps_Min(Reps/min)', 'Others'])

                else:
                    writeFirstHeader(['', '', 'Session 1', '', '', 'Session 2', '', '', 'Session 3', '', '', 'Session 4', '', '','Session 5', '', '', 'Session 6', '', '', 'Session 7'])

                    writeSecondHeader(['Date', 'Angle(Degrees)', 'Speed(Reps/min)', 'Others', 'Angle(Degrees)', 'Speed(Reps/min)', 'Others', 'Angle(Degrees)','Speed(Reps/min)', 'Others', 'Angle(Degrees)', 'Speed(Reps/min)', 'Others', 'Angle(Degrees)', 'Speed(Reps/min)', 'Others', 'Angle(Degrees)','Speed(Reps/min)', 'Others', 'Angle(degree)', 'Speed(Reps/min)', 'Others'])

                conn = sqlite3.connect(json_const['DB_NAME'])
                c = conn.cursor()

                c.execute(
                    "SELECT perfectHits,minAngle, maxAngle,StartTime,Weight_value,ExerciseCategory_ID,duration,ExerciseID FROM ExerciseSession WHERE PatientID='" + db_patient_name + "' and ExerciseID='" + str(id) + "'and StartTime>='"+str(start_conv)+"'and StartTime<='"+str(end_conv)+"'"+'and reps is not NULL and duration > 0')

                count = 0
                for row in c.fetchall():

                    initialdate = float(row[3]) + 5 * 60 * 60
                    finaltime = initialdate + 30 * 60

                    xDates = (datetime.datetime.utcfromtimestamp(finaltime).strftime('%d-%m-%Y %H:%M:%S'))
                    Dlist = xDates.split(' ')

                    date.append(Dlist[0])
                    if exerciseval==1 or exerciseval==2:
                        logging.info("Exercise val==2 or 1")
                        speed.append(round(float(row[2]) / float(row[6])))
                        totalAngle.append(row[2])
                    elif exerciseval==3:
                        logging.info("exerciseval==3")
                        speed.append(round(float(row[0]) / float(row[6])))
                        totalAngle.append(row[0])
                    else:
                        speed.append(round(float(row[0]) / float(row[6])))
                        totalAngle.append(round((-1) * row[1] + row[2]))
                    logging.info("row 0 data table graph :"+str(row[0]))
                    logging.info("row 6 data table graph :"+str(row[6]))
                    logging.info("row 2 data table graph :"+str(row[2]))
                    logging.info("speed data table graph :"+str(speed))
                    logging.info("total angle data table graph :"+str(totalAngle))
                    ex.append(row[5])
                    exerciseName.append(row[6])
                    count = count + 1

                    conn = sqlite3.connect(json_const['DB_NAME'])
                    c = conn.cursor()
                    c.execute(
                        "SELECT CategoryName,CategoryValue FROM ExerciseCategory WHERE ID='" + str(row[5]) + "'")
                    if row[5] =='':
                        value.append('')
                    elif row[5] >= 1 and row[5] <= 6:
                        for r in c.fetchall():
                            value.append(str(r[0]) + '- ' + str(r[1]))
                    else:
                        for r in c.fetchall():
                            value.append(str(r[0]) + '- ' + str(row[4]))
                date1 = list(dict.fromkeys(date))
                dlen = len(date1)
                i = 0
                sum = 0
                flag = 0
                for j in range(dlen):
                    ldata.append(date1[j])
                    dc = date.count(date1[j])
                    sum = sum + dc

                    for i in range(flag, sum):
                        # ldata.append(date[i])
                        ldata.append(totalAngle[i])
                        ldata.append(speed[i])
                        ldata.append(value[i])

                    flag = sum
                    ldata.append("\n")
                    writeCSV(ldata)
                    ldata = []

                Popen(filename, shell=True)
                result1=""
                result2=""
            else:
                d = dialoguebox(root, text="No data found for the patient.", buttons=["OK"],
                                default=0,  cancel=2, title=info, icon='Pictures/info.png')
                d.go()
                entry3.focus()
                return False
    else:
        return False

def remove_png():
    removed = 0

    dir_to_search_old = os.getcwd()

    if dir_to_search_old != "/Reports/":  # compare current to desired directory
        # Now change the directoryF
        os.chdir('Reports/')
        # Check current working directory.
        dir_to_search = os.getcwd()
    import glob
    tifCounter = glob.glob1(dir_to_search, "*.png")
    logging.info("Number of png files in directory : " + str(tifCounter))
    for item in tifCounter:
        if item.endswith("*.png"):
            logging.info("PNG file : ",str(item))
        os.remove(item)
        logging.info("Deleted PNG file : " + str(item))
        removed += 1
    logging.info("Number of png files removed : " + str(removed))
    os.chdir(dir_to_search_old)

def StartReportCheck():
    try:

        db_patient_name = patientid.get()
        db_exercise_name = exeValue.get()

        if db_patient_name is '' and db_exercise_name is '':
            d = dialoguebox(root, text="Please enter a valid patient ID ", buttons=["OK"],
                            default=0, cancel=2, title=warn, icon='Pictures/warn.png')
            d.go()
            return False
        elif db_patient_name is '':
            messagebox.showinfo("Enter the patient ID", "Please enter a valid patient ID")
            entry3.focus()
            return False
        elif db_exercise_name == 'Select':
            messagebox.showinfo("Select the exercise", "Select the Exercise Name from Dropdown list")
            return False
        else:
            return True
    except:
        log_except()

class GameGraph(tk.Frame):
    try:

        def __init__(self):
            global canvas5, canvas2, photo_image5, canvas4, canvas1, game_for_report_CV, back, patient_for_report_CV
            back.append(5);
            if canvas1 is not None:
                canvas1.config(height=0, width=0)
                canvas1.delete("all")
            if canvas5 is not None:
                canvas5.config(height=0, width=0)
                canvas5.delete("all")

            canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                             highlightthickness=5)
            canvas1.place(x=0, y=0)
            canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold",
                                text="Report Result")

            tk.Frame.__init__(self, bg='white')

            # MainWindow = canvas5.create_window(10, 10, window=tk.Frame, anchor='nw')
            self.game_for_report_CV = StringVar()
            self.patient_for_report_CV = IntVar()

            self.game_for_report = self.game_for_report_CV
            self.patient_for_report = self.patient_for_report_CV

            self.game_for_report_CV.set("ae1")
            self.patient_for_report_CV.set(1)
    except:
        log_except()

def gamepage():
    try:

        global canvas5, photo_image4, photo_image5, canvas4, canvas1, login, back, photo_image6, reportGameGraph, canvas2, photo_image3, photo_image2
        back.append(2)
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

        if canvas is not None:
            canvas.destroy()
        login = 1
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Exercises")

        canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40, height=root.winfo_screenheight() - 165,
                         highlightbackground="blue", highlightthickness=20)
        canvas2.place(x=0, y=30)

        # Images
        photo_image2 = ImageTk.PhotoImage(image2)
        canvas2.create_image(150, 100, image=photo_image2)
        photo_image3 = ImageTk.PhotoImage(image3)
        canvas2.create_image(300, 100, image=photo_image3)
        toprightmostpart()
        canvas5 = Canvas(root, bg="white", width=1000, height=350, bd=0, relief='ridge',
                         highlightthickness=0)
        canvas5.place(x=200, y=200)
        button3 = HoverButton(canvas5, compound=TOP, width=270, height=270, bg="white",activebackground='white', image=photo_image15,
                              borderwidth=0, command=lambda:upperLimb(1), cursor="hand2")
        button3.place(x=240, y=100)
        button4 = HoverButton(canvas5, compound=TOP, width=270, height=270, bg="white",activebackground='white', image=photo_image16,
                              borderwidth=0, command=lambda:lowerLimb(2), cursor="hand2")
        button4.place(x=520, y=100)
        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white", borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)

    except:
        log_except()
def lowerLimb(val=None):
    #val=if val is 2 then control is from update patient else new patient
    try:
        global canvas5, patientid, excercise, entry3, canvas1, back, device
        back.append(10)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")

        toprightmostpart()
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold",
                            text="Game Exercises")
        canvas5 = Canvas(root, bg="white", width=900, height=350, bd=0, relief='ridge', highlightthickness=0)
        canvas5.place(x=300, y=270)
        button1 = HoverButton(canvas5, compound=TOP, pady=30, bg="sky blue", width=15, height=5, wraplength=100,
                              text="Walking Exercise", font=('Helvetica', '14'), command=lambda :walkingExercise(val),
                              activebackground='orange', cursor="hand2")
        button1.place(x=620, y=10)
        button2 = HoverButton(canvas5, activebackground='orange', cursor="hand2", compound=TOP, pady=30, bg="sky blue",
                              width=15, height=5, wraplength=100, text='Knee Exercise', font=('Helvetica', '14'),
                              command=lambda : kneeExercise(val))
        button2.place(x=20, y=10)

        button3 = HoverButton(canvas5, activebackground='orange', cursor="hand2", compound=TOP, pady=30, bg="sky blue",
                              width=15, height=5, wraplength=100, text='Ankle Exercise', font=('Helvetica', '14'),
                              command=lambda: ankleExercise(val))
        button3.place(x=220, y=10)
        button4 = HoverButton(canvas5, activebackground='orange', cursor="hand2", compound=TOP, pady=30, bg="sky blue",
                              width=15, height=5, wraplength=100, text='Hip Exercise', font=('Helvetica', '14'),
                              command=lambda: hipExercise(val))
        button4.place(x=420, y=10)

        button3 = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white", borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
        button3.place(x=50, y=580)
    except:
        log_except()

def upperLimb(val=None):
    try:
        # if val is 2 then it is UpperLimb else LowerLimb
        global canvas5, patientid, excercise, entry3, canvas1, back,device
        back.append(10)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")

        toprightmostpart()
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold",
                            text="Game Exercises")
        canvas5 = Canvas(root, bg="white", width=600, height=350, bd=0, relief='ridge', highlightthickness=0)
        canvas5.place(x=400, y=270)
        button1 = HoverButton(canvas5, compound=TOP, pady=30, bg="sky blue", width=15, height=5, wraplength=100,
                              text="Arm Exercise", font=('Helvetica', '14'), command=lambda:armexercise(val),
                              activebackground='orange', cursor="hand2")
        button1.place(x=20, y=10)
        button2 = HoverButton(canvas5, activebackground='orange', cursor="hand2", compound=TOP, pady=30, bg="sky blue",
                              width=15, height=5, wraplength=100, text="Forearm Exercise", font=('Helvetica', '14'),
                              command=lambda: forearmexercise(val))
        button2.place(x=220, y=10)

        if device == "S":
            button3 = HoverButton(canvas5, activebackground='orange', cursor="hand2", compound=TOP, pady=30, bg="sky blue",
                              width=15, height=5, wraplength=100, text="Wrist Exercise", font=('Helvetica', '14'),
                              command=lambda:wristexercise(val))
            button3.place(x=420, y=10)

        button3 = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white", borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
        button3.place(x=50, y=580)
    except:
        log_except()

def checkLogIn() :
    try:

        global username, password, login, numberChoosen1,act1,pin1

        with open('Const/users.json') as i:
            json_const = json.load(i)
            data3 = []
            for value in json_const.values():
                data3.append(str(value))
            res = [data3[i] for i in range(len(data3)) if i % 2 == 0]
            val = [data3[i] for i in range(len(data3)) if i % 2 != 0]

            uact = json_const['User1']
            pwd = json_const['Pass1']
            upw = pwd.to_bytes(((pwd.bit_length() + 7) // 8), byteorder="big")
            upin = upw.decode("utf-8")

            data=[]
            for value in json_const.values():
                data.append(str(value))
            admin="admin"
            data2=[]
            if any(ext in admin for ext in data):
                for value in json_const.items():
                    data2.append(value)
                uid=data.index(admin)
                pid=int(data.index(admin))+1
                aact = data[uid]
                apw = int(data[pid])
                apw = apw.to_bytes(((apw.bit_length() + 7) // 8), byteorder="big")
                apin = apw.decode("utf-8")
                act1 = aact
                pin1 = apin

        actNum = entry1.get()
        pinNum = entry2.get()

        if actNum in res:
            p=int(data.index(actNum))
            q=int(p+1)
            r=int(data[q])
            pin_d = r.to_bytes(((r.bit_length() + 7) // 8), byteorder="big")
            apin = pin_d.decode("utf-8")
            if pinNum == apin:
                logging.info("Valid Login Credentials - " + str(time.strftime('%d %b %Y %X')) )
                with open('Const/license.json') as i:
                    json_const = json.load(i)
                    log_delete = json_const["101401729762753806113544700036426847301"]  # 237007384299206171504696
                    mBytes2 = log_delete.to_bytes(((log_delete.bit_length() + 7) // 8), byteorder="big")
                    json_endDate = mBytes2.decode("utf-8")
                    logging.info(" License End Date : " + str(json_endDate))
                    log_delete = json_const["6645463761731833437447950861006883695971924"]  # 237007384299206171504696
                    mBytes2 = log_delete.to_bytes(((log_delete.bit_length() + 7) // 8), byteorder="big")
                    json_CurCount1 = mBytes2.decode("utf-8")
                    json_CurCount = int(json_CurCount1)
                    logging.info(" Current count of sessions : " + str(json_CurCount))

                now = datetime.datetime.now()
                dt_string = now.strftime("%Y-%m-%d")

                if actNum==admin:
                    homemiddlepart(actNum)
                else:
                    logging.info("Current Date : " + str(dt_string) + " Exp Date is : " + str(json_endDate))
                    if dt_string > json_endDate:
                        d = dialoguebox(root,
                                        text="               License has expired. \n Please contact the system administrator",
                                        buttons=["OK"], default=0,
                                        cancel=2, title=error, icon='Pictures/error.png')
                        d.go()
                        logging.info("License has expired. Please contact the system administrator")
                        force_kill()

                    elif json_CurCount == 0:
                        d = dialoguebox(root, text=" All sessions have been exhausted.", buttons=["OK"], default=0,
                                        cancel=2,  title=error, icon='Pictures/error.png')
                        d.go()
                        logging.info("All sessions have been exhausted.")
                        force_kill()
                    else:
                        homemiddlepart(actNum)
            else:
                d = dialoguebox(root, text="Password is incorrect.", buttons=["OK"], default=0, cancel=2,
                                title=warn, icon='Pictures/warn.png')
                d.go()
        elif actNum == "":

            d = dialoguebox(root, text="Please enter a valid User ID.", buttons=["OK"], default=0, cancel=2,
                            title=warn,   icon='Pictures/warn.png')
            d.go()

        elif pinNum == "":
            d = dialoguebox(root, text="Please enter a valid password.", buttons=["OK"], default=0, cancel=2, title=warn,
                            icon='Pictures/warn.png')
            d.go()

        else:
            d = dialoguebox(root, text="User ID or Password is incorrect.", buttons=["OK"], default=0, cancel=2,
                            title=warn, icon='Pictures/warn.png')
            d.go()
    except:
        log_except()

def toprightmostpart() :
    try:

        global canvas4, username, photo_image6, photo_image7, photo_image8, login
        if login == 0:
            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
        elif login == 1:
            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
            canvas4 = Canvas(root, bg="white", width=230, height=100,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
            canvas4.create_text(140, 25, fill="blue", font="Times 14 bold ", text=str(username.get()).title())
            image6 = Image.open("Pictures/signout.png")
            image6 = image6.resize((30, 30), Image.ANTIALIAS)
            photo_image6 = ImageTk.PhotoImage(image6)
            button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
                                  command=initialmiddlepart, activebackground='blue', cursor="hand2")

            button1.place(x=120, y=50)

            image7 = Image.open("Pictures/homeicon.jpg")
            image7 = image7.resize((30, 30), Image.ANTIALIAS)
            photo_image7 = ImageTk.PhotoImage(image7)
            button2 = HoverButton(canvas4, compound=TOP, fg="white", bg="black", image=photo_image7, borderwidth=0,
                                  command=lambda: homemiddlepart(username.get()), activebackground='blue', cursor="hand2")
            button2.place(x=60, y=50)
    except:
        log_except()

def homemiddlepart(user) :
    try:

        global canvas5, photo_image4, photo_image5, canvas4, canvas1, login, back, photo_image6, reportGameGraph, canvas2, photo_image3, photo_image2
        back.append(1)
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
        if numberChoosen1 is not None:
            numberChoosen1.destroy()

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
        photo_image2 = ImageTk.PhotoImage(image2)
        canvas2.create_image(150, 100, image=photo_image2)
        photo_image3 = ImageTk.PhotoImage(image3)
        canvas2.create_image(300, 100, image=photo_image3)

        canvas4 = Canvas(root, bg="white", width=230, height=200,
                         highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
        canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
        canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
        canvas4.create_text(140, 25, fill="blue", font="Times 14 bold ", text=str(username.get()).title())
        image6 = Image.open("Pictures/signout.png")
        image6 = image6.resize((30, 30), Image.ANTIALIAS)
        photo_image6 = ImageTk.PhotoImage(image6)
        button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
                              command=initialmiddlepart, activebackground='blue', cursor="hand2")

        button1.place(x=120, y=50)

        canvas5 = Canvas(root, bg="white", width=1100, height=350, bd=0, relief='ridge',
                         highlightthickness=0)
        canvas5.place(x=100, y=200)
        txt1 = canvas5.create_text(720, 90, fill="black", font="Times 20 italic bold", text="Run Report")
        txt2 = canvas5.create_text(450, 90, fill="black", font="Times 20 italic bold", text="Run Game")
        image4 = Image.open("Pictures/reports-png-1.png")
        image4 = image4.resize((170, 170), Image.ANTIALIAS)
        photo_image4 = ImageTk.PhotoImage(image4)
        button1 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image4,
                              borderwidth=0, command=lambda:runreport(), cursor="hand2")
        button1.place(x=640, y=140)#x=790, y=140

        image5 = Image.open("Pictures/Physical-Therapy_Icon.png")
        image5 = image5.resize((170, 170), Image.ANTIALIAS)
        photo_image5 = ImageTk.PhotoImage(image5)
        button2 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image5,
                              borderwidth=0, command=gamepage, cursor="hand2")
        button2.place(x=370, y=140)
        txt3 = canvas5.create_text(180, 90, fill="black", font="Times 20 italic bold", text=" Patient Registration")#320, 90,

        button4 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image17,
                              borderwidth=0, activebackground='white', command=registration, cursor="hand2")
        button4.place(x=100, y=140)
        # ========================

        canvas5.create_text(990, 90, fill="black", font="Times 20 italic bold", text="Utilities", )
        button3 = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=photo_image13,
                              borderwidth=0,activebackground='white', command=lambda: utilities(user), cursor="hand2")
        button3.place(x=910, y=140)
    except:
        log_except()

def registration():
    try:

        global canvas5,photo_image4,canvas2, photo_image5, canvas4, patientid, excercise, entry3, canvas1, back,disordercombo,p_status,patient_entry,auto_text,patient_entry
        back.append(2)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")

        if reportGameGraph is not None:
            reportGameGraph.destroy()

        if canvas is not None:
            canvas.destroy()
        login = 1
        canvas5.config(height=0, width=0)
        canvas5.delete("all")

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Exercises")

        toprightmostpart()
        canvas5 = Canvas(root, bg="white", width=1000, height=350, bd=0, relief='ridge',
                         highlightthickness=0)
        canvas5.place(x=200, y=200)
        button3 = HoverButton(canvas5, compound=TOP,width=270, height=270, bg="white",activebackground='white', image=photo_image19,
                              borderwidth=0, command=lambda:registrationUi(val=2), cursor="hand2")
        button3.place(x=520, y=100)
        button4 = HoverButton(canvas5, compound=TOP, width=270, height=270, bg="white",activebackground='white', image=photo_image18,
                              borderwidth=0, command=lambda: registrationUi(val=1), cursor="hand2")
        button4.place(x=240, y=100)
        back_button = HoverButton(canvas6, image=photo_image9,width=90, height=backButton_height, bg="white",activebackground='white', borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)

    except:
        log_except()

def clear_lab():

    lister = root.grid_slaves()
    for l in lister:
        l.destroy()

def registrationUi(val=None,patient=None,disorder=None):
    global canvas5,p_id, registrtionfill,patientid, excercise, entry3, canvas1, back, disordercombo, p_status, patient_entry, auto_text, patient_entry
    back.append(3)
    clear_lab()

    if canvas5 is not None:
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
    if numberChoosen1 is not None:
        numberChoosen1.destroy()
    # val=to identify the user came form new patient screen or edit patient screen
    # patient= when the patient already registered then try to register again then that time we receive the patient
    # disorder= add disorder time user added new disorder but its already available then that time this disorder will not none
    canvas5.config(height=0, width=0)
    canvas5.delete("all")

    Pid = StringVar()
    status = StringVar()
    reg_disorder=StringVar()
    canvas5 = Canvas(root, bg="white", width=800, height=400, bd=0, relief='ridge', highlightthickness=0)
    canvas5.place(x=400, y=210)
    if val==1:
        canvas5.create_text(310, 25, fill="black", font="Times 23 italic bold", text="New Patient Registration")
    if val == 2:
        canvas5.create_text(310, 25, fill="black", font="Times 23 italic bold", text="Update Patient Details")
    canvas5.create_text(180, 80, fill="black", font="Times 20 italic bold", text="Patient Id           : ")
    canvas5.create_text(180, 160, fill="black", font="Times 20 italic bold", text="Disorder            : ")
    canvas5.create_text(180, 240, fill="black", font="Times 20 italic bold", text="Patient Status      : ")
    if val==1:
        patient_entry = Entry(canvas5, textvariable=Pid, bd=3, width=11, font=font_size, validate="key")
    if val==2:
        result = []
        patientResult(3)  # p_id,bd=3,patientid
        for j in p_id:
            result.append(str(j))
        patient_entry = AutocompleteCombobox(canvas5, textvariable=Pid, width=10, font=font_size,
                                  height=1)  # AutocompleteEntry(list_of_items1,canvas5, listboxLength=6,,bd=3, width=11, font=font_size)#Entry(canvas5, textvariable=patientid, bd=3, width=11, font=font_size)
        patient_entry.set_completion_list(result)
    patient_entry.place(x=360, y=70)
    patient_entry.focus()
    patient_entry.delete(0, END)

    def autocapitalize(*arg):
        Pid.set(Pid.get().upper())

    Pid.trace("w", autocapitalize)

    # # Auto populate the patient status on right side of the patient entry id

    # auto_text = Label(canvas5, text="", bg="white", fg="blue", width=15, font="Times 13 bold")
    # auto_text.place(x=520, y=70)
    #
    # patient_entry.bind("<KeyRelease>", lambda event: on_enter(2))
    def autofill(val=None):
        if patient_entry.get()!="":
            if val != 1:
                patientResult(6)
                if len(p_id)!=0:

                    p_status.set(p_id[0][3])
                    disordercombo.delete(0,END)
                    disordercombo.set(p_id[0][2])
                else:
                    d = dialoguebox(root, text="             Patient id not found.\n Do you want to register the patient ?", buttons=["Yes", "No"], default=0, cancel=2,
                                    title=info, icon='Pictures/info.png')
                    if (d.go()) == 0:
                        registrationUi(1,patient=str(patient_entry.get()))
                    else:
                        patient_entry.focus()
                        return False
    if patient is not None:

        patient_entry.delete(0,END)
        patient_entry.insert(0,patient)
        patient_entry.bind("<FocusIn>", lambda event: autofill(val))

    else:
        patient_entry.bind("<FocusOut>",lambda event:autofill(val))

    disordercombo = ttk.Combobox(canvas5, textvariable=reg_disorder, width=10, font=font_size, height=4,
                                 state="readonly")
    disordercombo['values'] = disorder_input()
    disordercombo.bind('<<ComboboxSelected>>',lambda event: addField(val,disordercombo.get()))
    disordercombo.place(x=360, y=150)
    disordercombo.focus_set()
    disordercombo.delete(0, END)

    status = ["Active", "Inactive"]
    p_status = ttk.Combobox(canvas5, textvariable=status, width=10, font=font_size, height=4,
                            state="readonly")
    p_status['values'] = status
    p_status.current(0)
    p_status.place(x=360, y=230)
    p_status.focus_set()

    save_button = HoverButton(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                         width=15, command=lambda: saveDetails(val), activebackground='blue', cursor="hand2")
    save_button.place(x=240, y=300)

    back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white", borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
    back_button.place(x=50, y=580)

def addField(val,val1):
    global disorder_entry
    # val = it is 1 for New Patient else 2 for Update patient
    # val1 = to identify the user came form new patient screen or edit patient screen
    # val1 will have a value if user navigated from the Patient Exercise screen

    if val1=="Add Disorder":

        d_entry=StringVar()
        disorder_entry = Entry(canvas5, textvariable=d_entry, bd=3, width=15, font=font_size, validate="key")
        disorder_entry.place(x=560, y=150)
        disorder_entry.focus()
        disorder_entry.delete(0, END)
        lable_disorder=Label(canvas5, text="* Add Disorder", bg="white", fg="blue", width=50)
        lable_disorder.place(x=420,y=190)

        def autocapitalize(*arg):
            d_entry.set(d_entry.get().upper())

        d_entry.trace("w", autocapitalize)
        d_entry.trace("r", autocapitalize)
        save_button = HoverButton(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                  width=15, command=lambda: saveDetails(val,val1=str(disorder_entry.get())), activebackground='blue', cursor="hand2")
        save_button.place(x=240, y=300)

def patientResult(val=None,val1=None):
    global p_id,disordercombo
    p_id = []
    # patient_result = []
    conn = sqlite3.connect(json_const['DB_NAME'])
    c = conn.cursor()
    if val==1:
        c.execute("select * from PatientDetails where Patient_id='" + str(patient_entry.get()) + "' and Active_Flag='Active'")
    elif val==2:
        c.execute("SELECT Patient_id FROM PatientDetails where Active_Flag='Active' ")
    elif val==3:
        c.execute("select Patient_id from PatientDetails")
    elif val==4:
        c.execute("UPDATE PatientDetails SET Active_Flag =" + "'" + 'Active' + "'" + " where Patient_id=" + "'" + str(entry3.get()) + "'")
    elif val==5:
        c.execute("INSERT INTO PatientDetails(Patient_id, Disorder_id, Active_Flag) VALUES (?,?,?)",
                  (str(entry3.get()), disordercombo.get(),"Active"))
    elif val==6:
        c.execute("select * from PatientDetails where Patient_id='" + str(patient_entry.get()) + "'")
    elif val==7:
        if val1 is not None:
            c.execute("select * from PatientDetails where Patient_id='" + str(val1) + "' and Active_Flag='Active'")
    else:
        c.execute("select Disorder_id from PatientDetails where Patient_id='" + str(patient_entry.get()) + "'")
    if val==4 or val==5:
        conn.commit()
    else:
        if val==6 or val==7:
            for row in c.fetchall():
                p_id.append(row)
        else:
            for row in c.fetchall():
                p_id.append(row[0])

def saveDetails(val=None,val1=None):
    global disordercombo,p_status,patient_entry,disorder_entry
    # val= to identify the new user or edit user
    # val1= get the value like patient id and insert into the present screen disorder.

    if val1 is not None:

        if val1 in disorder_input():
            d = dialoguebox(root, text="Disorder "+"'"+str(val1)+"'"+" already exists.", buttons=["OK"], default=0,
                            cancel=2, title=info, icon='Pictures/info.png')
            if(d.go())==0:
                if val==2:
                    registrationUi(2, patient=patient_entry.get(),disorder=val1)
                else:
                    registrationUi(1, patient=patient_entry.get(), disorder=val1)
                return False

    patientResult()
    if patient_entry.get()=="":
        d = dialoguebox(root, text="Enter the Patient ID.", buttons=["OK"], default=0,
                        cancel=2, title=info, icon='Pictures/info.png')
        if (d.go()) == 0:
            patient_entry.focus()
        return False
    elif ( ' ' in str(patient_entry.get()) ):
        d = dialoguebox(root, text="Invalid Patient ID.", buttons=["OK"], default=0,
                        cancel=2, title=info, icon='Pictures/info.png')
        if (d.go()) == 0:
            patient_entry.focus()
        return False
    elif disordercombo.get()=="":
        d = dialoguebox(root, text="Select disorder from dropdown list.", buttons=["OK"], default=0,
                        cancel=2, title=info, icon='Pictures/info.png')
        if (d.go()) == 0:
            disordercombo.focus_set()
        return False
    elif disordercombo.get()=="Add Disorder" and val1=="" :
        d = dialoguebox(root, text="Add value for Disorder.", buttons=["OK"], default=0,
                        cancel=2, title=info, icon='Pictures/info.png')
        if (d.go()) == 0:
            # registrationUi(val, patient=patient_entry.get())
            disorder_entry.focus()
        return False
    elif disordercombo.get()!="Add Disorder" and val1 is not None :
        d = dialoguebox(root, text="Invalid Disorder combination.", buttons=["OK"], default=0,
                        cancel=2, title=info, icon='Pictures/info.png')
        if (d.go()) == 0:
            registrationUi(val, patient=patient_entry.get())
        return False
    elif val!=1:
       if len(p_id)!=0 :
           logging.info("Patient found.")
           d = dialoguebox(root, text="Do you want to update the patient details?", buttons=["Yes", "No"], default=0,cancel=2, title=info, icon='Pictures/info.png')
           if (d.go()) == 0:
               db_query(val,val1)
           return False
       else:
           logging.info("Patient not found.")
           d = dialoguebox(root, text="              Patient id not found. \n Do you want to register the patient ?", buttons=["Yes", "No"], default=0, cancel=2,
                           title=info, icon='Pictures/info.png')
           if (d.go()) == 0:
               registrationUi(1,patient=patient_entry.get())
           else:
               # registrationUi(2, patient=patient_entry.get())
                disordercombo.focus_set()
                return False
    else:
        if len(p_id) == 0:
            d = dialoguebox(root, text="Do you want to register the Patient ?", buttons=["Yes", "No"],default=0,cancel=2, title=info, icon='Pictures/info.png')

            if (d.go()) == 0:
                db_query(1,val1)
            return False
        else:
            logging.info("Patient found")
            d = dialoguebox(root, text="              Patient ID exists. \n Do you want to update the details?", buttons=["Yes", "No"], default=0,
                            cancel=2, title=info, icon='Pictures/info.png')

            if (d.go()) == 0:
                registrationUi(2,patient=patient_entry.get())
            return False

def db_query(val=None,val1=None):
    global disorder_entry
    # val= to identify the new user or edit user
    # val1= get the value like patient id and insert into the present screen disorder.

    conn = sqlite3.connect(json_const['DB_NAME'])
    c = conn.cursor()

    if val == 1:
        patient=str(patient_entry.get())
        if val1 is None:
            c.execute("INSERT INTO PatientDetails(Patient_id, Disorder_id, Active_Flag) VALUES (?,?,?)",
                      (patient, disordercombo.get(), p_status.get()))
        else:
            if val1 != "":
                c.execute("INSERT INTO PatientDetails(Patient_id, Disorder_id, Active_Flag) VALUES (?,?,?)",
                          (patient, val1, p_status.get()))
                conn.commit()
                logging.info("New Disorder added :  "+str(val1))
                c.execute("INSERT INTO PatientDisorder(Disorder) VALUES (?)",(val1,))
            else:
                logging.info("Disorder not created")
                d = dialoguebox(root, text="Failed to save the patient details.", buttons=["OK"], default=0,
                                cancel=2, title=info, icon='Pictures/info.png')
                if (d.go()) == 0:
                    registrationUi(val,patient)
                    return False
                else:
                    return False
    else:
        if val1 is not None:
            if val1!="":
                c.execute("INSERT INTO PatientDisorder(Disorder) VALUES (?)", (val1,))
                logging.info("New Disorder added :  " + str(val1))
                c.execute("UPDATE PatientDetails SET Active_Flag = ?,Disorder_id=? where Patient_id=" + "'" + str(
                    patient_entry.get()) + "'",  (p_status.get(), val1))
                conn.commit()
            else:
                logging.info("Disorder not created.")
                d = dialoguebox(root, text="Failed to save the patient details.", buttons=["OK"], default=0,
                                cancel=2, title=info, icon='Pictures/info.png')
                if (d.go()) == 0:
                    registrationUi(val, str(patient_entry.get()))
                    return False
                else:
                    return False
        else:
            c.execute("UPDATE PatientDetails SET Active_Flag = ?,Disorder_id=? where Patient_id=" + "'" + str(
                patient_entry.get()) + "'",
                      (p_status.get(), disordercombo.get()))

    d = dialoguebox(root, text="Details saved successfully.", buttons=["OK"], default=0,
                    cancel=2, title=info, icon='Pictures/info.png')
    conn.commit()
    if (d.go()) == 0:
        registrationUi(val)

def utilities(user=None):
    try:

        global canvas5, patientid, excercise, entry3, canvas1, back
        back.append(2)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")

        toprightmostpart()
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold",
                            text="Utilities")

        if user == "admin":
            text="Config \n Management"
            canvas5 = Canvas(root, bg="white", width=1100, height=350, bd=0, relief='ridge', highlightthickness=0)
            canvas5.place(x=200, y=270)
        else:
            text = "Change \nDevice"
            canvas5 = Canvas(root, bg="white", width=700, height=350, bd=0, relief='ridge', highlightthickness=0)
            canvas5.place(x=400, y=270)
        button3 = HoverButton(canvas5, activebackground='orange', cursor="hand2", compound=TOP, pady=30, bg="sky blue",
                              width=20, height=5, wraplength=150, text="Support \nUtility",
                              command=lambda: support_utilities(),
                              font=('Helvetica bold', '16'))  # command=lambda: managelicense()
        button3.place(x=380, y=10)

        button1 = HoverButton(canvas5, compound=TOP, pady=30, bg="sky blue", width=20, height=5, wraplength=150,
                              text=text, font=('Helvetica bold', '16'), command=lambda:configmanage(2),
                              activebackground='orange', cursor="hand2")
        if user == "admin":
            button1.place(x=30, y=10)
        else:
            with open('Const/config.json') as i:
                json_const = json.load(i)
                MULTI_DEVICE = json_const['MULTI_DEVICE']
            if MULTI_DEVICE=="Y":
                button1.place(x=30, y=10)
                button3.place(x=380, y=10)
                button1.config(command=lambda: configmanage(2))
            else:
                button1.destroy()
                button3.place(x=200, y=10)

        if user=="admin":

            button1.config( command=lambda: configmanage(1))

            button2 = HoverButton(canvas5, activebackground='orange', cursor="hand2", compound=TOP, pady=30, bg="sky blue",
                                  width=20, height=5, wraplength=150, text="License \n Management",command=lambda:managelicense() ,font=('Helvetica bold', '16'))#command=lambda:configmanage(2)
            button2.place(x=720, y=10)




        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white", borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)
    except:
        log_except()

def support_utilities():
    cmd="supportutil.exe"
    # subprocess.Popen(cmd, shell=True)
    subprocess.Popen(cmd,creationflags=subprocess.CREATE_NEW_CONSOLE)


def managelicense():
    global canvas5,texttit, canvas1,entry3,entry4,entry5,curSession_entry, session_entry, license_endentry, license_entry,result2
    logging.info("In manage license .")
    back.append(11)
    if canvas1 is not None:
        canvas1.config(height=0, width=0)
        canvas1.delete("all")
    if canvas4 is not None:
        canvas4.config(height=0, width=0)
        canvas4.delete("all")
    if entry3 is not None:
        entry3.destroy()
    if entry4 is not None:
        entry4.destroy()
    if entry5 is not None:
        entry5.destroy()

    canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                     highlightthickness=5)
    canvas1.place(x=0, y=0)
    canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="License Management")
    canvas5.config(height=0, width=0)
    canvas5.delete("all")
    canvas5 = Canvas(root, bg="white", width=1150, height=460, bd=0, relief='ridge',
                     highlightthickness=0)
    canvas5.place(x=150, y=190)
    if os.path.isfile("Const/license.json"):
        # checks if file exists
        logging.info("License File exists and is readable.")
        texttit=canvas5.create_text(550, 10, fill="black", font="Times 22  bold", text="Update Licenses ")

    else:
        now = datetime.datetime.now()
        dt_string = now.strftime("%Y-%m-%d")
        m = dt_string
        mBytes = m.encode("utf-8")
        mInt = int.from_bytes(mBytes, byteorder="big")

        logging.info("Either file is missing or is not readable, creating file...")
        import io
        with io.open(os.path.join("Const/license.json"), 'w') as data:
            data.write(json.dumps({}))
        person = {
            "6645463761731833437523489052997651110384709": mInt,
            "6044014082119095689857058819668": 48,
            "6645463761731833437447950861006883695971924": 48,
            "101401729762753806113544700036426847301": mInt,
        }

        with open('Const/license.json', 'w') as f:  # writing JSON object
            json.dump(person, f)
        canvas5.create_text(550, 10, fill="black", font="Times 22  bold", text="Create Licenses ")
    canvas5.create_text(200, 100, fill="black", font=lable_font, text="License Start Date        : ")
    canvas5.create_text(750, 100, fill="black", font=lable_font, text="License End Date          : ")
    canvas5.create_text(200, 200, fill="black", font=lable_font, text="Total Session Count     : ")
    canvas5.create_text(750, 200, fill="black", font=lable_font, text="Pending Session Count   : ")
    licenseEntry=StringVar()
    licensEendEntry=StringVar()
    sessionCount=IntVar()
    sessionCurCount=IntVar()

    with open('Const/license.json') as i:
        json_const = json.load(i)
        keyval = json_const['6645463761731833437523489052997651110384709']  # 237007384299206171504696
        mBytes2 = keyval.to_bytes(((keyval.bit_length() + 7) // 8), byteorder="big")
        license_start = mBytes2.decode("utf-8")
        logging.info("License Start Date is : " + str(license_start) )

        keyval = json_const['101401729762753806113544700036426847301']  # 237007384299206171504696
        mBytes2 = keyval.to_bytes(((keyval.bit_length() + 7) // 8), byteorder="big")
        license_end = mBytes2.decode("utf-8")
        logging.info( "License End Date is : " + str(license_end) )

        keyval = json_const['6044014082119095689857058819668']  # 237007384299206171504696
        mBytes2 = keyval.to_bytes(((keyval.bit_length() + 7) // 8), byteorder="big")
        session_count = mBytes2.decode("utf-8")
        logging.info("Total Session Count : " + str(session_count) )

        keyval = json_const['6645463761731833437447950861006883695971924']  # 237007384299206171504696
        mBytes2 = keyval.to_bytes(((keyval.bit_length() + 7) // 8), byteorder="big")
        session_curcount = mBytes2.decode("utf-8")
        logging.info("Current Session Count : " + str(session_curcount) )

    def help(helpval):
        d = dialoguebox(root, text="Click on the calendar icon to edit date.", buttons=["OK"], default=0,
                        cancel=2, title=info, icon='Pictures/info.png')
        if (d.go()) == 0:
            if helpval==1:
                cal_wid1.focus_set()

            if helpval==2:
                cal_wid2.focus_set()

    license_entry = Entry(canvas5, textvariable=licenseEntry, bd=3, width=11, font=font_size)
    license_entry.place(x=360, y=85)
    license_entry.bind('<FocusIn>', lambda event: help(1))
    license_entry.insert(0, license_start)
    result2=license_entry.get()
    cal_wid1 = HoverButton(canvas5, compound=LEFT, bg="white",
                       activebackground="blue", image=photo_image14, width=20, height=20,
                       borderwidth=1,
                       command=lambda: cal_widget(value=1), cursor="hand2")
    cal_wid1.place(x=485, y=89)

    license_endentry = Entry(canvas5, textvariable=licensEendEntry, bd=3, width=11, font=font_size)
    license_endentry.place(x=900, y=85)

    license_endentry.insert(0, license_end)
    license_endentry.bind('<FocusIn>', lambda event: help(2))

    result1=license_endentry.get()

    cal_wid2 = HoverButton(canvas5, compound=LEFT, bg="white",
                          activebackground="blue", image=photo_image14, width=20, height=20,
                          borderwidth=1, command=lambda: cal_widget(value=2), cursor="hand2")
    cal_wid2.place(x=1025, y=89)

    session_entry = Entry(canvas5, textvariable=sessionCount, bd=3, width=11, font=font_size, validate="key")
    session_entry['validatecommand'] = (session_entry.register(testVal), '%P', '%d')
    session_entry.place(x=360, y=185)
    session_entry.focus()
    session_entry.delete(0, END)
    session_entry.insert(0,session_count)

    curSession_entry = Entry(canvas5, textvariable=sessionCurCount, bd=3, width=11, font=font_size, validate="key")
    curSession_entry['validatecommand'] = (curSession_entry.register(testVal), '%P', '%d')
    curSession_entry.place(x=900, y=185)
    curSession_entry.focus()
    curSession_entry.delete(0, END)
    curSession_entry.insert(0, session_curcount)

    save_button = Button(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                         width=15,command=savelicense , activebackground='blue', cursor="hand2")
    save_button.place(x=500, y=270)

def savelicense():
    global curSession_entry,session_entry,license_endentry,license_entry,result2,result1

    with open('Const/license.json', "r") as jsonFile:
        data = json.load(jsonFile)

    m = result2
    mBytes = m.encode("utf-8")
    n = int.from_bytes(mBytes, byteorder="big")

    o= result1
    mBytes = o.encode("utf-8")
    p = int.from_bytes(mBytes, byteorder="big")

    q = session_entry.get()
    mBytes = q.encode("utf-8")
    r = int.from_bytes(mBytes, byteorder="big")
    if curSession_entry.get() is not None:
        s = curSession_entry.get()
        mBytes = s.encode("utf-8")
        t = int.from_bytes(mBytes, byteorder="big")
    else :
        print("In none session")

    d = dialoguebox(root, text="Do you want to save the changes ? ", buttons=["Yes", "No"], default=0,
                    cancel=2, title=info, icon='Pictures/info.png')
    if (d.go()) == 0:
        data["6645463761731833437523489052997651110384709"] = n
        data["6044014082119095689857058819668"] =r
        data["6645463761731833437447950861006883695971924"] =t
        data["101401729762753806113544700036426847301"] = p
    with open('Const/license.json', "w") as jsonFileData:
        json.dump(data, jsonFileData)

def cal_widget(value=None,fromfun=None):

    global cal,top_cal,result_cal,license_entry,license_endentry

    top_cal = Toplevel(root)
    top_cal.transient(canvas5)
    global Calendar
    from tkcalendar import Calendar
    top_cal.title("Calendar")
    top_cal.grab_set()
    top_cal.geometry("400x250+500+250")
    top_cal.focus()
    img = PhotoImage(file="Pictures/info.png")
    top_cal.tk.call('wm', 'iconphoto', top_cal._w, img)
    if value==1:
        try:
            day_val=(license_entry.get()).split(sep="-")
            cal = Calendar(top_cal, font="Arial 12", selectmode='day', cursor="hand2", year=int(day_val[0]), month=int(day_val[1]), day=int(day_val[2]))
            # cal.selection_set("%x")
            cal.pack(fill="both", expand=False)
        except:
            standerdtime()
    elif value==2:
        try:
            day_val = (license_endentry.get()).split(sep="-")
            cal = Calendar(top_cal, font="Arial 12", selectmode='day', cursor="hand2",  year=int(day_val[0]), month=int(day_val[1]), day=int(day_val[2]))
            cal.pack(fill="both", expand=False)
        except:
            standerdtime()
    else:
        try:
            now = datetime.datetime.now()
            dt_string = now.strftime("%Y-%m-%d")
            day_val = dt_string.split(sep="-")
            cal = Calendar(top_cal, font="Arial 12", selectmode='day', cursor="hand2", year=int(day_val[0]), month=int(day_val[1]), day=int(day_val[2]))
            cal.pack(fill="both", expand=False)
        except:
            standerdtime()
    calender_endbutton=HoverButton(top_cal, text="OK",width=8,font="Calibri 18 bold", command= lambda: print_sel(value,fromfun=fromfun),cursor="hand2").pack()

    top_cal.wait_window()

def standerdtime():
    global cal
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%d")
    day_val = dt_string.split(sep="-")
    cal = Calendar(top_cal, font="Arial 12", selectmode='day', cursor="hand2", year=int(day_val[0]), month=int(day_val[1]), day=int(day_val[2]))
    cal.pack(fill="both", expand=False)

def print_sel(val,fromfun=None):
    global cal,top_cal,result_cal,license_entry,license_endentry,result2,result1

    result_cal = str(cal.selection_get())
    if val==1:
        license_entry = Entry(canvas5, textvariable=patientid, bd=3, width=11, font=font_size)
        if fromfun is not None :
            logging.info("from fun is not none")
            license_entry.config(textvariable=reportStart)
            license_entry.place(x=160, y=230)
        else:
            license_entry.config(textvariable=patientid)
            license_entry.place(x=360, y=85)

        license_entry.delete(0, END)
        license_entry.insert(0,result_cal)
        cal_wid = HoverButton(canvas5, compound=LEFT, bg="white",
                              activebackground="blue", image=photo_image14, width=20, height=20,
                              borderwidth=1,  command=lambda: cal_widget(1,fromfun=fromfun), cursor="hand2")
        if fromfun is not None :
            cal_wid.place(x=315, y=235)
        else:
            cal_wid.place(x=485, y=89)
        result2 = license_entry.get()
    if val==2:
        license_endentry = Entry(canvas5, textvariable=patientid, bd=3, width=11, font=font_size)
        if fromfun is not None :
            license_endentry.config(textvariable=reportEnd)
            license_endentry.place(x=500, y=230)
        else:
            license_endentry.config(textvariable=patientid)
            license_endentry.place(x=900, y=85)
        license_endentry.delete(0, END)
        license_endentry.insert(0, result_cal)
        cal_wid = HoverButton(canvas5, compound=LEFT, bg="white",
                              activebackground="blue", image=photo_image14, width=20, height=20,
                              borderwidth=1,  command=lambda: cal_widget(2,fromfun=fromfun), cursor="hand2")
        if fromfun is not None :
            cal_wid.place(x=655, y=235)
        else:
            cal_wid.place(x=1025, y=89)
        result1=license_endentry.get()
    top_cal.grab_release()
    top_cal.withdraw()

def configmanage(val=None):
    global canvas5,canvas1,config,key_value,entry_config,prevlaue,keyop,text_data
    try:
        if license_entry is not None:
            print("im in global area" + str(license_entry.get()))

        back.append(11)

        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if entry3 is not None:
            entry3.destroy()
        if entry4 is not None:
            entry4.destroy()
        if entry5 is not None:
            entry5.destroy()
        if canvas5 is not None:
            canvas5.delete(text)
        if entry_config is not None:
            entry_config.destroy()
        if val==1:

            with open('Const/config.json') as i:
                test = json.load(i)
            list = []
            for key in test.keys():
                list.append(key)
        elif val==2:
            list=['BLE_DEVICE_MAC_ADD']
        config = StringVar()
        configkey=StringVar()
        prevlaue = key_value=None
        if val == 1:
            text1 = "Config Management"
        elif val == 2:
            text1 = "Support Utilities"

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text=text1)
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
        canvas5 = Canvas(root, bg="white", width=1150, height=460, bd=0, relief='ridge',  highlightthickness=0)
        canvas5.place(x=150, y=190)
        if val==1:

            canvas5.create_text(310, 90, fill="black", font="Times 20 bold", text="Config Key             : ")
            config = ttk.Combobox(canvas5, textvariable=config, width=33, font="Calibri 15", height=5,state="readonly")
            config['values'] = list
            config.bind('<FocusIn>', lambda event: edit(val=val,val1=config.get()))
            config.current(0)
            config.focus_set()
            config.place(x=500, y=80)
            canvas5.create_text(310, 150, fill="black", font="Times 20 bold", text="Config Value           :  ")
            entry_config = Entry(canvas5, textvariable=configkey, bd=3, width=35, font="Calibri 15")
            entry_config.bind('<KeyRelease>', lambda event: edit(val=val))
            entry_config.bind('<FocusIn>', lambda event: edit(val=val))
            entry_config.delete(0, END)
            entry_config.place(x=500, y=140)
        elif val==2:
            canvas5.create_text(580, 90, fill="black", font="Times 20 bold", text="Change Device")
            # edit(val=val,val1='BLE_DEVICE_MAC_ADD')
            with open('Const/config.json') as i:
                json_const = json.load(i)
                insert_value = json_const['BLE_DEVICE_MAC_ADD']
                logging.info(insert_value)
                # text_data = canvas5.create_text(600, 200, fill="black", font="Times 13",
                #                             text="(Current Device : " + str(insert_value) + ")")
                text_data = Label(canvas5, font="Times 13",text="(Current Device : " + str(insert_value) + ")", bg="white", fg="blue", width=50)
                text_data.place(x=680, y=140)
            try:
                with open('Const/mac_id.json') as i:
                    keyop = 'BLE_DEVICE_MAC_ADD'
                    json_const = json.load(i)
                    key_value = json_const['BLE_DEVICE_MAC_ADD']
                    logging.info("Key value: " + str(key_value))

                    if insert_value in key_value:
                        logging.info("Old Mac id " + str(insert_value) )
                        logging.info("New Mac id " + str(key_value) )
            except:
                print("MAC_Id .json file not Found in const folder")

            entry_config = ttk.Combobox(canvas5, textvariable=configkey, width=33, font="Calibri 15", height=3,state="readonly")
            entry_config['values'] = [x for x in key_value if x != insert_value]#key_value

            entry_config.pack()

            entry_config.place(x=400, y=140)
            button_edit = Button(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                 width=15, command=lambda: save(val), activebackground='blue', cursor="hand2")
            button_edit.place(x=480, y=270)
        if val==2:
            entry_config.set("hello world")
            button_edit = Button(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                 width=15, command=lambda: save(val), activebackground='blue', cursor="hand2")
            button_edit.place(x=480, y=270)

        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, borderwidth=0, font=('Helvetica', '15'),
                              command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)
        toprightmostpart()
    except:
        log_except()


def do_update():
    global text_data,entry_config

    logging.info(type(text_data))
    with open('Const/config.json') as i:
        json_const = json.load(i)
        insert_value = json_const['BLE_DEVICE_MAC_ADD']
        logging.info(insert_value)
    text_data.configure(text="(Current Device : " + str(insert_value) + ")")
    entry_config['values'] = [x for x in key_value if x != insert_value]


def save(val=None):
    global config, key_value,value1,m,keyop,entry_config,tmp,previousType

    if val==1:
        logging.info("entered into if val=="+str(val))
        if entry_config.get() != "" and config.get != "":
            with open("Const/config.json", "r") as jsonFile:
                data = json.load(jsonFile)
                tmp = data[keyop]
                previousType = type(tmp)
    elif val==2:
        logging.info("entered into if val==" + str(val))
        with open("Const/config.json", "r") as jsonFile:
            data = json.load(jsonFile)
            tmp = data["BLE_DEVICE_MAC_ADD"]
            previousType = type(tmp)

    if previousType==int:
        global m

        try:
            if val==1:
                m =int(entry_config.get())
            if val==2:
                m = int(entry_config.get())
            d = dialoguebox(root, text="Do you want to save changes ? ", buttons=["Yes","No"], default=0,
                            cancel=2, title=info, icon='Pictures/info.png')
            if (d.go())==0:
                data[keyop] = m

            else:
                data[keyop] = tmp
        except:

            d = dialoguebox(root, text="Enter an integer value", buttons=["OK"], default=0,
                            cancel=2, title=info, icon='Pictures/info.png')
            if (d.go())==0:
                m=tmp
                print("pleasae enter integer values")
    else:
        m = entry_config.get()
        d = dialoguebox(root, text="Do you want to save changes ? ", buttons=["Yes", "No"], default=0,
                        cancel=2, title=info, icon='Pictures/info.png')
        if (d.go()) == 0:
            with open("Const/config.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data[keyop] = m

    if val==1:
        with open('Const/config.json', "w") as jsonFileData:
            json.dump(data, jsonFileData)
            logging.info("Successfully Updated json key and values are: Key : " + str(keyop) + "  and  value: " + str(m))
    if val == 2:
        with open('Const/config.json', "w") as jsonFileData:
            json.dump(data, jsonFileData)
            logging.info(
                "Successfully Updated json key and values are: Key : " + str(keyop) + "  and  value: " + str(m))
        do_update()
def edit(val=None,val1=None):
    try:
        global key_value,entry_config,keyop
        # entry_config.focus()
        logging.info("edit function called")
        config = StringVar()
        configkey = StringVar()
        if entry_config is not None:
            entry_config.delete(0, END)
        if val1!="":
            if val==1:
                with open('Const/config.json') as i:
                    json_const = json.load(i)
                    keyop = val1
                    logging.info("Key output value: "+str(keyop))
                    key_value = json_const[keyop]
                    entry_config = Entry(canvas5, textvariable=configkey, bd=3, width=35, font="Calibri 15")
                    entry_config.focus()
                    entry_config.insert(0, key_value)
                    entry_config.place(x=500, y=140)

        button_edit = Button(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                             width=15, command=lambda:save(val), activebackground='blue', cursor="hand2")
        button_edit.place(x=350, y=270)
        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, borderwidth=0, font=('Helvetica', '15'),
                              command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)
        toprightmostpart()
    except:
        log_except()

def initialmiddlepart():
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
        if reportGameGraph is not None:
            reportGameGraph.destroy()

        if canvas is not None:
            canvas.destroy()
        if entry3 is not None:
            entry3.destroy()

        login = 0
        username = StringVar()
        password = StringVar()
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Login")
        canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40, height=root.winfo_screenheight() - 165,
                         highlightbackground="blue", highlightthickness=20)
        canvas2.place(x=0, y=30)

        # Images
        photo_image2 = ImageTk.PhotoImage(image2)
        canvas2.create_image(150, 100, image=photo_image2)
        photo_image3 = ImageTk.PhotoImage(image3)
        canvas2.create_image(300, 100, image=photo_image3)
        canvas5 = Canvas(root, bg="white", width=550, height=350, bd=0, relief='ridge',
                         highlightthickness=0)  # , highlightbackground="black", highlightthickness=5)
        canvas5.place(x=400, y=210)  # int(root.winfo_screenheight()/2)),
        canvas5.create_text(310, 40, fill="black", font="Times 25 italic bold", text="Soujhe App System Login")
        canvas5.create_text(150, 120, fill="black", font="Times 20 italic bold", text="User ID    : ")
        canvas5.create_text(150, 190, fill="black", font="Times 20 italic bold", text="Password : ")

        entry1 = Entry(canvas5, textvariable=username, bd=3, width=20, font=font_size)
        entry1.place(x=250, y=110)
        entry1.focus()
        entry1.delete(0, END)

        entry2 = Entry(canvas5, show="*", textvariable=password, bd=3, width=20, font=font_size)
        entry2.place(x=250, y=180)
        entry2.delete(0, END)

        button1 = HoverButton(canvas5, text="Login", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                              command=checkLogIn, width=15, activebackground='blue', cursor="hand2")
        button1.place(x=110, y=270)

        button2 = HoverButton(canvas5, text="Exit", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                              command=lambda: on_closing(), width=15, activebackground='blue', cursor="hand2")
        button2.place(x=320, y=270)

        toprightmostpart()
    except:
        log_except()

def loginpage() :
    try:

        global canvas1, canvas2, canvas3, canvas4, photo_image2, photo_image3, username, password, back, photo_image9
        username = StringVar()
        password = StringVar()
        if len(back) > 0:
            back[:] = []

        if canvas2 is not None:
            canvas2.config(height=0, width=0)
            canvas2.delete("all")
        if canvas3 is not None:
            canvas3.config(height=0, width=0)
            canvas3.delete("all")

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Login")
        canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40, height=root.winfo_screenheight() - 165,
                         highlightbackground="blue", highlightthickness=20)
        canvas2.place(x=0, y=30)
        canvas3 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas3.place(x=0, y=root.winfo_screenheight() - 95)
        canvas3.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 10 italic bold",
                            text="2019 © Soujhe Innovative Healthcare Devices Pvt. Ltd.")

        # Images
        photo_image2 = ImageTk.PhotoImage(image2)
        canvas2.create_image(150, 100, image=photo_image2)
        image3 = Image.open("Pictures/company_logo.png")
        image3 = image3.resize((150, 100), Image.ANTIALIAS)
        photo_image3 = ImageTk.PhotoImage(image3)
        canvas2.create_image(250, 100, image=photo_image3)

        button2 = HoverButton(canvas2, image=photo_image9, width=90, height=backButton_height, borderwidth=0, font=('Helvetica', '15'),
                              command=backpage, cursor="hand2")
        button2.place(x=50, y=580)

        initialmiddlepart()
    except:
        log_except()

def checkServer():
    import requests
    try:

        logging.info("Running server check")
        while True:
            try:
                s.connect((json_const["SOCKET_HOST"], int(json_const["SOCKET_PORT"])))
                s.sendall(encode_msg('me,ui'))
                import threading
                receive_thread = threading.Thread(target=receive)
                receive_thread.start()
                return
            except requests.exceptions.ConnectionError:
                logging.info("Server is not ready")
                time.sleep(1) # Sleep for a second before retrying
                pass
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                logging.info("Exception in checkServer : " + message)
                time.sleep(1)  # Sleep for a second before retrying
                pass
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

def returningDuration():
    global durationOfTheGame
    return durationOfTheGame

def loading():
    try:
        global l
        if l < 1:
            canvas2.create_text(600 + l * 20, 680, fill="black", font="Times 15 italic bold",
                                text="2019 © Soujhe Innovative Healthcare Devices Pvt. Ltd. ")
            root.after(2000, loading)
            l = l + 1
        else:
            loginpage()
    except:
        log_except()

def openServer():
    try:
        if envMode == "development":
            cmd = "python socket_manager.py"
            opening = subprocess.Popen(cmd, shell=True).pid
        else:
            if (platform.system() == "Windows"):
                cmd = "socket_manager.exe"
            else:
                cmd = "./socket_manager"

            opening = subprocess.Popen(cmd, shell=True).pid
    except:
        log_except()

def checkExistingInstance():
    global psutil
    import psutil
    logging.info("Checking for any existing instances.")
    val = [procObj for procObj in psutil.process_iter() if'tkinter_ui' in procObj.name().lower()] or [procObj for procObj in psutil.process_iter() if
                                                         'soujhe' in procObj.name().lower()]
    obj=len(val)
    logging.info("Found existing instances : " + str(val))
    if obj>2 : # Means there is an existing instance already running
        logging.info("A program instance is already open." + str(val) )
        logging.info(" Length of obj is : " + str(obj) )
        d = dialoguebox(root, text="Program is already running.", buttons=["OK"], default=0,
                       cancel=2, title=error, icon='Pictures/error.png')
        d.go()
        force_kill()
    else:
        loading()
        if (platform.system() == "Windows"):
            openFile("database_Server")
        else:
            openFile("./database_Server")
        openServer()

checkExistingInstance()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
if (platform.system()=="Linux"):
    root.attributes('-zoomed', True)
else:
    root.state('zoomed')

root.protocol("WM_DELETE_WINDOW", on_closing)
root.after(2000, checkServer)
img = PhotoImage(file='Pictures/icon_s.png')
root.tk.call('wm', 'iconphoto', root._w, img)

root.mainloop()